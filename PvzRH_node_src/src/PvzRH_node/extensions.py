from . import nodes, api
from .core import ctx
from .node_base import ExecutionPath, BaseNode
from enum import Enum
from .TypeMgr import PlantType, ZombieAnimation, ZombieType
from typing import Any, Final, Union, Iterable, Optional
from enum import Enum



class If:
    """Syntactic sugar that acts as a safe visual scripting 'if/elif/else' block."""
    def __init__(self, condition):
        self.node = nodes.branch_node(condition=condition)
        
    def __enter__(self):
        self.node.Output.Then.__enter__()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.node.Output.Then.__exit__(exc_type, exc_val, exc_tb)
        
    @property
    def Else(self):
        return self.node.Output.Else
        
    def Elif(self, condition):
        ctx.trigger_stack.append(self.node.Output.Else)
        new_branch = If(condition)
        ctx.trigger_stack.pop()
        return new_branch

class Switch:
    """
    Syntactic sugar for transpiling 'switch-case' branching statements.
    
    Usage:
        with pvn.Switch(plant.plantType) as sw:
            with sw.case(PlantType.SunFlower):
                pvn.nodes.add_sun(100)
                
            with sw.case(PlantType.Peashooter, PlantType.GatlingPea):
                pvn.nodes.add_sun(50)
                
            with sw.default:
                pvn.nodes.add_sun(10)
    """
    def __init__(self, target):
        self.target = target
        self.last_false_path = None
        self.parent_trigger = ctx.trigger_stack[-1] if ctx.trigger_stack else None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def case(self, *values):
        if len(values) == 1 and isinstance(values[0], (list, tuple, set)):
            values = tuple(values[0])
        return _SwitchCase(self, values)

    @property
    def default(self):
        return _SwitchDefault(self)

class _SwitchCase:
    def __init__(self, switch_obj, values):
        self.switch = switch_obj
        self.values = values
        self.branch_node = None

    def __enter__(self):
        condition = (self.switch.target == self.values[0])
        for val in self.values[1:]:
            condition = condition | (self.switch.target == val)

        # 🎯 THE FIX: Temporarily hide the stack to prevent parallel auto-wiring!
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()
        
        self.branch_node = nodes.branch_node(condition=condition)
        
        ctx.trigger_stack.extend(saved_stack)

        # Now explicitly wire it in a sequential chain (False -> Next Case)
        if self.switch.last_false_path is not None:
            ctx.add_connection(
                self.switch.last_false_path.id,
                self.switch.last_false_path.out_trigger,
                self.branch_node.id,
                "触发"
            )
        elif ctx.trigger_stack:
            curr = ctx.trigger_stack[-1]
            ctx.add_connection(curr.id, curr.out_trigger, self.branch_node.id, "触发")

        # Update the False path chain for the next case or default block
        self.switch.last_false_path = ExecutionPath(self.branch_node.id, "假（停止）")

        # Push the True branch onto trigger stack for statements inside this case
        ctx.trigger_stack.append(ExecutionPath(self.branch_node.id, "真（触发）"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

class _SwitchDefault:
    def __init__(self, switch_obj):
        self.switch = switch_obj

    def __enter__(self):
        if self.switch.last_false_path is not None:
            ctx.trigger_stack.append(self.switch.last_false_path)
        elif self.switch.parent_trigger:
            ctx.trigger_stack.append(self.switch.parent_trigger)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()
    

#region Variables

class IntVar:
    """Use to create a Variable Int Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=0, node_ref=None, name: str = "整数"):
        self._nodes_by_scope = {}
        
        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = start_val if isinstance(start_val, int) and not isinstance(start_val, bool) else 0
            self._node = nodes.int_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node
            
            if not isinstance(start_val, int) or isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_int_variable_value(
                    variable=self.variable, 
                    value=self._cast_to_int(start_val)
                )
                ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self):
        scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if self._asset_dict:
                new_node = nodes.int_variable(asset_dict=self._asset_dict)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self): return False
    def _get_primary_port(self): return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_int_variable_value(variable=self.variable).value
        
    def set(self, target_value):
        if target_value is self:
            return self
            
        casted_val = self._cast_to_int(target_value)
        return nodes.set_int_variable_value(variable=self.variable, value=casted_val)

    def _cast_to_int(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "IntVar": return val.value
        if cls_name == "FloatVar": return nodes.float_to_int(float_val=val.value).int
        if cls_name == "BoolVar": 
            raise TypeError("❌ Type Error: Cannot implicitly cast a BoolVar to an IntVar.")
            
        if isinstance(val, bool): return 1 if val else 0
        if isinstance(val, int): return val
        if isinstance(val, float): return int(val)
            
        if hasattr(val, 'node'):
            t = val.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: return nodes.float_to_int(float_val=val).int
            return val
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to IntVariable.")

    def to_string(self, decimals=0):
        from .nodes import int_to_float, float_to_string, int_value
        f_val = int_to_float(int_val=self.value).float
        dec_node = int_value(val=decimals).value 
        return float_to_string(float_val=f_val, decimals=dec_node).result

    def __iadd__(self, other): self.set(nodes.int_add(a=self.value, b=self._cast_to_int(other)).result); return self
    def __isub__(self, other): self.set(nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result); return self
    def __imod__(self, other): self.set(nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result); return self

    def __add__(self, other): return nodes.int_add(a=self.value, b=self._cast_to_int(other)).result
    def __radd__(self, other): return nodes.int_add(a=self._cast_to_int(other), b=self.value).result
    def __sub__(self, other): return nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result
    def __rsub__(self, other): return nodes.int_subtract(a=self._cast_to_int(other), b=self.value).result
    def __mod__(self, other): return nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result
    def __rmod__(self, other): return nodes.int_modulo(a=self._cast_to_int(other), b=self.value).result
    
    def __itruediv__(self, other):
        from .nodes import int_to_float, divide_node, float_to_int, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division.")

        f_result = divide_node(a=f_self, b=f_other).result
        self.set(float_to_int(float_val=f_result).int)
        return self

    def __truediv__(self, other):
        from .nodes import int_to_float, divide_node, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division.")
            
        return divide_node(a=f_self, b=f_other).result

    def __rtruediv__(self, other):
        from .nodes import int_to_float, divide_node, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported dividend type '{type(other).__name__}' for division.")
            
        return divide_node(a=f_other, b=f_self).result

    def __ifloordiv__(self, other): self.set(nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result); return self
    def __floordiv__(self, other): return nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result
    def __rfloordiv__(self, other): return nodes.int_divide(a=self._cast_to_int(other), b=self.value).result

    def __imul__(self, other):
        from .nodes import int_to_float, multiply_node, float_to_int, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            f_result = multiply_node(a=f_self, b=f_other).result
            self.set(float_to_int(float_val=f_result).int)
        else: self.set(int_multiply(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __mul__(self, other):
        from .nodes import int_to_float, multiply_node, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            return multiply_node(a=f_self, b=f_other).result
        else: return int_multiply(a=self.value, b=self._cast_to_int(other)).result

    def __rmul__(self, other):
        from .nodes import int_to_float, multiply_node, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            return multiply_node(a=f_other, b=f_self).result
        else: return int_multiply(a=self._cast_to_int(other), b=self.value).result
        
    def __eq__(self, other): return self.value == self._cast_to_int(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_int(other) #type: ignore
    def __gt__(self, other): return self.value > self._cast_to_int(other)
    def __lt__(self, other): return self.value < self._cast_to_int(other)
    def __ge__(self, other): return self.value >= self._cast_to_int(other)
    def __le__(self, other): return self.value <= self._cast_to_int(other)

class FloatVar:
    """Use to create a Variable Float Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=0.0, node_ref=None, name: str = "浮点数"):
        self._nodes_by_scope = {}
        
        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = float(start_val) if isinstance(start_val, (int, float)) and not isinstance(start_val, bool) else 0.0
            self._node = nodes.float_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, (int, float)) or isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_float_variable_value(
                    variable=self.variable, 
                    value=self._cast_to_float(start_val)
                )
                ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self):
        scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if self._asset_dict:
                new_node = nodes.float_variable(asset_dict=self._asset_dict)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self): return True
    def _get_primary_port(self): return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_float_variable_value(variable=self.variable).value

    def set(self, target_value):
        if target_value is self:
            return self
            
        casted_val = self._cast_to_float(target_value)
        return nodes.set_float_variable_value(variable=self.variable, value=casted_val)

    def _cast_to_float(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "FloatVar": return val.value
        if cls_name == "IntVar": return nodes.int_to_float(int_val=val.value).float
        if cls_name == "BoolVar": 
            raise TypeError("❌ Type Error: Cannot implicitly cast a BoolVar to a FloatVar.")
            
        if isinstance(val, bool): return 1.0 if val else 0.0
        if isinstance(val, float): return val
        if isinstance(val, int): return float(val)
            
        if hasattr(val, 'node'):
            t = val.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: return nodes.int_to_float(int_val=val).float
            return val
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to FloatVar.")

    def to_string(self, decimals=2):
        from .nodes import float_to_string, int_value
        dec_node = int_value(val=decimals).value 
        return float_to_string(float_val=self.value, decimals=dec_node).result

    def __iadd__(self, other): self.set(nodes.add_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __isub__(self, other): self.set(nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __imul__(self, other): self.set(nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __itruediv__(self, other): self.set(nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result); return self

    def __add__(self, other): return nodes.add_node(a=self.value, b=self._cast_to_float(other)).result
    def __radd__(self, other): return nodes.add_node(a=self._cast_to_float(other), b=self.value).result
    def __sub__(self, other): return nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result
    def __rsub__(self, other): return nodes.subtract_node(a=self._cast_to_float(other), b=self.value).result
    def __mul__(self, other): return nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result
    def __rmul__(self, other): return nodes.multiply_node(a=self._cast_to_float(other), b=self.value).result
    def __truediv__(self, other): return nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result
    def __rtruediv__(self, other): return nodes.divide_node(a=self._cast_to_float(other), b=self.value).result

    def __eq__(self, other): return self.value == self._cast_to_float(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_float(other) #type: ignore
    def __gt__(self, other): return self.value > self._cast_to_float(other)
    def __lt__(self, other): return self.value < self._cast_to_float(other)
    def __ge__(self, other): return self.value >= self._cast_to_float(other)
    def __le__(self, other): return self.value <= self._cast_to_float(other)

class BoolVar:
    """Use to create a Variable Bool Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=False, node_ref=None, name: str = "布尔值"):
        self._nodes_by_scope = {}
        
        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = bool(start_val) if isinstance(start_val, bool) else False
            self._node = nodes.bool_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node
            
            if not isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_bool_variable_value(
                    variable=self.variable, 
                    value=self._cast_to_bool(start_val)
                )
                ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self):
        scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if self._asset_dict:
                new_node = nodes.bool_variable(asset_dict=self._asset_dict)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self): return False
    def _get_primary_port(self): return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_bool_variable_value(variable=self.variable).value

    def set(self, target_state):
        if target_state is self:
            return self
            
        casted_val = self._cast_to_bool(target_state)
        return nodes.set_bool_variable_value(variable=self.variable, value=casted_val)

    def _cast_to_bool(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "BoolVar": return val.value
        if cls_name in ["IntVar", "FloatVar"]:
            raise TypeError("❌ Type Error: Cannot perform implicit boolean logic on numeric Variables.")
            
        if isinstance(val, bool): return val
        if isinstance(val, (int, float)): return bool(val)
            
        if hasattr(val, 'node'):
            t = val.node.type 
            bool_nodes = [
                "BoolValueNode", "BoolVariableNode", "GetBoolVariableValueNode", 
                "ToggleNode", "CompareIntNode", "CompareFloatNode", 
                "CompareGameObjectNode", "ComparePlantTypeNode", "CompareZombieTypeNode",
                "AndNode", "OrNode", "NotNode"
            ]
            if t in bool_nodes: return val
            raise TypeError(f"❌ Type Error: The node output '{t}' is not a valid boolean.")
            
        return val

    def toggle(self):
        with If(self.value == True) as flow:
            self.set(False)
        with flow.Else:
            self.set(True)

    def to_string(self):
        """Converts the BoolVar to a string node output ('True' / 'False')."""
        from .nodes import branch_node, string_value
        
        # Use a branch node to output string literals based on state
        res_str = string_value(val="False").value
        b = branch_node(condition=self.value)
        
        # Wire 'True' string on true branch
        true_str = string_value(val="True").value
        return true_str if b else res_str
    
    def __iand__(self, other): 
        self.set(nodes.and_node(a=self.value, b=self._cast_to_bool(other)).output)
        return self

    def __ior__(self, other): 
        self.set(nodes.or_node(a=self.value, b=self._cast_to_bool(other)).output)
        return self

    def __and__(self, other): 
        return nodes.and_node(a=self.value, b=self._cast_to_bool(other)).output

    def __rand__(self, other): 
        return nodes.and_node(a=self._cast_to_bool(other), b=self.value).output

    def __or__(self, other): 
        return nodes.or_node(a=self.value, b=self._cast_to_bool(other)).output

    def __ror__(self, other): 
        return nodes.or_node(a=self._cast_to_bool(other), b=self.value).output

    def __invert__(self): 
        return nodes.not_node(inp=self.value).output

    def __eq__(self, other): #type: ignore
        return self.value == self._cast_to_bool(other)

    def __ne__(self, other): #type: ignore
        return self.value != self._cast_to_bool(other)
    
#endregion

class MultiSelectMenu:
    """Deferred UI Builder for Multiple Choice Menus."""
    def __init__(self, is_rerollable: bool = True, reroll_count: int = 3, is_skippable: bool = False, window_count: int = 3):
        self.refreshable = is_rerollable
        self.refreshCount = reroll_count
        self.cancelable = is_skippable
        self.windowCount = window_count
        self._options = {}
        self._option_id_counter = 0
        self._show_node_id = None
        self.Output = self._Outputs(self)

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def add_option(self, title: str, description: str, callback, plant_type: int | PlantType = 254, zombie_type: int | ZombieType = -1) -> str:
        if isinstance(plant_type, PlantType): plant_type = plant_type.value
        if isinstance(zombie_type, ZombieType): zombie_type = zombie_type.value
        
        if (plant_type != -1 and zombie_type != -1):
            print(f"Warning: Cannot pass both Zombie or Plant type to MultiSelectMenu.add_option()")
            plant_type = 254
            zombie_type = -1
        if (plant_type == -1 and zombie_type == -1):
            print(f"Warning: None Zombie or Plant type passed to MultiSelectMenu.add_option()")
            plant_type = 254
        
        opt_id = f"opt_{self._option_id_counter}"
        self._option_id_counter += 1
        self._options[opt_id] = {"title": title, "description": description, "callback": callback, "plant_type": plant_type, "zombie_type": zombie_type}
        return opt_id

    def show(self):
        current_list_node_id, current_list_port_name = None, None
        
        for opt_id, opt_data in self._options.items():
            node_id = ctx._generate_uuid()
            kwargs = {
                "class": "AddMultipleChoiceOptionNode", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp",
                "title": opt_data["title"], "description": opt_data["description"], "plantType": opt_data["plant_type"], "zombieType": opt_data["zombie_type"],
                "list_PortName": "选项列表", "title_PortName": "标题", "description_PortName": "描述",
                "plantType_PortName": "植物类型", "zombieType_PortName": "僵尸类型", "optionSelected_PortName": "选项被点击"
            }
            ctx.nodes.append({"id": node_id, "type": "AddMultipleChoiceOptionNode", "kwargs": kwargs})
            
            if current_list_node_id:
                ctx.add_connection(current_list_node_id, current_list_port_name, node_id, "选项列表") # type: ignore
            
            current_list_node_id, current_list_port_name = node_id, "选项列表"
            
            if opt_data["callback"]:
                prev_trigger = ctx.trigger_stack[-1]
                class OptionClickTrigger:
                    def __init__(self, n_id): self.id, self.out_trigger = n_id, "选项被点击"
                ctx.trigger_stack[-1] = OptionClickTrigger(node_id)
                opt_data["callback"]()
                ctx.trigger_stack[-1] = prev_trigger

        self._show_node_id = ctx._generate_uuid()
        show_kwargs = {
            "class": "ShowMultipleChoiceMenuNode", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp",
            "refreshable": self.refreshable, "refreshCount": self.refreshCount, "cancelable": self.cancelable, "windowCount": self.windowCount,
            "trigger_PortName": "触发", "options_PortName": "选项列表", "refreshable_PortName": "可刷新",
            "refreshCount_PortName": "刷新次数", "cancelable_PortName": "可取消", "windowCount_PortName": "窗口数量",
            "actionOnExit_PortName": "退出时触发", "actionOnRefresh_PortName": "刷新时触发"
        }
        ctx.nodes.append({"id": self._show_node_id, "type": "ShowMultipleChoiceMenuNode", "kwargs": show_kwargs})
        
        current_execution = ctx.trigger_stack[-1]
        ctx.add_connection(current_execution.id, current_execution.out_trigger, self._show_node_id, "触发")
        
        if current_list_node_id:
            ctx.add_connection(current_list_node_id, current_list_port_name, self._show_node_id, "选项列表") # type: ignore
            
        ctx.trigger_stack[-1] = nodes.wait_node(0.0)

    class _Outputs:
        def __init__(self, parent): self.parent = parent
        def on_exit(self): return ExecutionPath(self.parent._show_node_id, "退出时触发")
        def on_refresh(self): return ExecutionPath(self.parent._show_node_id, "刷新时触发")           

class ForEachPlant:
    """Safely loops through plants and acts as a direct proxy to the current Plant object."""
    def __init__(self, plant_list_port):
        from . import nodes

        # Unpack list wrappers if passed directly
        if hasattr(plant_list_port, "list_port"):
            plant_list_port = plant_list_port.list_port
        elif hasattr(plant_list_port, "value"):
            plant_list_port = plant_list_port.value

        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        self._plant_cache = None
        
    def __enter__(self):
        from .node_base import ExecutionPath
        from .core import ctx
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        from .core import ctx
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Returns an execution path context manager for post-loop logic."""
        from .node_base import ExecutionPath
        return ExecutionPath(self.node.id, "循环完成")
    
    @property
    def plant(self):
        """Returns the current iterated plant wrapped in a Plant helper object."""
        from .extensions import Plant
        if self._plant_cache is None:
            self._plant_cache = Plant(self.node.currentPlant)
        return self._plant_cache

    @property
    def index(self):
        """The index of the current iteration."""
        return self.node.currentIndex

    # ==========================================================
    # TRANSPARENT PROXY TO PLANT WRAPPER
    # ==========================================================
    def __getattr__(self, name):
        """Forwards all plant methods and properties (heal, damage, die, row, col, etc.) directly."""
        return getattr(self.plant, name)


class ForEachPlantType:
    """Safely loops through a list of Plant Types natively on the node canvas."""
    def __init__(self, type_list_port):
        from . import nodes

        # Unpack list wrappers if passed directly
        if hasattr(type_list_port, "list_port"):
            type_list_port = type_list_port.list_port
        elif hasattr(type_list_port, "value"):
            type_list_port = type_list_port.value

        self.node = nodes.for_each_plant_type(type_list=type_list_port)
        
    def __enter__(self):
        from .node_base import ExecutionPath
        from .core import ctx
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        from .core import ctx
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Returns an execution path context manager for post-loop logic."""
        from .node_base import ExecutionPath
        return ExecutionPath(self.node.id, "循环完成")

    @property
    def plant_type(self):
        """The plant type of the current iteration."""
        return self.node.currentPlantType

    # Aliases
    type = plant_type
    value = plant_type

    @property
    def index(self):
        """The index of the current iteration."""
        return self.node.currentIndex

    # ==========================================================
    # DIRECT PORT & OPERATOR FORWARDING
    # ==========================================================
    def _get_primary_port(self):
        return self.plant_type

    def __eq__(self, other):
        return self.plant_type == other

    def __ne__(self, other):
        return self.plant_type != other

class PlantTypeList:
    """
    A smart wrapper representing a dynamic or static list of Plant Types on the node canvas.
    """
    def __init__(self, initial: Optional[Any] = None, initialize_empty: bool = True):
        from . import nodes
        from .node_base import PortReference

        self._current_port = None
        self._count_port = None

        if initial is None:
            storage = nodes.plant_type_list_storage(op=0, init_empty=initialize_empty)
            self._current_port = storage.currentList
            self._count_port = storage.count

        elif isinstance(initial, (Enum, int)):
            val = initial.value if isinstance(initial, Enum) else int(initial)
            multi_node = nodes.multi_plant_type_list(plant_types=[val])
            self._current_port = multi_node.plantTypeList
            self._count_port = nodes.int_value(val=1).value

        # Guard: check list/set while strictly excluding PortReference (which is a tuple subclass)
        elif isinstance(initial, (list, tuple, set)) and not isinstance(initial, PortReference):
            items = list(initial)
            if len(items) == 0:
                storage = nodes.plant_type_list_storage(op=0, init_empty=initialize_empty)
                self._current_port = storage.currentList
                self._count_port = storage.count
            else:
                raw_types = [item.value if isinstance(item, Enum) else int(item) for item in items]
                multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
                self._current_port = multi_node.plantTypeList
                self._count_port = nodes.int_value(val=len(raw_types)).value

        elif isinstance(initial, PlantTypeList):
            self._current_port = initial.list_port
            self._count_port = initial.count
        elif isinstance(initial, PortReference) or hasattr(initial, "node"):
            self._current_port = initial
        else:
            self._current_port = initial

    @property
    def list_port(self):
        return self._current_port

    @property
    def count(self):
        if self._count_port is not None:
            return self._count_port
        return self._current_port

    def set(self, other: Union['PlantTypeList', Iterable, Enum, int, Any]):
        new_list = PlantTypeList(other)
        self._current_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type):
        """
        Uses ForEachPlantTypeNode to search MultiPlantTypeListNode, protected by
        conditional branches to ensure safe state reset and latching.
        """
        from . import nodes
        from .core import ctx
        from .node_base import PortReference, ExecutionPath

        # 1. Resolve target port reference safely
        raw_target = target_type.value if hasattr(target_type, "value") else target_type
        if isinstance(raw_target, int) and not isinstance(raw_target, PortReference):
            target_port = nodes.plant_type_value(val=raw_target).value
        elif hasattr(raw_target, "_get_primary_port"):
            target_port = raw_target._get_primary_port() #type: ignore
        elif hasattr(raw_target, "value"):
            target_port = raw_target.value #type: ignore
        else:
            target_port = raw_target

        # 2. State tracking toggle node
        match_toggle = nodes.toggle_node(initial_state=False)

        # 3. PRE-LOOP RESET: If toggle is currently True, trigger it once to reset to False
        reset_branch = nodes.branch_node(condition=match_toggle.state)
        ctx.add_connection(reset_branch.id, "真（触发）", match_toggle.id, "触发")

        loop = nodes.for_each_plant_type(type_list=self._current_port)
        ctx.add_connection(reset_branch.id, "假（停止）", loop.id, "触发")
        ctx.add_connection(reset_branch.id, "真（触发）", loop.id, "触发")

        # 4. INSIDE LOOP BODY: Compare Current Type == Target Plant Type
        curr_type = PortReference(loop, "当前类型")
        is_equal = nodes.compare_plant_type(a=curr_type, b=target_port).equal

        match_branch = nodes.branch_node(condition=is_equal)
        ctx.add_connection(loop.id, "循环体", match_branch.id, "触发")

        # 5. SAFE LATCH: When matched, only trigger Toggle if Toggle.State is False
        state_guard_branch = nodes.branch_node(condition=match_toggle.state)
        ctx.add_connection(match_branch.id, "真（触发）", state_guard_branch.id, "触发")
        ctx.add_connection(state_guard_branch.id, "假（停止）", match_toggle.id, "触发")

        # 6. Route subsequent execution from Loop's OnComplete trigger
        ctx.trigger_stack[-1] = ExecutionPath(loop.id, "循环完成")

        return match_toggle.state

    def contains(self, plant_type: Union[Enum, int, Iterable, Any]):
        from . import nodes
        from .node_base import PortReference

        if isinstance(plant_type, (list, set)) and not isinstance(plant_type, PortReference):
            items = list(plant_type)
            if not items:
                return nodes.bool_value(val=True).value

            result_wire = None
            for p in items:
                check_wire = self._contains_single(p)
                result_wire = check_wire if result_wire is None else (result_wire & check_wire)
            return result_wire

        return self._contains_single(plant_type)

    Contains = contains

    def __iadd__(self, other: Union['PlantTypeList', Enum, int, Iterable, Any]):
        from . import nodes
        from .node_base import PortReference

        if isinstance(other, (Enum, int)):
            val = other.value if isinstance(other, Enum) else int(other)
            single_node = nodes.single_plant_type_list(plant_type=val)
            merge_node = nodes.merge_plant_type_lists(list_a=self._current_port, list_b=single_node.plantTypeList)
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            raw_types = [item.value if isinstance(item, Enum) else int(item) for item in other]
            multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
            merge_node = nodes.merge_plant_type_lists(list_a=self._current_port, list_b=multi_node.plantTypeList)
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, PlantTypeList):
            merge_node = nodes.merge_plant_type_lists(list_a=self._current_port, list_b=other.list_port)
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif hasattr(other, 'list_port') or hasattr(other, 'node'):
            port = other.list_port if hasattr(other, 'list_port') else other #type: ignore
            merge_node = nodes.merge_plant_type_lists(list_a=self._current_port, list_b=port)
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count

        return self

    def __add__(self, other: Union['PlantTypeList', Enum, int, Iterable, Any]):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list += other
        return copy_list

    def __isub__(self, other: Union['PlantTypeList', Enum, int, Iterable, Any]):
        from . import nodes
        from .node_base import PortReference
        from .extensions import ForEachPlantType

        if isinstance(other, (Enum, int)):
            raw_val = other.value if isinstance(other, Enum) else int(other)
            rem_node = nodes.remove_plant_type(list_in=self._current_port, plant_type=raw_val)
            self._current_port = rem_node.resultList
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            for item in other:
                self.__isub__(item)
        elif isinstance(other, PlantTypeList):
            with ForEachPlantType(other.list_port) as loop:
                rem_node = nodes.remove_plant_type(list_in=self._current_port, plant_type=loop.plant_type)
                self._current_port = rem_node.resultList
        elif hasattr(other, 'node'):
            rem_node = nodes.remove_plant_type(list_in=self._current_port, plant_type=other)
            self._current_port = rem_node.resultList

        return self

    def __sub__(self, other: Union['PlantTypeList', Enum, int, Iterable, Any]):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list -= other
        return copy_list

    def __eq__(self, other: Union['PlantTypeList', Any]): #type: ignore
        from . import nodes
        if isinstance(other, PlantTypeList):
            return nodes.compare_int(a=self.count, b=other.count).equal
        return False

    def add(self, plant_type: Union[Enum, int, Any]):
        self += plant_type
        return self

    def remove(self, plant_type: Union[Enum, int, Any]):
        self -= plant_type
        return self

    def get_random(self):
        from . import nodes
        return nodes.get_random_plant_type(list_in=self._current_port).result

    def merge(self, other: Union['PlantTypeList', Any]):
        self += other
        return self

    def for_each(self):
        from .extensions import ForEachPlantType
        return ForEachPlantType(self._current_port)

class Plant:
    """A smart wrapper for a Plant pointer that exposes built-in actions and properties."""

    def __init__(self, plant_ref):
        if isinstance(plant_ref, Plant):
            self.ref = plant_ref.ref
        else:
            self.ref = plant_ref

        self._split_cache = None

    # INTERNAL TYPE CASTING HELPERS
    
    @staticmethod
    def _to_float_port(val):
        from . import nodes
        from .node_base import PortReference

        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return nodes.float_value(val=float(val)).value
        if hasattr(val, "_is_float_port") and not val._is_float_port():
            return nodes.int_to_float(int_val=val).float
        if hasattr(val, "value"):
            return val.value #type: ignore
        return val

    @staticmethod
    def _to_int_port(val):
        from . import nodes
        from .node_base import PortReference

        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return nodes.int_value(val=int(val)).value
        if hasattr(val, "_is_float_port") and val._is_float_port():
            return nodes.float_to_int(float_val=val).int
        if hasattr(val, "value"):
            return val.value #type: ignore
        return val

    @staticmethod
    def _to_bool_port(val):
        from . import nodes
        from .node_base import PortReference

        if isinstance(val, bool) and not isinstance(val, PortReference):
            return nodes.bool_value(val=val).value
        if hasattr(val, "value"):
            return val.value
        return val

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def die(self):
        """Instantly destroys the plant."""
        from . import nodes
        return nodes.die_plant(plant=self.ref)

    def damage(self, amount):
        """Damages the plant by a specified amount."""
        from . import nodes
        float_amount = self._to_float_port(amount)
        return nodes.damage_plant(plant=self.ref, damage=float_amount)

    def heal(self, amount):
        """Heals the plant by a specified amount (ensures float port)."""
        from . import nodes
        float_amount = self._to_float_port(amount)
        return nodes.heal_plant(plant=self.ref, heal_amount=float_amount)

    def add_shield(self, amount):
        """Adds shield to the plant (ensures float port)."""
        from . import nodes
        float_amount = self._to_float_port(amount)
        return nodes.give_plant_shield(plant=self.ref, shield=float_amount)

    def move(self, col, row, force=False):
        """Moves the plant to a new grid cell. `force` bypasses all in-game placement checks."""
        from . import nodes
        int_col = self._to_int_port(col)
        int_row = self._to_int_port(row)
        bool_force = self._to_bool_port(force)
        return nodes.move_plant(plant=self.ref, row=int_row, column=int_col, force=bool_force)

    def move_relative(self, col_diff, row_diff, force=False):
        """Moves the plant relative to its current grid position."""
        return self.move(col=self.col + col_diff, row=self.row + row_diff, force=force)

    def modify_attack(self, multiplier):
            """Modifies attack multiplier (ensures float port)."""
            from . import nodes
            float_multiplier = self._to_float_port(multiplier)
            return nodes.modify_plant_attack(plant=self.ref, multiplier=float_multiplier)
    
    def modify_health(self, multiplier):
        """Modifies health multiplier (ensures float port)."""
        from . import nodes
        float_multiplier = self._to_float_port(multiplier)
        return nodes.modify_plant_health(plant=self.ref, multiplier=float_multiplier)

    # Alias for consistency with Zombie wrapper
    set_health_multiplier = modify_health
    
    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via plant_split)
    # ==========================================================
    @property
    def split(self):
        if self._split_cache is None:
            from . import nodes
            self._split_cache = nodes.plant_split(plant=self.ref)
        return self._split_cache

    @property
    def plantType(self):
        return self.split.plantType

    @property
    def row(self):
        return self.split.row

    @property
    def col(self):
        return self.split.column

    @property
    def attributeCD(self):
        return self.split.attributeCountdown

class Zombie:
    """A smart wrapper for a Zombie pointer that exposes built-in actions and properties."""

    def __init__(self, zombie_ref):
        if isinstance(zombie_ref, Zombie):
            self.ref = zombie_ref.ref
        else:
            self.ref = zombie_ref

        self._split_cache = None

    # ==========================================================
    # INTERNAL TYPE CASTING HELPERS
    # ==========================================================
    @staticmethod
    def _to_float_port(val):
        from . import nodes
        from .node_base import PortReference

        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return nodes.float_value(val=float(val)).value
        if hasattr(val, "_is_float_port") and not val._is_float_port():
            return nodes.int_to_float(int_val=val).float
        if hasattr(val, "value"):
            return val.value #type: ignore
        return val

    @staticmethod
    def _to_int_port(val):
        from . import nodes
        from .node_base import PortReference

        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return nodes.int_value(val=int(val)).value
        if hasattr(val, "_is_float_port") and val._is_float_port():
            return nodes.float_to_int(float_val=val).int
        if hasattr(val, "value"):
            return val.value #type: ignore
        return val

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def damage(self, amount):
        """Damages the zombie by a specified amount."""
        from . import nodes
        float_amount = self._to_float_port(amount)
        return nodes.damage_zombie(zombie=self.ref, damage=float_amount)

    def set_health_multiplier(self, ratio):
        """Modifies zombie health multiplier (ensures float/Single input to avoid C# cast crashes)."""
        from . import nodes
        float_ratio = self._to_float_port(ratio)
        return nodes.modify_zombie_health(zombie=self.ref, ratio=float_ratio)

    def hypnotize(self):
        """Mind-controls/hypnotizes the zombie to fight for the player."""
        from . import nodes
        return nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row, col):
        """Moves the zombie to a specific grid row and column."""
        from . import nodes
        int_row = self._to_int_port(row)
        int_col = self._to_int_port(col)
        return nodes.move_zombie(zombie=self.ref, row=int_row, column=int_col)

    def move_relative(self, row_diff=0, col_diff=0):
        """Moves the zombie relative to its current position."""
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    def play_animation(self, anim_name: Union[str, Enum, Any] = "idle"):
        """Plays a named animation clip on the zombie."""
        from . import nodes
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        return nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)

    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via zombie_split)
    # ==========================================================
    @property
    def split(self):
        if self._split_cache is None:
            from . import nodes
            self._split_cache = nodes.zombie_split(zombie=self.ref)
        return self._split_cache

    @property
    def zombieType(self):
        return self.split.zombieType

    @property
    def row(self):
        return self.split.row

    @property
    def col(self):
        return self.split.column
    
class While:
    """
    A continuous execution loop that runs as long as a condition port evaluates to True.
    
    Usage:
        with pvn.While(sun_boost < 500):
            sun_boost += 10
    """
    def __init__(self, condition):
        self.branch = nodes.branch_node(condition=condition)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.branch.id, "真（触发）"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.add_connection(self.branch.id, "真（触发）", self.branch.id, "触发")
        ctx.trigger_stack.pop()

class For:
    """
    A fixed-count loop structure that runs an execution block a specified number of times.
    Exposes the current loop index port dynamically.
    
    Usage:
        with pvn.For(5) as loop:
            pvn.Zombie.spawn(row=loop.index, column=10, zombie_type=0)
    """
    def __init__(self, count):
        self.loop_node = nodes.for_loop_node(count=count)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, "循环体"))
        return self

    @property
    def index(self):
        """Allows access to the loop index tracking output port directly inside scripts."""
        return (self.loop_node, "当前索引")

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()
      
class _Time:
    
    class OnFixedUpdate:
        """
        High-frequency/timed event loop driven natively by ToggleCycleNode.
        Runs 10 times a second by default.
        Features a lazy-loaded frame tracker.
        
        ### Usage:
            with pvn.Time.OnFixedUpdate(interval=0.1) as update:
                pvn.Board.Sun += 1
                with pvn.If(update.tick == 100):
                    pvn.show_message("100 ticks have passed!")
        """
        def __init__(self, interval:float | Any=0.1):
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            
            self.ref = nodes.toggle_cycle_node(interval=interval)
            
            ctx.trigger_stack.extend(saved_stack)
            
            if ctx.trigger_stack:
                previous_exec = ctx.trigger_stack[-1]
                ctx.add_connection(previous_exec.id, previous_exec.out_trigger, self.ref.id, "触发")
                
            self._counter = None 

        def __enter__(self):
            """Defaults straight into the repeating execution track loop body."""
            ctx.trigger_stack.append(ExecutionPath(self.ref.id, "周期事件"))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

        def toggle(self):
            if ctx.trigger_stack:
                current_exec = ctx.trigger_stack[-1]
                ctx.add_connection(current_exec.id, current_exec.out_trigger, self.ref.id, "触发")
                ctx.trigger_stack[-1] = ExecutionPath(self.ref.id, "切换开始时")
            return self
        
        @property
        def tick(self):
            """
            Lazy getter. Spawns and wires an active CounterNode tracking the loop 
            the very first time this property is read in a level script.
            """
            if self._counter is None:
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                
                self._counter = nodes.counter_node(start_val=0, reset=None)
                
                ctx.add_connection(self.ref.id, "周期事件", self._counter.id, "触发")
                
                ctx.trigger_stack.extend(saved_stack)
                
            return self._counter.count

        @property
        def on_cycle(self):
            """Explicit access to the repeating loop execution track."""
            return ExecutionPath(self.ref.id, "周期事件")

        @property
        def on_enable(self):
            """Timeline track fired the exact instant the loop engine activates."""
            return ExecutionPath(self.ref.id, "切换开始时")

        @property
        def on_disable(self):
            """Timeline track fired when the loop engine is turned off."""
            return ExecutionPath(self.ref.id, "切换关闭时")

    class Wait:
        """A clean Syntactic Sugar context manager to pause execution timelines."""
        def __init__(self, duration):
            self.node = nodes.wait_node(duration=duration)
            
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

    def __init__(self):
        self._global_time_var = None
    
    @property
    def time_since_start(self):
        """
        Returns the time in seconds since the level started.
        """
        if self._global_time_var is None:
            # 1. Preserve active compiler context stack
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            
            # 2. Instantiate global float tracking register
            self._global_time_var = FloatVar(start_val=0.0)
            
            # 3. Clean background loop driven by high-level trigger context managers
            with api.Trigger.OnBoardStart():
                with self.OnFixedUpdate(interval=0.1):
                    self._global_time_var += 0.1
            
            # 4. Restore the user's active compilation stack
            ctx.trigger_stack.extend(saved_stack)
            
        return self._global_time_var.value
    
    @property
    def time_since_game_start(self):
        """
        Returns the time in seconds since the game started.
        """
        if self._global_time_var is None:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            
            self._global_time_var = FloatVar(start_val=0.0)
            
            with api.Trigger.OnGameStart():
                with self.OnFixedUpdate(interval=0.1):
                    self._global_time_var += 0.1
            
            ctx.trigger_stack.extend(saved_stack)
            
        return self._global_time_var.value

Time = _Time()
    
class Mouse:
    def __init__(self, mouse_ref = None): 
        if mouse_ref is None: mouse_ref = nodes.on_mouse_click()
        self.node = mouse_ref
    @property
    def col(self):
        return self.node.column
    @property
    def row(self):
        return self.node.row
    @property
    def theItemType(self):
        return self.node.item
    @property
    def isLeftClick(self):
        return self.node.isLeftButton


