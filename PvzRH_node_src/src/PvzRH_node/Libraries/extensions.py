from __future__ import annotations

from collections.abc import Callable, Iterable
from enum import Enum
from typing import Any, overload, Optional, Union

from typing_extensions import Self

from .. import api, nodes
from ..core import ctx
from ..Data.TypeMgr import PlantType, ZombieType
from ..node_base import ExecutionPath, PortReference
from ..nodes import (
    branch_node,
    divide_node,
    float_to_int,
    float_to_string,
    float_value,
    int_multiply,
    int_to_float,
    int_value,
    multiply_node,
    string_value,
)
from ..typing import _staticproperty, to_int_port, to_bool_port, to_float_port

__all__ = [
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "Option",
    "MultiSelectMenu",
    "ForEachPlant",
    "ForEachPlantType",
    "PlantTypeList",
    "Plant",
    "Zombie",
    "While",
    "For",
    "Time",
    "Mouse",
    "Random",
    "InfoCard",
    
]

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
        condition = self.switch.target == self.values[0]
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
                "触发",
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


# region Variables


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
            asset_init_val = (
                start_val
                if isinstance(start_val, int) and not isinstance(start_val, bool)
                else 0
            )
            self._node = nodes.int_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, int) or isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_int_variable_value(
                    variable=self.variable, value=self._cast_to_int(start_val)
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

    def _is_float_port(self):
        return False

    def _get_primary_port(self):
        return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_int_variable_value(variable=self.variable).value

    def set(self, value):

        node = nodes.set_int_variable_value(variable=self.variable, value=value)
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.id, "完成")
        return self

    def _cast_to_int(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "IntVar":
            return val.value
        if cls_name == "FloatVar":
            return nodes.float_to_int(float_val=val.value).int
        if cls_name == "BoolVar":
            raise TypeError(
                "❌ Type Error: Cannot implicitly cast a BoolVar to an IntVar."
            )

        if isinstance(val, bool):
            return 1 if val else 0
        if isinstance(val, int):
            return val
        if isinstance(val, float):
            return int(val)

        if hasattr(val, "node"):
            t = val.node.type
            float_nodes = [
                "FloatVariableNode",
                "GetFloatVariableValueNode",
                "RandomFloatNode",
                "IntToFloatNode",
                "AddNode",
                "SubtractNode",
                "MultiplyNode",
                "DivideNode",
            ]
            if t in float_nodes:
                return nodes.float_to_int(float_val=val).int
            return val

        raise TypeError(
            f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to IntVariable."
        )

    def to_string(self, decimals=0):
        f_val = int_to_float(int_val=self.value).float
        dec_node = int_value(val=decimals).value
        return float_to_string(float_val=f_val, decimals=dec_node).result

    def __iadd__(self, other):
        self.set(nodes.int_add(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __isub__(self, other):
        self.set(nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __imod__(self, other):
        self.set(nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __add__(self, other):
        return nodes.int_add(a=self.value, b=self._cast_to_int(other)).result

    def __radd__(self, other):
        return nodes.int_add(a=self._cast_to_int(other), b=self.value).result

    def __sub__(self, other):
        return nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result

    def __rsub__(self, other):
        return nodes.int_subtract(a=self._cast_to_int(other), b=self.value).result

    def __mod__(self, other):
        return nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result

    def __rmod__(self, other):
        return nodes.int_modulo(a=self._cast_to_int(other), b=self.value).result

    def __itruediv__(self, other):

        f_self = int_to_float(int_val=self.value).float

        if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
            f_other = other.value
        elif hasattr(other, "value") and other.__class__.__name__ == "IntVar":
            f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)):
            f_other = float_value(val=float(other)).value
        elif hasattr(other, "node"):
            t = other.node.type
            int_nodes = [
                "IntVariableNode",
                "GetIntVariableValueNode",
                "RandomIntNode",
                "FloatToIntNode",
                "IntAddNode",
                "IntSubtractNode",
                "IntMultiplyNode",
                "IntDivideNode",
                "IntModuloNode",
                "CounterNode",
            ]
            if t in int_nodes:
                f_other = int_to_float(int_val=other).float
            else:
                f_other = other
        else:
            raise TypeError(
                f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division."
            )

        f_result = divide_node(a=f_self, b=f_other).result
        self.set(float_to_int(float_val=f_result).int)
        return self

    def __truediv__(self, other):
        f_self = int_to_float(int_val=self.value).float

        if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
            f_other = other.value
        elif hasattr(other, "value") and other.__class__.__name__ == "IntVar":
            f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)):
            f_other = float_value(val=float(other)).value
        elif hasattr(other, "node"):
            t = other.node.type
            int_nodes = [
                "IntVariableNode",
                "GetIntVariableValueNode",
                "RandomIntNode",
                "FloatToIntNode",
                "IntAddNode",
                "IntSubtractNode",
                "IntMultiplyNode",
                "IntDivideNode",
                "IntModuloNode",
                "CounterNode",
            ]
            if t in int_nodes:
                f_other = int_to_float(int_val=other).float
            else:
                f_other = other
        else:
            raise TypeError(
                f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division."
            )

        return divide_node(a=f_self, b=f_other).result

    def __rtruediv__(self, other):
        f_self = int_to_float(int_val=self.value).float

        if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
            f_other = other.value
        elif hasattr(other, "value") and other.__class__.__name__ == "IntVar":
            f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)):
            f_other = float_value(val=float(other)).value
        elif hasattr(other, "node"):
            t = other.node.type
            int_nodes = [
                "IntVariableNode",
                "GetIntVariableValueNode",
                "RandomIntNode",
                "FloatToIntNode",
                "IntAddNode",
                "IntSubtractNode",
                "IntMultiplyNode",
                "IntDivideNode",
                "IntModuloNode",
                "CounterNode",
            ]
            if t in int_nodes:
                f_other = int_to_float(int_val=other).float
            else:
                f_other = other
        else:
            raise TypeError(
                f"❌ Type Error: Unsupported dividend type '{type(other).__name__}' for division."
            )

        return divide_node(a=f_other, b=f_self).result

    def __ifloordiv__(self, other):
        self.set(nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __floordiv__(self, other):
        return nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result

    def __rfloordiv__(self, other):
        return nodes.int_divide(a=self._cast_to_int(other), b=self.value).result

    def __imul__(self, other):
        is_float_op = False
        if isinstance(other, float) or (
            hasattr(other, "value") and other.__class__.__name__ == "FloatVar"
        ):
            is_float_op = True
        elif hasattr(other, "node"):
            t = other.node.type
            float_nodes = [
                "FloatVariableNode",
                "GetFloatVariableValueNode",
                "RandomFloatNode",
                "IntToFloatNode",
                "AddNode",
                "SubtractNode",
                "MultiplyNode",
                "DivideNode",
            ]
            if t in float_nodes:
                is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
                f_other = other.value  # type: ignore
            elif isinstance(other, float):
                f_other = float_value(val=other).value
            else:
                f_other = other
            f_result = multiply_node(a=f_self, b=f_other).result
            self.set(float_to_int(float_val=f_result).int)
        else:
            self.set(int_multiply(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __mul__(self, other):
        is_float_op = False
        if isinstance(other, float) or (
            hasattr(other, "value") and other.__class__.__name__ == "FloatVar"
        ):
            is_float_op = True
        elif hasattr(other, "node"):
            t = other.node.type
            float_nodes = [
                "FloatVariableNode",
                "GetFloatVariableValueNode",
                "RandomFloatNode",
                "IntToFloatNode",
                "AddNode",
                "SubtractNode",
                "MultiplyNode",
                "DivideNode",
            ]
            if t in float_nodes:
                is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
                f_other = other.value  # type: ignore
            elif isinstance(other, float):
                f_other = float_value(val=other).value
            else:
                f_other = other
            return multiply_node(a=f_self, b=f_other).result
        else:
            return int_multiply(a=self.value, b=self._cast_to_int(other)).result

    def __rmul__(self, other):
        is_float_op = False
        if isinstance(other, float) or (
            hasattr(other, "value") and other.__class__.__name__ == "FloatVar"
        ):
            is_float_op = True
        elif hasattr(other, "node"):
            t = other.node.type
            float_nodes = [
                "FloatVariableNode",
                "GetFloatVariableValueNode",
                "RandomFloatNode",
                "IntToFloatNode",
                "AddNode",
                "SubtractNode",
                "MultiplyNode",
                "DivideNode",
            ]
            if t in float_nodes:
                is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, "value") and other.__class__.__name__ == "FloatVar":
                f_other = other.value  # type: ignore
            elif isinstance(other, float):
                f_other = float_value(val=other).value
            else:
                f_other = other
            return multiply_node(a=f_other, b=f_self).result
        else:
            return int_multiply(a=self._cast_to_int(other), b=self.value).result

    def __eq__(self, other): # type: ignore
        return self.value == self._cast_to_int(other)  # type: ignore

    def __ne__(self, other): # type: ignore
        return self.value != self._cast_to_int(other)  # type: ignore

    def __gt__(self, other):
        return self.value > self._cast_to_int(other)

    def __lt__(self, other):
        return self.value < self._cast_to_int(other)

    def __ge__(self, other):
        return self.value >= self._cast_to_int(other)

    def __le__(self, other):
        return self.value <= self._cast_to_int(other)


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
            asset_init_val = (
                float(start_val)
                if isinstance(start_val, (int, float))
                and not isinstance(start_val, bool)
                else 0.0
            )
            self._node = nodes.float_variable(
                var_name=name, initial_value=asset_init_val
            )
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, (int, float)) or isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_float_variable_value(
                    variable=self.variable, value=self._cast_to_float(start_val)
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

    def _is_float_port(self):
        return True

    def _get_primary_port(self):
        return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_float_variable_value(variable=self.variable).value

    def set(self, value):

        node = nodes.set_float_variable_value(variable=self.variable, value=value)
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.id, "完成")
        return self

    def _cast_to_float(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "FloatVar":
            return val.value
        if cls_name == "IntVar":
            return nodes.int_to_float(int_val=val.value).float
        if cls_name == "BoolVar":
            raise TypeError(
                "❌ Type Error: Cannot implicitly cast a BoolVar to a FloatVar."
            )

        if isinstance(val, bool):
            return 1.0 if val else 0.0
        if isinstance(val, float):
            return val
        if isinstance(val, int):
            return float(val)

        if hasattr(val, "node"):
            t = val.node.type
            int_nodes = [
                "IntVariableNode",
                "GetIntVariableValueNode",
                "RandomIntNode",
                "FloatToIntNode",
                "IntAddNode",
                "IntSubtractNode",
                "IntMultiplyNode",
                "IntDivideNode",
                "IntModuloNode",
                "CounterNode",
            ]
            if t in int_nodes:
                return nodes.int_to_float(int_val=val).float
            return val

        raise TypeError(
            f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to FloatVar."
        )

    def to_string(self, decimals=2):
        dec_node = int_value(val=decimals).value
        return float_to_string(float_val=self.value, decimals=dec_node).result

    def __iadd__(self, other):
        self.set(nodes.add_node(a=self.value, b=self._cast_to_float(other)).result)
        return self

    def __isub__(self, other):
        self.set(nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result)
        return self

    def __imul__(self, other):
        self.set(nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result)
        return self

    def __itruediv__(self, other):
        self.set(nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result)
        return self

    def __add__(self, other):
        return nodes.add_node(a=self.value, b=self._cast_to_float(other)).result

    def __radd__(self, other):
        return nodes.add_node(a=self._cast_to_float(other), b=self.value).result

    def __sub__(self, other):
        return nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result

    def __rsub__(self, other):
        return nodes.subtract_node(a=self._cast_to_float(other), b=self.value).result

    def __mul__(self, other):
        return nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result

    def __rmul__(self, other):
        return nodes.multiply_node(a=self._cast_to_float(other), b=self.value).result

    def __truediv__(self, other):
        return nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result

    def __rtruediv__(self, other):
        return nodes.divide_node(a=self._cast_to_float(other), b=self.value).result

    def __eq__(self, other): # type: ignore
        return self.value == self._cast_to_float(other)  # type: ignore

    def __ne__(self, other): # type: ignore
        return self.value != self._cast_to_float(other)  # type: ignore

    def __gt__(self, other):
        return self.value > self._cast_to_float(other)

    def __lt__(self, other):
        return self.value < self._cast_to_float(other)

    def __ge__(self, other):
        return self.value >= self._cast_to_float(other)

    def __le__(self, other):
        return self.value <= self._cast_to_float(other)


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
            self._node = nodes.bool_variable(
                var_name=name, initial_value=asset_init_val
            )
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, bool):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_bool_variable_value(
                    variable=self.variable, value=self._cast_to_bool(start_val)
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

    def _is_float_port(self):
        return False

    def _get_primary_port(self):
        return self.value

    @property
    def variable(self):
        return self._get_current_node().variable

    @property
    def value(self):
        return nodes.get_bool_variable_value(variable=self.variable).value

    def set(self, value):

        # Pass variable and value directly
        node = nodes.set_bool_variable_value(variable=self.variable, value=value)

        # Update trigger stack to "完成" (matches onComplete_PortName="完成")
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.id, "完成")
        return self

    def _cast_to_bool(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "BoolVar":
            return val.value
        if cls_name in ["IntVar", "FloatVar"]:
            raise TypeError(
                "❌ Type Error: Cannot perform implicit boolean logic on numeric Variables."
            )

        if isinstance(val, bool):
            return val
        if isinstance(val, (int, float)):
            return bool(val)

        if hasattr(val, "node"):
            t = val.node.type
            bool_nodes = [
                "BoolValueNode",
                "BoolVariableNode",
                "GetBoolVariableValueNode",
                "ToggleNode",
                "CompareIntNode",
                "CompareFloatNode",
                "CompareGameObjectNode",
                "ComparePlantTypeNode",
                "CompareZombieTypeNode",
                "AndNode",
                "OrNode",
                "NotNode",
            ]
            if t in bool_nodes:
                return val
            raise TypeError(
                f"❌ Type Error: The node output '{t}' is not a valid boolean."
            )

        return val

    def toggle(self):
        with If(self.value == True) as flow:
            self.set(False)
        with flow.Else:
            self.set(True)

    def to_string(self):
        """Converts the BoolVar to a string node output ('True' / 'False')."""

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

    def __eq__(self, other):  # type: ignore
        return self.value == self._cast_to_bool(other)

    def __ne__(self, other):  # type: ignore
        return self.value != self._cast_to_bool(other)


# endregion


class Option:
    """
    Standalone multiple choice option card.
    Instantiates its node and compiles its callback graph once for reuse across multiple menus.
    """

    def __init__(
        self,
        title: str,
        description: str,
        callback: Callable[[], None] | None = None,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> None:
        p_val = plant_type.value if isinstance(plant_type, PlantType) else plant_type
        z_val = (
            zombie_type.value if isinstance(zombie_type, ZombieType) else zombie_type
        )

        if p_val != -1 and p_val != 254 and z_val != -1:
            print(
                "[Warning] Option: Cannot set both Plant and Zombie type. Defaulting to Plant."
            )
            z_val = -1
        elif p_val == -1 and z_val == -1:
            p_val = 254

        self.title: str = title
        self.description: str = description
        self.callback: Callable[[], None] | None = callback
        self.plant_type: int = p_val
        self.zombie_type: int = z_val

        self.node_id: str = ctx._generate_uuid()
        self._build_node()

    def _build_node(self) -> None:
        kwargs = {
            "class": "AddMultipleChoiceOptionNode",
            "ns": "GameLevel.EventNodes",
            "asm": "Assembly-CSharp",
            "title": self.title,
            "description": self.description,
            "plantType": self.plant_type,
            "zombieType": self.zombie_type,
            "list_PortName": "选项列表",
            "title_PortName": "标题",
            "description_PortName": "描述",
            "plantType_PortName": "植物类型",
            "zombieType_PortName": "僵尸类型",
            "optionSelected_PortName": "选项被点击",
        }
        ctx.nodes.append(
            {
                "id": self.node_id,
                "type": "AddMultipleChoiceOptionNode",
                "kwargs": kwargs,
            }
        )

        # Compile option callback logic once
        if self.callback:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            ctx.trigger_stack.append(ExecutionPath(self.node_id, "选项被点击"))
            try:
                self.callback()
            finally:
                ctx.trigger_stack.clear()
                ctx.trigger_stack.extend(saved_stack)

    @property
    def output_port(self) -> tuple[str, str]:
        return (self.node_id, "选项列表")

    def _get_primary_port(self) -> tuple[str, str]:
        return self.output_port


class MultiSelectMenu:
    """
    Deferred UI Builder for Multiple Choice Menus.
    Supports sharing Option instances across menus using merge nodes.
    """

    def __init__(
        self,
        is_rerollable: bool = True,
        reroll_count: int = 3,
        is_skippable: bool = False,
        window_count: int = 3,
    ) -> None:
        self.refreshable: bool = is_rerollable
        self.refreshCount: int = reroll_count
        self.cancelable: bool = is_skippable
        self.windowCount: int = window_count

        self._options: list[Option] = []
        self._show_node_id: str | None = None
        self.Output: MultiSelectMenu._Outputs = self._Outputs(self)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    @property
    def _get_show_node_id(self) -> str:
        if self._show_node_id is None:
            raise RuntimeError(
                "ShowMultipleChoiceMenuNode has not been generated yet. Call menu.show() first."
            )
        return self._show_node_id

    @overload
    def add_option(self, option: Option) -> Option:
        """Add a pre-instantiated Option object."""

    @overload
    def add_option(
        self,
        title: str,
        description: str,
        callback: Callable[[], None] | None = None,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> Option:
        """Create and register an Option card inline."""

    def add_option(self, *args: Any, **kwargs: Any) -> Option:
        if args and isinstance(args[0], Option):
            opt = args[0]
        elif "option" in kwargs and isinstance(kwargs["option"], Option):
            opt = kwargs["option"]
        else:
            # Extract arguments for inline Option creation
            title = args[0] if len(args) > 0 else kwargs.get("title", "")
            description = args[1] if len(args) > 1 else kwargs.get("description", "")
            callback = args[2] if len(args) > 2 else kwargs.get("callback", None)
            plant_type = args[3] if len(args) > 3 else kwargs.get("plant_type", 254)
            zombie_type = args[4] if len(args) > 4 else kwargs.get("zombie_type", -1)

            opt = Option(
                title=title,
                description=description,
                callback=callback,
                plant_type=plant_type,
                zombie_type=zombie_type,
            )

        self._options.append(opt)
        return opt

    def option(
        self,
        title: str,
        description: str,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> Callable[[Callable[[], None]], Option]:
        """Decorator syntax to register a choice callback cleanly inline."""

        def decorator(func: Callable[[], None]) -> Option:
            opt = Option(
                title=title,
                description=description,
                callback=func,
                plant_type=plant_type,
                zombie_type=zombie_type,
            )
            self._options.append(opt)
            return opt

        return decorator

    def show(self) -> None:
        """
        Merges all registered Option lists, links them to ShowMultipleChoiceMenuNode,
        and connects execution triggers into the compiler graph.
        """

        self._show_node_id = ctx._generate_uuid()
        show_kwargs = {
            "class": "ShowMultipleChoiceMenuNode",
            "ns": "GameLevel.EventNodes",
            "asm": "Assembly-CSharp",
            "refreshable": self.refreshable,
            "refreshCount": self.refreshCount,
            "cancelable": self.cancelable,
            "windowCount": self.windowCount,
            "trigger_PortName": "触发",
            "options_PortName": "选项列表",
            "refreshable_PortName": "可刷新",
            "refreshCount_PortName": "刷新次数",
            "cancelable_PortName": "可取消",
            "windowCount_PortName": "窗口数量",
            "actionOnExit_PortName": "退出时触发",
            "actionOnRefresh_PortName": "刷新时触发",
        }
        ctx.nodes.append(
            {
                "id": self._show_node_id,
                "type": "ShowMultipleChoiceMenuNode",
                "kwargs": show_kwargs,
            }
        )

        # Connect execution trigger into menu display node
        current_execution = ctx.trigger_stack[-1]
        ctx.add_connection(
            current_execution.id,
            current_execution.out_trigger,
            self._show_node_id,
            "触发",
        )

        # Merge and wire option lists
        if self._options:
            if len(self._options) == 1:
                ctx.add_connection(
                    self._options[0].node_id, "选项列表", self._show_node_id, "选项列表"
                )
            else:
                # 1. Merge first two Option nodes
                first_merge = nodes.merge_multiple_choice_option_lists(
                    list1=(self._options[0].node_id, "选项列表"),
                    list2=(self._options[1].node_id, "选项列表"),
                )

                prev_node_id = first_merge.id

                # 2. Chain subsequent options one by one
                for next_opt in self._options[2:]:
                    next_merge = nodes.merge_multiple_choice_option_lists(
                        list1=(prev_node_id, "合并列表"),
                        list2=(next_opt.node_id, "选项列表"),
                    )
                    prev_node_id = next_merge.id

                # 3. Connect the final merge node's merged list to the menu
                ctx.add_connection(
                    prev_node_id, "合并列表", self._show_node_id, "选项列表"
                )

        # Advance trigger stack past the menu window
        ctx.trigger_stack[-1] = ExecutionPath(self._show_node_id, "退出时触发")

    class _Outputs:
        def __init__(self, parent: MultiSelectMenu) -> None:
            self._parent = parent

        @property
        def OnExit(self) -> ExecutionPath:
            return ExecutionPath(self._parent._get_show_node_id, "退出时触发")

        @property
        def OnRefresh(self) -> ExecutionPath:
            return ExecutionPath(self._parent._get_show_node_id, "刷新时触发")

        def on_exit(self) -> ExecutionPath:
            return self.OnExit

        def on_refresh(self) -> ExecutionPath:
            return self.OnRefresh


class ForEachPlant:
    """Safely loops through plants and acts as a direct proxy to the current Plant object."""

    def __init__(self, plant_list_port):

        # Unpack list wrappers if passed directly
        if hasattr(plant_list_port, "list_port"):
            plant_list_port = plant_list_port.list_port
        elif hasattr(plant_list_port, "value"):
            plant_list_port = plant_list_port.value

        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        self._plant_cache = None

    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Returns an execution path context manager for post-loop logic."""
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

        # Unpack list wrappers if passed directly
        if hasattr(type_list_port, "list_port"):
            type_list_port = type_list_port.list_port
        elif hasattr(type_list_port, "value"):
            type_list_port = type_list_port.value

        self.node = nodes.for_each_plant_type(type_list=type_list_port)

    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Returns an execution path context manager for post-loop logic."""
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

    def __init__(self, initial: Any | None = None, initialize_empty: bool = True):

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
        elif isinstance(initial, (list, tuple, set)) and not isinstance(
            initial, PortReference
        ):
            items = list(initial)
            if len(items) == 0:
                storage = nodes.plant_type_list_storage(
                    op=0, init_empty=initialize_empty
                )
                self._current_port = storage.currentList
                self._count_port = storage.count
            else:
                raw_types = [
                    item.value if isinstance(item, Enum) else int(item)
                    for item in items
                ]
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

    def set(self, other: PlantTypeList | Iterable | Enum | int | Any):
        new_list = PlantTypeList(other)
        self._current_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type):
        """
        Uses ForEachPlantTypeNode to search MultiPlantTypeListNode.
        Strictly prevents duplicate trigger wiring by isolating BaseNode.__init__.
        """

        # 1. Resolve target port reference safely
        raw_target = target_type.value if hasattr(target_type, "value") else target_type
        if isinstance(raw_target, int) and not isinstance(raw_target, PortReference):
            target_port = nodes.plant_type_value(val=raw_target).value
        elif hasattr(raw_target, "_get_primary_port"):
            target_port = raw_target._get_primary_port()  # type: ignore
        elif hasattr(raw_target, "value"):
            target_port = raw_target.value  # type: ignore
        else:
            target_port = raw_target

        parent_trigger = ctx.trigger_stack[-1] if ctx.trigger_stack else None

        # 🎯 CRITICAL: Keep trigger stack empty during node construction
        # to prevent BaseNode from auto-connecting parent_trigger in parallel!
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        # 2. Instantiate search nodes cleanly with zero auto-wires
        match_toggle = nodes.toggle_node(initial_state=False)
        reset_branch = nodes.branch_node(condition=match_toggle.state)
        loop = nodes.for_each_plant_type(type_list=self._current_port)

        curr_type = PortReference(loop, "当前类型")
        is_equal = nodes.compare_plant_type(a=curr_type, b=target_port).equal
        match_branch = nodes.branch_node(condition=is_equal)
        state_guard = nodes.branch_node(condition=match_toggle.state)

        # 3. Explicit Single-Track Execution Wiring
        if parent_trigger:
            ctx.add_connection(
                parent_trigger.id, parent_trigger.out_trigger, reset_branch.id, "触发"
            )

        # Reset toggle if True, otherwise continue directly into loop
        ctx.add_connection(reset_branch.id, "真（触发）", match_toggle.id, "触发")
        ctx.add_connection(reset_branch.id, "真（触发）", loop.id, "触发")
        ctx.add_connection(reset_branch.id, "假（停止）", loop.id, "触发")

        # Loop body -> match check -> state guard -> toggle
        ctx.add_connection(loop.id, "循环体", match_branch.id, "触发")
        ctx.add_connection(match_branch.id, "真（触发）", state_guard.id, "触发")
        ctx.add_connection(state_guard.id, "假（停止）", match_toggle.id, "触发")

        # 4. Restore stack and forward execution strictly through loop's OnComplete
        ctx.trigger_stack.extend(saved_stack)
        ctx.trigger_stack[-1] = ExecutionPath(loop.id, "循环完成")

        return match_toggle.state

    def contains(self, plant_type: Enum | int | Iterable | Any):

        if isinstance(plant_type, (list, set)) and not isinstance(
            plant_type, PortReference
        ):
            items = list(plant_type)
            if not items:
                return nodes.bool_value(val=True).value

            result_wire = None
            for p in items:
                check_wire = self._contains_single(p)
                result_wire = (
                    check_wire if result_wire is None else (result_wire & check_wire)
                )
            return result_wire

        return self._contains_single(plant_type)

    def __iadd__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        if isinstance(other, (Enum, int)):
            val = other.value if isinstance(other, Enum) else int(other)
            single_node = nodes.single_plant_type_list(plant_type=val)
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=single_node.plantTypeList
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            raw_types = [
                item.value if isinstance(item, Enum) else int(item) for item in other
            ]
            multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=multi_node.plantTypeList
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, PlantTypeList):
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=other.list_port
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif hasattr(other, "list_port") or hasattr(other, "node"):
            port = other.list_port if hasattr(other, "list_port") else other  # type: ignore
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=port
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count

        return self

    def __add__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list += other
        return copy_list

    def __isub__(self, other: PlantTypeList | Enum | int | Iterable | Any):

        if isinstance(other, (Enum, int)):
            raw_val = other.value if isinstance(other, Enum) else int(other)
            rem_node = nodes.remove_plant_type(
                list_in=self._current_port, plant_type=raw_val
            )
            self._current_port = rem_node.resultList
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            for item in other:
                self.__isub__(item)
        elif isinstance(other, PlantTypeList):
            with ForEachPlantType(other.list_port) as loop:
                rem_node = nodes.remove_plant_type(
                    list_in=self._current_port, plant_type=loop.plant_type
                )
                self._current_port = rem_node.resultList
        elif hasattr(other, "node"):
            rem_node = nodes.remove_plant_type(
                list_in=self._current_port, plant_type=other
            )
            self._current_port = rem_node.resultList

        return self

    def __sub__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list -= other
        return copy_list

    def __eq__(self, other: PlantTypeList | Any):  # type: ignore
        if isinstance(other, PlantTypeList):
            return nodes.compare_int(a=self.count, b=other.count).equal
        return False

    def add(self, plant_type: Enum | int | Any):
        self += plant_type
        return self

    def remove(self, plant_type: Enum | int | Any):
        self -= plant_type
        return self

    def get_random(self):
        return nodes.get_random_plant_type(list_in=self._current_port).result

    def merge(self, other: PlantTypeList | Any):
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

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def die(self):
        """Instantly destroys the plant."""
        return nodes.die_plant(plant=self.ref)

    def damage(self, amount):
        """Damages the plant by a specified amount."""

        float_amount = to_float_port(amount)
        return nodes.damage_plant(plant=self.ref, damage=float_amount)

    def heal(self, amount):
        """Heals the plant by a specified amount."""

        float_amount = to_float_port(amount)
        return nodes.heal_plant(plant=self.ref, heal_amount=float_amount)

    def add_shield(self, amount):
        """Adds shield to the plant."""

        float_amount = to_float_port(amount)
        return nodes.give_plant_shield(plant=self.ref, shield=float_amount)

    def move(self, col, row, force=False):
        """Moves the plant to a new grid cell. `force` bypasses all in-game placement checks."""

        int_col = to_int_port(col)
        int_row = to_int_port(row)
        bool_force = to_bool_port(force)
        return nodes.move_plant(
            plant=self.ref, row=int_row, column=int_col, force=bool_force
        )

    def move_relative(self, col_diff, row_diff, force=False):
        """Moves the plant relative to its current grid position."""
        return self.move(col=self.col + col_diff, row=self.row + row_diff, force=force)

    def modify_attack(self, multiplier):
        """Modifies attack multiplier."""

        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_attack(plant=self.ref, multiplier=float_multiplier)

    def modify_health(self, multiplier):
        """Modifies health multiplier."""

        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_health(plant=self.ref, multiplier=float_multiplier)

    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via plant_split)
    # ==========================================================
    @property
    def _split(self):
        if self._split_cache is None:
            self._split_cache = nodes.plant_split(plant=self.ref)
        return self._split_cache

    @property
    def plantType(self):
        return self._split.plantType

    @property
    def row(self):
        return self._split.row

    @property
    def col(self):
        return self._split.column

    @property
    def attributeCD(self):
        return self._split.attributeCountdown


class Zombie:
    """A smart wrapper for a Zombie pointer that exposes built-in actions and properties."""

    def __init__(self, zombie_ref):
        if isinstance(zombie_ref, Zombie):
            self.ref = zombie_ref.ref
        else:
            self.ref = zombie_ref

        self._split_cache = None

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def damage(self, amount):
        """Damages the zombie by a specified amount."""

        return nodes.damage_zombie(zombie=self.ref, damage=amount)

    def set_health_multiplier(self, ratio):
        """Modifies zombie health multiplier (ensures float/Single input to avoid C# cast crashes)."""

        float_ratio = to_float_port(ratio)
        return nodes.modify_zombie_health(zombie=self.ref, ratio=float_ratio)

    def hypnotize(self):
        """Mind-controls/hypnotizes the zombie to fight for the player."""

        return nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row, col):
        """Moves the zombie to a specific grid row and column."""

        int_row = to_int_port(row)
        int_col = to_int_port(col)
        return nodes.move_zombie(zombie=self.ref, row=int_row, column=int_col)

    def move_relative(self, row_diff=0, col_diff=0):
        """Moves the zombie relative to its current position."""
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    def play_animation(self, anim_name: str | Enum | Any = "idle"):
        """Plays a named animation clip on the zombie."""

        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        return nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)

    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via zombie_split)
    # ==========================================================
    @property
    def split(self):
        if self._split_cache is None:
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

        def __init__(self, interval: float | Any = 0.1):
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()

            self.ref = nodes.toggle_cycle_node(interval=interval)

            ctx.trigger_stack.extend(saved_stack)

            if ctx.trigger_stack:
                previous_exec = ctx.trigger_stack[-1]
                ctx.add_connection(
                    previous_exec.id, previous_exec.out_trigger, self.ref.id, "触发"
                )

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
                ctx.add_connection(
                    current_exec.id, current_exec.out_trigger, self.ref.id, "触发"
                )
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
    def __init__(self, mouse_ref=None):
        if mouse_ref is None:
            mouse_ref = nodes.on_mouse_click()
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


class Random:
    class TriggerChance:
        """Fires its contents based on a random probability (e.g. TriggerChance(0.5) is 50%)."""

        def __init__(self, probability):
            rand = Random.randf(0.0, 1.0)
            self.flow = If(rand <= probability)

        def __enter__(self):
            self.flow.__enter__()
            return self

        def __exit__(self, *args):
            self.flow.__exit__(*args)

    class RandomTrigger:
        """
        Triggers a random connected event.
        """

        def __init__(self, count=1, allow_repeat=False):
            self.node = nodes.random_trigger(count=count, allow_repeat=allow_repeat)

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

    @staticmethod
    def randint(min_val : int, max_val : int) -> int:
        return nodes.random_int(min_val=min_val, max_val=max_val).result  # type: ignore

    @staticmethod
    def randf(min_val : float, max_val : float) -> float:
        return nodes.random_float(min_val=min_val, max_val=max_val).result  # type: ignore

    @_staticproperty
    def value():
        """Return a random float between 0.0 and 1.0."""
        return Random.randf(0.0, 1.0)

    class Seeded:
        """
        A deterministic, graph-compatible pseudo-random number generator (LCG).
        Uses overflow-safe LCG constants (a=75, c=74, m=65537) to prevent C# 32-bit integer wrapping.
        """

        def __init__(self, seed: int = 12345, name: str = "PRNG_State"):
            from .extensions import IntVar

            # Clamp seed into valid positive range
            safe_seed = (abs(seed) % 65537) or 1
            self.state = IntVar(start_val=safe_seed, name=name)

            # Overflow-safe LCG constants: Max math is (75 * 65536 + 74) = 4,915,274 << 2,147,483,647
            self.a = 75
            self.c = 74
            self.m = 65537

        def set_seed(self, seed_value):
            """Manually update or reset the active random seed at runtime."""
            safe_seed = (abs(seed_value) % self.m) or 1
            return self.state.set(safe_seed)

        def _next(self):
            """Advances LCG state. Guaranteed strictly positive without overflow or BranchNodes."""
            next_state = ((self.state * self.a) + self.c) % self.m
            self.state.set(next_state)
            return self.state.value

        def randint(self, min_val: int, max_val: int):
            """Generates a seeded random integer within [min_val, max_val]."""
            range_size = (max_val - min_val) + 1
            raw_val = self._next()
            return min_val + (raw_val % range_size)

        def randf(self, min_val: float = 0.0, max_val: float = 1.0):
            """Generates a seeded random float within [min_val, max_val]."""
            raw_val = self._next()
            normalized = raw_val / float(self.m - 1)
            return min_val + (normalized * (max_val - min_val))

        class TriggerChance:
            """Context manager that fires based on seeded probability (0.0 to 1.0)."""

            def __init__(self, rng: Seeded, probability: float):  # type: ignore  # noqa: F821
                roll = rng.randf(0.0, 1.0)
                self.flow = If(roll <= probability)

            def __enter__(self):
                self.flow.__enter__()
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.flow.__exit__(exc_type, exc_val, exc_tb)


class InfoCard:
    """
    High-level manager for CreateInfoCardNode.
    Supports callbacks, context managers, decorators, and trigger outputs.
    """

    def __init__(
        self,
        big_title: Any,
        small_title: Any,
        callback: Optional[Callable[[], None]] = None
    ) -> None:
        self.big_title = big_title
        self.small_title = small_title
        self.callback = callback
        
        # Instantiate the underlying node
        self.node = nodes.create_info_card(
            big_title=self.big_title,
            small_title=self.small_title
        )
        self.node_id = self.node.id
        self.Output = self._Outputs(self)

        # Connect callback graph if provided
        if self.callback:
            self._compile_callback(self.callback)

    def _compile_callback(self, func: Callable[[], None]) -> None:
        """Isolates and compiles the click execution path graph."""
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()
        ctx.trigger_stack.append(self.Output.OnCardClicked)
        try:
            func()
        finally:
            ctx.trigger_stack.clear()
            ctx.trigger_stack.extend(saved_stack)

    def on_click(self, func: Callable[[], None]) -> Callable[[], None]:
        """Decorator syntax for handling card click events."""
        self._compile_callback(func)
        return func

    def __enter__(self) -> InfoCard:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    class _Outputs:
        """Execution paths for the card events."""

        def __init__(self, parent: InfoCard) -> None:
            self._parent = parent

        @property
        def OnCardClicked(self) -> ExecutionPath:
            """Triggered when the player clicks this card."""
            return ExecutionPath(self._parent.node_id, "点击卡牌时触发")

        @property
        def on_card_clicked(self) -> ExecutionPath:
            return self.OnCardClicked