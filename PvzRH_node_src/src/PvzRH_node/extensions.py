from . import nodes, api
from .core import ctx
from .node_base import ExecutionPath, BaseNode
from enum import Enum
from .TypeMgr import PlantType, ZombieAnimation
from typing import Any, Final
import math

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
    
class Mathf:
    """Commonly used math functions"""
    
    PI : Final[float] = 3.141592653589793
    """The mathematical constant π, representing the ratio of a circle's circumference to its diameter."""
    HALF_PI : Final[float] = 1.570796326794896
    """Half value of PI."""
    E : Final[float] = 2.718281828459045
    """The mathematical constant e, representing the base of the natural logarithm."""
    TAU : Final[float] = 6.283018867E-17
    """The mathematical constant τ, representing the ratio of a circle's circumference to its radius (τ = 2π)."""
    
    @staticmethod
    def abs(val):
        """
        Returns the absolute value of an integer or float wire configuration.
        Calculates natively via: result = (val < 0) ? (val * -1) : val
        """
        from . import nodes
        from .node_base import PortReference
        
        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return abs(val)

        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        is_negative = val < 0 
        branch = nodes.branch_node(condition=is_negative)

        is_float = hasattr(val, "_is_float_port") and val._is_float_port()
        
        if is_float:
            result_reg = nodes.float_variable(var_name="abs_temp_f")
            set_true = nodes.set_float_variable_value(variable=result_reg.variable, value=val * -1)
            set_false = nodes.set_float_variable_value(variable=result_reg.variable, value=val)
            final_port = nodes.get_float_variable_value(variable=result_reg.variable).value
        else:
            result_reg = nodes.int_variable(var_name="abs_temp_i")
            set_true = nodes.set_int_variable_value(variable=result_reg.variable, value=val * -1)
            set_false = nodes.set_int_variable_value(variable=result_reg.variable, value=val)
            final_port = nodes.get_int_variable_value(variable=result_reg.variable).value

        ctx.add_connection(branch.id, "真（触发）", set_true.id, "触发")
        ctx.add_connection(branch.id, "假（停止）", set_false.id, "触发")

        ctx.trigger_stack.extend(saved_stack)

        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            
            # Replace stack pointer with a merged path wrapper or wire next node to both
            ctx.trigger_stack[-1] = ExecutionPath(set_true.id, "完成")
            ctx.add_connection(set_false.id, "完成", set_true.id, "完成") # Converge False into True completion

        return final_port
    @staticmethod
    def max(*args):
        """
        Returns the largest of a variable number of arguments or a sequence loop.
        Usage: 
            Mathf.max(val1, val2, val3) or Mathf.max([val1, val2, val3])
        """
        from .node_base import PortReference
        
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args = args[0]
            
        if not args:
            raise ValueError("Mathf.max() requires at least one argument.")
            
        if all(isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args):
            return max(args)

        res = args[0]
        for next_val in args[1:]:
            res = Mathf._binary_max(res, next_val)
        return res

    @staticmethod
    def _binary_max(a, b):
        """Internal helper to compare exactly two values inside the node graph."""
        from . import nodes
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        branch = nodes.branch_node(condition=(a > b))
        
        is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (hasattr(b, "_is_float_port") and b._is_float_port())
        if is_float:
            reg = nodes.float_variable(var_name="max_temp_f")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_float_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_float_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_float_variable_value(variable=reg.variable).value
        else:
            reg = nodes.int_variable(var_name="max_temp_i")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_int_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_int_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_int_variable_value(variable=reg.variable).value

        ctx.trigger_stack.extend(saved_stack)
        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

        return final_port

    @staticmethod
    def min(*args):
        """
        Returns the smallest of a variable number of arguments or a sequence loop.
        Usage: 
            Mathf.min(val1, val2, val3) or Mathf.min([val1, val2, val3])
        """
        from .node_base import PortReference
        
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args = args[0]
            
        if not args:
            raise ValueError("Mathf.min() requires at least one argument.")
            
        if all(isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args):
            return min(args)

        res = args[0]
        for next_val in args[1:]:
            res = Mathf._binary_min(res, next_val)
        return res

    @staticmethod
    def _binary_min(a, b):
        """Internal helper to compare exactly two values inside the node graph."""
        from . import nodes
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        branch = nodes.branch_node(condition=(a < b))
        
        is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (hasattr(b, "_is_float_port") and b._is_float_port())
        if is_float:
            reg = nodes.float_variable(var_name="min_temp_f")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_float_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_float_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_float_variable_value(variable=reg.variable).value
        else:
            reg = nodes.int_variable(var_name="min_temp_i")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_int_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_int_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_int_variable_value(variable=reg.variable).value

        ctx.trigger_stack.extend(saved_stack)
        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

        return final_port

    @staticmethod
    def clamp(value, min_value, max_value):
        return Mathf.max(min_value, Mathf.min(value, max_value))

    @staticmethod
    def floor(value):
        from . import nodes
        if isinstance(value, (int, float)):
            return int(value)
        return nodes.float_to_int(float_val=value).int

    @staticmethod
    def ceil(value):
        from . import nodes
        if isinstance(value, (int, float)):
            return int(-(-value // 1))  # Ceiling for numeric types
        return nodes.float_to_int(float_val=value).int + 1  # Ceiling for node references
    
    @staticmethod
    def clamp01(value):
        """Clamps a value between 0 and 1."""
        return Mathf.clamp(value, 0.0, 1.0)
    
    @staticmethod
    def lerp(start, end, t):
        """Linearly interpolates between start and end by t (0 <= t <= 1)."""
        return start + (end - start) * Mathf.clamp01(t)
    
    @staticmethod
    def lerp_unclamped(start, end, t):
        """Linearly interpolates between start and end by t without clamping."""
        return start + (end - start) * t
    
    @staticmethod
    def sign(value):
        """Returns 1 if value is positive, -1 if negative, and 0 if zero."""
        from . import nodes
        if isinstance(value, (int, float)):
            return (value > 0) - (value < 0)
        
        with If(value > 0) as branch:
            return 1
        with branch.Elif(value < 0):
            return -1
        with branch.Else:
            return 0

    @staticmethod
    def round(value):
        """Rounds a value to the nearest integer."""
        from . import nodes
        if isinstance(value, (int, float)):
            return round(value)
        
        # For node references, we can use a combination of floor and ceil
        with If(value - Mathf.floor(value) < 0.5) as branch:
            return Mathf.floor(value)
        with branch.Else:
            return Mathf.ceil(value)
    
    @staticmethod
    def copy_sign(magnitude, sign):
        """Returns a value with the magnitude of 'magnitude' and the sign of 'sign'."""
        return Mathf.sign(sign) * abs(magnitude)

    @staticmethod
    def _ensure_float_port(val):
        """Helper to safely promote integers or integer node ports to float ports."""
        from . import nodes
        from .node_base import PortReference

        raw_val = val.value if hasattr(val, "value") else val

        if isinstance(raw_val, int) and not isinstance(raw_val, bool):
            return float(raw_val)
            
        if isinstance(raw_val, float):
            return raw_val

        # Check if input is an integer port or IntVar
        is_int_port = False
        if hasattr(val, '_is_float_port') and not val._is_float_port():
            is_int_port = True
        elif hasattr(raw_val, 'node'):
            int_nodes = [
                "IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", 
                "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", 
                "IntDivideNode", "IntModuloNode", "CounterNode"
            ]
            if raw_val.node.type in int_nodes: #type: ignore
                is_int_port = True

        if is_int_port:
            return nodes.int_to_float(int_val=raw_val).float

        return raw_val

    @staticmethod
    def sqrt(val, precision: int = 6):
        """
        Calculates the square root of val using Newton-Raphson iteration.
        - precision: Number of iterative refinement steps (default 6).
        """
        import math
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        is_static = isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference)

        # 1. Static Python Evaluation
        if is_static:
            if raw_val < 0:
                raise ValueError(f"❌ Error: Cannot calculate square root of negative number '{raw_val}'.")
            return math.sqrt(raw_val) #type: ignore

        # 2. Dynamic Node Graph Calculation
        guess = raw_val
        for _ in range(precision):
            div = nodes.divide_node(a=raw_val, b=guess).result
            add = nodes.add_node(a=guess, b=div).result
            guess = nodes.multiply_node(a=add, b=0.5).result

        return guess

    @staticmethod
    def cbrt(val, precision: int = 6):
        """
        Calculates the cube root of val using Newton-Raphson iteration.
        - precision: Number of iterative refinement steps (default 6).
        """
        import math
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        is_static = isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference)

        # 1. Static Python Evaluation
        if is_static:
            return math.cbrt(raw_val) if hasattr(math, "cbrt") else (raw_val ** (1/3) if raw_val >= 0 else -(-raw_val) ** (1/3)) #type: ignore

        # 2. Dynamic Node Graph Calculation
        guess = raw_val
        for _ in range(precision):
            guess_sq = nodes.multiply_node(a=guess, b=guess).result
            div = nodes.divide_node(a=raw_val, b=guess_sq).result
            two_guess = nodes.multiply_node(a=guess, b=2.0).result
            sum_val = nodes.add_node(a=two_guess, b=div).result
            guess = nodes.divide_node(a=sum_val, b=3.0).result

        return guess
    
    @staticmethod
    def natural_pow(base, exp):
        """
        Calculates base raised to a natural number exponent (exp >= 1).
        - Static exponents: Throws ValueError if non-natural (negative or decimal).
        - Dynamic exponents: Auto-casts float ports to int; evaluates to 0.0 if exp < 1 at runtime.
        """
        import math
        from . import nodes
        from .extensions import FloatVar, If
        from .node_base import PortReference, ExecutionPath

        raw_base = base.value if hasattr(base, "value") else base
        raw_exp = exp.value if hasattr(exp, "value") else exp

        is_base_static = isinstance(raw_base, (int, float)) and not isinstance(raw_base, PortReference)
        is_exp_static = isinstance(raw_exp, (int, float)) and not isinstance(raw_exp, PortReference)

        # --- STATIC EXPONENT HANDLING ---
        if is_exp_static:
            if isinstance(raw_exp, float) and not raw_exp.is_integer():
                raise ValueError(f"❌ Error: natural_pow requires a natural number exponent, got float '{raw_exp}'.")
            
            exp_int = int(raw_exp)
            if exp_int < 1:
                raise ValueError(f"❌ Error: natural_pow exponent must be >= 1, got '{exp_int}'.")

            if is_base_static:
                return float(raw_base ** exp_int)

            # Unroll multiplication chain on node canvas
            curr_res = raw_base
            for _ in range(exp_int - 1):
                curr_res = nodes.multiply_node(a=curr_res, b=raw_base).result
            return curr_res

        # --- DYNAMIC EXPONENT HANDLING ---
        # 1. Cast float port to int port if necessary
        if hasattr(raw_exp, '_is_float_port') and raw_exp._is_float_port(): #type: ignore
            exp_int_port = nodes.float_to_int(float_val=raw_exp).int
        else:
            exp_int_port = raw_exp

        # 2. Construct runtime condition (exp >= 1 -> base^exp, else -> 0.0)
        result_var = FloatVar(start_val=0.0, name="nat_pow_res")

        with If(exp_int_port >= 1):
            result_var.set(1.0)
            loop_node = nodes.for_loop_node(count=exp_int_port)
            
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.append(ExecutionPath(loop_node.id, "循环体"))
            result_var *= raw_base
            ctx.trigger_stack.pop()

        return result_var.value

    @staticmethod
    def _ensure_int_port(val):
        """Helper to safely promote floats or float node ports to integer ports."""
        from . import nodes
        from .node_base import PortReference

        raw_val = val.value if hasattr(val, "value") else val

        if isinstance(raw_val, float):
            return int(raw_val)
            
        if isinstance(raw_val, int):
            return raw_val

        # Check if input is a float port or FloatVar
        is_float_port = False
        if hasattr(val, '_is_float_port') and val._is_float_port():
            is_float_port = True
        elif hasattr(raw_val, 'node'):
            float_nodes = [
                "FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", 
                "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"
            ]
            if raw_val.node.type in float_nodes:
                is_float_port = True

        if is_float_port:
            return nodes.float_to_int(float_val=raw_val).int

        return raw_val

    @staticmethod
    def is_prime(val):
        """
        Checks if a number is a prime number. 
        Evaluates statically if constant, or builds an optimized O(sqrt(N)) runtime loop on the node canvas.
        """
        import math
        import uuid
        from . import nodes
        from .extensions import BoolVar, IntVar, If
        from .node_base import PortReference
        from .core import ctx

        raw_val = Mathf._ensure_int_port(val)
        is_static = isinstance(raw_val, int) and not isinstance(raw_val, PortReference)

        # 1. Static Python Evaluation (Compile-time)
        if is_static:
            if raw_val <= 1:
                return False
            for i in range(2, int(math.isqrt(raw_val)) + 1): #type: ignore
                if raw_val % i == 0:
                    return False
            return True

        # 2. Dynamic Node Graph Calculation (Runtime)
        uid = uuid.uuid4().hex[:6]
        result_var = BoolVar(start_val=True, name=f"is_prime_res_{uid}")
        val_var = IntVar(start_val=0, name=f"prime_val_{uid}")
        val_var.set(raw_val)

        # Edge case: N <= 1 is not prime
        with If(val_var <= 1):
            result_var.set(False)

        # Main check: N > 1
        with If(val_var > 1):
            # Calculate sqrt(N) to constrain loop iterations
            sqrt_float = Mathf.sqrt(val_var, precision=5)
            sqrt_int = nodes.float_to_int(float_val=sqrt_float).int
            
            loop_count = nodes.int_subtract(a=sqrt_int, b=1).result
            loop_node = nodes.for_loop_node(count=loop_count)

            class _LoopScope:
                def __init__(self, node_id, port):
                    self.id = node_id
                    self.out_trigger = port

            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.append(_LoopScope(loop_node.id, "循环体"))

            current_index = PortReference(loop_node, "当前索引")
            divisor = nodes.int_add(a=current_index, b=2).result
            
            # Direct dataflow comparison: N % divisor == 0 (No intermediate IntVar)
            mod_res = nodes.int_modulo(a=val_var.value, b=divisor).result
            
            with If(mod_res == 0):
                result_var.set(False)

            # Restore parent execution stack
            ctx.trigger_stack.clear()
            ctx.trigger_stack.extend(saved_stack)

        return result_var.value
    
    @staticmethod
    def perlin_noise(x, y=0.0):
        """
        Calculates 1D or 2D Smooth Perlin/Value Noise in the range [0.0, 1.0].
        - Static inputs: Evaluates procedurally at compile time in Python.
        - Dynamic inputs: Constructs a node graph with bilinear interpolation and smoothstep curves.
        """
        import math
        from . import nodes
        from .node_base import PortReference

        raw_x = Mathf._ensure_float_port(x)
        raw_y = Mathf._ensure_float_port(y)

        is_x_static = isinstance(raw_x, (int, float)) and not isinstance(raw_x, PortReference)
        is_y_static = isinstance(raw_y, (int, float)) and not isinstance(raw_y, PortReference)

        # Helper: Deterministic Hash for Static Python Evaluation
        def _static_hash(ix: int, iy: int) -> float:
            h = (ix * 374761393 + iy * 668265263) % 1000003
            h = (h * 1274126177) % 1000003
            return float(h) / 1000003.0

        # Helper: Smoothstep Fade Curve f(t) = 3t^2 - 2t^3
        def _fade(t):
            return t * t * (3.0 - 2.0 * t)

        # ==========================================================
        # 1. STATIC PYTHON EVALUATION (Compile-Time)
        # ==========================================================
        if is_x_static and is_y_static:
            x_val, y_val = float(raw_x), float(raw_y) #type: ignore

            x0, y0 = math.floor(x_val), math.floor(y_val)
            x1, y1 = x0 + 1, y0 + 1

            tx, ty = x_val - x0, y_val - y0
            sx, sy = _fade(tx), _fade(ty)

            v00 = _static_hash(x0, y0)
            v10 = _static_hash(x1, y0)
            v01 = _static_hash(x0, y1)
            v11 = _static_hash(x1, y1)

            # Bilinear Interpolation
            l0 = v00 + sx * (v10 - v00)
            l1 = v01 + sx * (v11 - v01)
            return l0 + sy * (l1 - l0)

        # ==========================================================
        # 2. DYNAMIC NODE GRAPH CALCULATION (Runtime)
        # ==========================================================
        def _node_hash(i_port, j_port):
            """Generates a deterministic pseudo-random float [0, 1] on the node graph."""
            h1 = nodes.int_modulo(
                a=nodes.int_add(
                    a=nodes.int_multiply(a=i_port, b=374761393).result,
                    b=nodes.int_multiply(a=j_port, b=668265263).result
                ).result,
                b=1000003
            ).result

            h2 = nodes.int_modulo(
                a=nodes.int_multiply(a=h1, b=1274126177).result,
                b=1000003
            ).result

            f_hash = nodes.int_to_float(int_val=h2).float
            return nodes.divide_node(a=f_hash, b=1000003.0).result

        # Floor inputs to get cell integer coordinates
        x_int = nodes.float_to_int(float_val=raw_x).int
        y_int = nodes.float_to_int(float_val=raw_y).int

        x0_float = nodes.int_to_float(int_val=x_int).float
        y0_float = nodes.int_to_float(int_val=y_int).float

        x1_int = nodes.int_add(a=x_int, b=1).result
        y1_int = nodes.int_add(a=y_int, b=1).result

        # Fractional distance inside cell
        tx = nodes.subtract_node(a=raw_x, b=x0_float).result
        ty = nodes.subtract_node(a=raw_y, b=y0_float).result

        # Smoothstep curve sx = tx * tx * (3.0 - 2.0 * tx)
        tx_sq = nodes.multiply_node(a=tx, b=tx).result
        two_tx = nodes.multiply_node(a=tx, b=2.0).result
        three_sub_tx = nodes.subtract_node(a=3.0, b=two_tx).result
        sx = nodes.multiply_node(a=tx_sq, b=three_sub_tx).result

        ty_sq = nodes.multiply_node(a=ty, b=ty).result
        two_ty = nodes.multiply_node(a=ty, b=2.0).result
        three_sub_ty = nodes.subtract_node(a=3.0, b=two_ty).result
        sy = nodes.multiply_node(a=ty_sq, b=three_sub_ty).result

        # Sample cell corners
        v00 = _node_hash(x_int, y_int)
        v10 = _node_hash(x1_int, y_int)
        v01 = _node_hash(x_int, y1_int)
        v11 = _node_hash(x1_int, y1_int)

        # Bilinear Interpolation Nodes
        # l0 = v00 + sx * (v10 - v00)
        diff0 = nodes.subtract_node(a=v10, b=v00).result
        mult0 = nodes.multiply_node(a=sx, b=diff0).result
        l0 = nodes.add_node(a=v00, b=mult0).result

        # l1 = v01 + sx * (v11 - v01)
        diff1 = nodes.subtract_node(a=v11, b=v01).result
        mult1 = nodes.multiply_node(a=sx, b=diff1).result
        l1 = nodes.add_node(a=v01, b=mult1).result

        # result = l0 + sy * (l1 - l0)
        diff_final = nodes.subtract_node(a=l1, b=l0).result
        mult_final = nodes.multiply_node(a=sy, b=diff_final).result
        
        return nodes.add_node(a=l0, b=mult_final).result

    #region Trignometry
    
    RAD2DEG = 57.29577951308232   # 180.0 / PI
    DEG2RAD = 0.017453292519943295 # PI / 180.0
    TWO_PI = 6.283185307179586   # 2 * PI
    
    @staticmethod
    def rad2deg(rad):
        """Converts radians to degrees (rad * 180 / PI)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return raw_val * Mathf.RAD2DEG

        return nodes.multiply_node(a=raw_val, b=Mathf.RAD2DEG).result

    @staticmethod
    def deg2rad(deg):
        """Converts degrees to radians (deg * PI / 180)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(deg)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return raw_val * Mathf.DEG2RAD

        return nodes.multiply_node(a=raw_val, b=Mathf.DEG2RAD).result

    @staticmethod
    def normalize_angle_360(angle):
        """Wraps any angle in degrees to the range [0.0, 360.0)."""
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(angle)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return raw_val % 360.0

        return PortReference._float_modulo(raw_val, 360.0)

    @staticmethod
    def normalize_angle_180(angle):
        """
        Wraps any angle in degrees to the range [-180.0, 180.0).
        Calculates: ((angle + 180) % 360) - 180
        """
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(angle)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return ((raw_val + 180.0) % 360.0) - 180.0

        # Dynamic graph calculation
        add_180 = nodes.add_node(a=raw_val, b=180.0).result
        mod_360 = PortReference._float_modulo(add_180, 360.0)
        return nodes.subtract_node(a=mod_360, b=180.0).result

    @staticmethod
    def delta_angle(current, target):
        """Calculates the shortest difference between two angles in degrees [-180.0, 180.0]."""
        from .node_base import PortReference

        raw_curr = Mathf._ensure_float_port(current)
        raw_targ = Mathf._ensure_float_port(target)

        is_curr_static = isinstance(raw_curr, (int, float)) and not isinstance(raw_curr, PortReference)
        is_targ_static = isinstance(raw_targ, (int, float)) and not isinstance(raw_targ, PortReference)

        if is_curr_static and is_targ_static:
            return Mathf.normalize_angle_180(raw_targ - raw_curr)

        diff = raw_targ - raw_curr
        return Mathf.normalize_angle_180(diff)

    @staticmethod
    def lerp_angle(a, b, t):
        """Linearly interpolates between two angles (in degrees) taking the shortest path."""
        delta = Mathf.delta_angle(a, b)
        return a + (delta * t)
    
    @staticmethod
    def _wrap_rad(rad):
        """Wraps radians into the range [-PI, PI] for optimal Taylor series convergence."""
        import math
        from . import nodes
        from .node_base import PortReference

        if isinstance(rad, (int, float)) and not isinstance(rad, PortReference):
            return ((rad + math.pi) % (2 * math.pi)) - math.pi

        # Dynamic Graph: ((rad + PI) % TWO_PI) - PI
        add_pi = nodes.add_node(a=rad, b=Mathf.PI).result
        mod_2pi = PortReference._float_modulo(add_pi, Mathf.TWO_PI)
        return nodes.subtract_node(a=mod_2pi, b=Mathf.PI).result

    @staticmethod
    def sin(rad, terms: int = 5):
        """Calculates sine (in radians) with range reduction."""
        import math
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.sin(raw_val)

        # 1. Wrap angle into [-PI, PI]
        wrapped = Mathf._wrap_rad(raw_val)

        # 2. Compute Taylor Series: x - x^3/3! + x^5/5! - x^7/7! ...
        result = wrapped
        x_power = wrapped
        sign = -1.0

        for n in range(3, 3 + (terms - 1) * 2, 2):
            x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
            x_power = nodes.multiply_node(a=x_power, b=x_sq).result

            fact = float(math.factorial(n))
            term = nodes.divide_node(a=x_power, b=fact).result
            term_scaled = nodes.multiply_node(a=term, b=sign).result

            result = nodes.add_node(a=result, b=term_scaled).result
            sign *= -1.0

        return result

    @staticmethod
    def cos(rad, terms: int = 5):
        """Calculates cosine (in radians) with range reduction."""
        import math
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.cos(raw_val)

        # 1. Wrap angle into [-PI, PI]
        wrapped = Mathf._wrap_rad(raw_val)

        # 2. Compute Taylor Series: 1 - x^2/2! + x^4/4! - x^6/6! ...
        result = nodes.float_value(val=1.0).value
        x_power = nodes.float_value(val=1.0).value
        sign = -1.0

        for n in range(2, 2 + terms * 2, 2):
            x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
            x_power = nodes.multiply_node(a=x_power, b=x_sq).result

            fact = float(math.factorial(n))
            term = nodes.divide_node(a=x_power, b=fact).result
            term_scaled = nodes.multiply_node(a=term, b=sign).result

            result = nodes.add_node(a=result, b=term_scaled).result
            sign *= -1.0

        return result
    
    @staticmethod
    def tan(rad, terms: int = 5):
        """Calculates tangent (sin / cos)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.tan(raw_val)

        s = Mathf.sin(raw_val, terms=terms)
        c = Mathf.cos(raw_val, terms=terms)
        return nodes.divide_node(a=s, b=c).result

    @staticmethod
    def cosec(rad, terms: int = 5):
        """Calculates cosecant (1 / sin)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return 1.0 / math.sin(raw_val)

        s = Mathf.sin(raw_val, terms=terms)
        return nodes.divide_node(a=1.0, b=s).result

    @staticmethod
    def sec(rad, terms: int = 5):
        """Calculates secant (1 / cos)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return 1.0 / math.cos(raw_val)

        c = Mathf.cos(raw_val, terms=terms)
        return nodes.divide_node(a=1.0, b=c).result

    @staticmethod
    def cot(rad, terms: int = 5):
        """Calculates cotangent (cos / sin)."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(rad)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return 1.0 / math.tan(raw_val)

        s = Mathf.sin(raw_val, terms=terms)
        c = Mathf.cos(raw_val, terms=terms)
        return nodes.divide_node(a=c, b=s).result


    @staticmethod
    def asin(val, terms: int = 5):
        """Calculates arcsine in radians [-pi/2, pi/2]. Input domain [-1, 1]."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.asin(raw_val)

        # Dynamic Graph: Taylor Series x + (1/2)(x^3/3) + (3/8)(x^5/5) + (15/48)(x^7/7) + ...
        result = raw_val
        x_power = raw_val

        for n in range(1, terms):
            two_n = 2 * n
            x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
            x_power = nodes.multiply_node(a=x_power, b=x_sq).result

            # Coefficient: ( (2n)! ) / ( (4^n) * (n!)^2 * (2n + 1) )
            coeff = float(math.factorial(two_n)) / ((4.0 ** n) * (math.factorial(n) ** 2) * (two_n + 1))
            term = nodes.multiply_node(a=x_power, b=coeff).result
            result = nodes.add_node(a=result, b=term).result

        return result

    @staticmethod
    def acos(val, terms: int = 5):
        """Calculates arccostine in radians [0, pi]. (pi/2 - asin(val))"""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.acos(raw_val)

        asin_val = Mathf.asin(raw_val, terms=terms)
        return nodes.subtract_node(a=Mathf.HALF_PI, b=asin_val).result

    @staticmethod
    def atan(val, terms: int = 5):
        """Calculates arctangent in radians [-pi/2, pi/2]."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.atan(raw_val)

        # Transform atan(x) = asin(x / sqrt(1 + x^2)) for full range domain stability
        x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
        one_plus_x_sq = nodes.add_node(a=1.0, b=x_sq).result
        denom = Mathf.sqrt(one_plus_x_sq)
        ratio = nodes.divide_node(a=raw_val, b=denom).result

        return Mathf.asin(ratio, terms=terms)

    @staticmethod
    def acosec(val, terms: int = 5):
        """Calculates arccosecant in radians (asin(1 / val))."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.asin(1.0 / raw_val)

        reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
        return Mathf.asin(reciprocal,terms=terms)

    @staticmethod
    def asec(val, terms: int = 5):
        """Calculates arcsecant in radians (acos(1 / val))."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.acos(1.0 / raw_val)

        reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
        return Mathf.acos(reciprocal, terms=terms)

    @staticmethod
    def acot(val, terms: int = 5):
        """Calculates arccotangent in radians (pi/2 - atan(val))."""
        from . import nodes
        from .node_base import PortReference

        raw_val = Mathf._ensure_float_port(val)
        if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
            return math.atan(1.0 / raw_val)

        atan_val = Mathf.atan(raw_val, terms=terms)
        return nodes.subtract_node(a=Mathf.HALF_PI, b=atan_val).result
    
    #endregion
    
    
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


