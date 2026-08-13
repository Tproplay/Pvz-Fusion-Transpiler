from . import nodes, api
from .core import ctx
from .node_base import ExecutionPath, BaseNode
from enum import Enum
from .TypeMgr import PlantType, ZombieAnimation
from typing import Any, Final


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
            bool_nodes = ["BoolVariableNode", "GetBoolVariableValueNode", "ToggleNode", "CompareIntNode", "CompareFloatNode", "CompareGameObjectNode", "AndNode", "OrNode", "NotNode"]
            if t in bool_nodes: return val
            raise TypeError(f"❌ Type Error: The node output '{t}' is not a valid boolean.")
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to BoolVar.")

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
    
    def __iand__(self, other): self.set(nodes.and_node(a=self.value, b=self._cast_to_bool(other)).Output); return self #type: ignore
    def __ior__(self, other): self.set(nodes.or_node(a=self.value, b=self._cast_to_bool(other)).Output); return self #type: ignore

    def __and__(self, other): return nodes.and_node(a=self.value, b=self._cast_to_bool(other)).Output
    def __rand__(self, other): return nodes.and_node(a=self._cast_to_bool(other), b=self.value).Output
    def __or__(self, other): return nodes.or_node(a=self.value, b=self._cast_to_bool(other)).Output
    def __ror__(self, other): return nodes.or_node(a=self._cast_to_bool(other), b=self.value).Output
    def __invert__(self): return nodes.not_node(inp=self.value).Output

    def __eq__(self, other): return self.value == self._cast_to_bool(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_bool(other) #type: ignore
    
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

    def add_option(self, title: str, description: str, callback, plant_type: int = 254, zombie_type: int = -1) -> str:
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
    """Safely loops through plants and yields a Plant Object."""
    def __init__(self, plant_list_port):
        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Returns a clean context manager for the post-loop timeline track."""
        return ExecutionPath(self.node.id, "循环完成")
    
    @property
    def plant(self):
        """Returns the current iterated plant wrapped in a Smart Object."""
        return Plant(self.node.currentPlant)

    @property
    def index(self):
        return self.node.currentIndex
 
class ForEachPlantType:
    """Safely loops through a list of Plant Types natively."""
    def __init__(self, type_list_port):
        self.node = nodes.for_each_plant_type(type_list=type_list_port)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self.node
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

class Plant:
    """A smart wrapper for a Plant pointer that exposes built-in actions."""
    def __init__(self, plant_ref):
        if isinstance(plant_ref, Plant): plant_ref = plant_ref.ref
        else: self.ref = plant_ref
        
        self.split = nodes.plant_split(plant=self.ref)
        

    def die(self):
        """Instantly destroys the plant."""
        nodes.die_plant(plant=self.ref)

    def damage(self, amount):
        nodes.damage_plant(plant=self.ref, damage=amount)

    def heal(self, amount):
        nodes.heal_plant(plant=self.ref, heal_amount=amount)

    def add_shield(self, amount):
        nodes.give_plant_shield(plant=self.ref, shield=amount)

    def move(self, col, row, force=False):
        """force bypasses all ingame checks."""
        nodes.move_plant(plant=self.ref, row=row, column=col, force=force)
        
    def move_relative(self, col_diff, row_diff, force=False):
        """force bypasses all ingame checks."""
        nodes.move_plant(plant=self.ref, row=self.row + row_diff, column=self.col + col_diff, force=force)

    # Automatically unrolls the plant_split node to fetch properties!
    @property
    def plantType(self): return self.split.plantType
    
    @property
    def row(self): return self.split.row
    
    @property
    def col(self): return self.split.column
    
    @property
    def attributeCD(self): return self.split.attributeCountdown

class Zombie:
    """A smart wrapper for a Zombie pointer that exposes built-in actions."""
    def __init__(self, zombie_ref):
        if isinstance(zombie_ref, Zombie): zombie_ref = zombie_ref.ref
        else: self.ref = zombie_ref

    def damage(self, amount):
        nodes.damage_zombie(zombie=self.ref, damage=amount)

    def set_health_multiplier(self, ratio):
        nodes.modify_zombie_health(zombie=self.ref, ratio=ratio)

    def hypnotize(self):
        nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row, col):
        nodes.move_zombie(zombie=self.ref, row=row, column=col)

    def play_animation(self, anim_name : str | ZombieAnimation | Any= "idle"): # type: ignore
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)
    
    @property
    def zombieType(self): return nodes.zombie_split(zombie=self.ref).zombieType
    
    @property
    def row(self): return nodes.zombie_split(zombie=self.ref).row
    
    @property
    def col(self): return nodes.zombie_split(zombie=self.ref).column
    
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


