from __future__ import annotations
from typing import Any, Optional, Union
from ... import nodes
from ...nodes import (
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
from ...Core.context import ctx, ExecutionPath
from ...typing import to_int_port, to_float_port, to_bool_port
from .branching import If
from .extension_node import ExtensionNode
from .Variables.list_var import ListVar

class IntVar(ExtensionNode):
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
        super().__init__(root_node=self._node)

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

    def get_primary_port(self):
        return self.value

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


class FloatVar(ExtensionNode):
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
        super().__init__(root_node=self._node)

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

    def get_primary_port(self):
        return self.value

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


class BoolVar(ExtensionNode):
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
        super().__init__(root_node=self._node)

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

    def get_primary_port(self):
        return self.value

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


class StrVar(ExtensionNode):
    """Use to create a Variable String Value. Don't use = to set the value, use .set() instead."""

    def __init__(self, start_val="", node_ref=None, name: str = "字符串"):
        self._nodes_by_scope = {}

        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = str(start_val) if isinstance(start_val, str) else ""
            self._node = nodes.string_variable(
                var_name=name, initial_value=asset_init_val
            )
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, str):
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_string_variable_value(
                    variable=self.variable, value=self._cast_to_str(start_val)
                )
                ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                ctx.trigger_stack.extend(saved_stack)
        super().__init__(root_node=self._node)

    def _get_current_node(self):
        scope_key = ctx.trigger_stack[-1].id if ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if self._asset_dict:
                new_node = nodes.string_variable(asset_dict=self._asset_dict)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self):
        return False

    def get_primary_port(self):
        return self.value

    def _get_primary_port(self):
        return self.value

    @property
    def variable(self):
        return self._get_current_node().get_output("变量")

    @property
    def value(self):
        return nodes.get_string_variable_value(variable=self.variable).value

    def set(self, value):
        node = nodes.set_string_variable_value(variable=self.variable, value=self._cast_to_str(value))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.id, "完成")
        return self

    def _cast_to_str(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "StrVar":
            return val.value
        if hasattr(val, "to_string") and callable(val.to_string):
            return val.to_string()
        if isinstance(val, str):
            return val
        if isinstance(val, (int, float, bool)):
            return str(val)
        return val

    def to_string(self):
        return self.value

    def __add__(self, other):
        return nodes.string_concat(a=self.value, b=self._cast_to_str(other)).result

    def __radd__(self, other):
        return nodes.string_concat(a=self._cast_to_str(other), b=self.value).result

    def __iadd__(self, other):
        self.set(nodes.string_concat(a=self.value, b=self._cast_to_str(other)).result)
        return self


__all__ = [
    "IntVar",
    "FloatVar",
    "BoolVar",
    "StrVar",
    "ListVar",
]
