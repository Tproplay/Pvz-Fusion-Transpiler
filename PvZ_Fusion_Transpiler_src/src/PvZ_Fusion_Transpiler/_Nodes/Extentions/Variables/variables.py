from __future__ import annotations

from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_int_port, to_float_port, to_bool_port


class IntVar:
    """Use to create a Variable Int Value. Don't use = to set the value, use .set() instead."""

    def __init__(self, start_val: Any = 0, node_ref: Any = None, name: str = "整数") -> None:
        self._nodes_by_scope: dict[str, Any] = {}

        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = (
                start_val
                if isinstance(start_val, int) and not isinstance(start_val, bool)
                else 0
            )
            self._node = nodes.int_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, int) or isinstance(start_val, bool):
                saved_stack = _ctx.trigger_stack[:]
                _ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_int_variable_value(
                    variable=self.variable, value=self._cast_to_int(start_val)
                )
                _ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                _ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self) -> Any:
        scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if hasattr(self._node, "asset") and self._node.asset is not None:
                new_node = nodes.int_variable(asset=self._node.asset)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self) -> bool:
        return False

    def _get_primary_port(self) -> Any:
        return self.value

    @property
    def variable(self) -> Any:
        return self._get_current_node().port_output_intvariable_Variable

    @property
    def value(self) -> Any:
        return nodes.get_int_variable_value(variable=self.variable).port_output_int_Value

    def set(self, value: Any) -> IntVar:
        node = nodes.set_int_variable_value(variable=self.variable, value=self._cast_to_int(value))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def _cast_to_int(self, val: Any) -> Any:
        cls_name = val.__class__.__name__
        if cls_name == "IntVar":
            return val.value
        if cls_name == "FloatVar":
            return nodes.float_to_int(float_val=val.value).port_output_int_IntValue
        if cls_name == "BoolVar":
            raise TypeError("Cannot implicitly cast a BoolVar to an IntVar.")
        if isinstance(val, bool):
            return 1 if val else 0
        if isinstance(val, int):
            return val
        if isinstance(val, float):
            return int(val)
        return to_int_port(val)

    def to_string(self, decimals: int = 0) -> Any:
        f_val = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
        dec_node = nodes.int_value(val=decimals).port_output_int_Value
        return nodes.float_to_string(float_val=f_val, decimals=dec_node).port_output_string_StringValue

    def __iadd__(self, other: Any) -> IntVar:
        self.set(nodes.int_add(a=self.value, b=self._cast_to_int(other)).port_output_int_Sum)
        return self

    def add_in_place(self, amount: Any) -> IntVar:
        node = nodes.int_variable_arithmetic(variable=self.variable, operand=self._cast_to_int(amount))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def __isub__(self, other: Any) -> IntVar:
        self.set(nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).port_output_int_Difference)
        return self

    def __imod__(self, other: Any) -> IntVar:
        self.set(nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).port_output_int_Remainder)
        return self

    def __add__(self, other: Any) -> Any:
        return nodes.int_add(a=self.value, b=self._cast_to_int(other)).port_output_int_Sum

    def __radd__(self, other: Any) -> Any:
        return nodes.int_add(a=self._cast_to_int(other), b=self.value).port_output_int_Sum

    def __sub__(self, other: Any) -> Any:
        return nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).port_output_int_Difference

    def __rsub__(self, other: Any) -> Any:
        return nodes.int_subtract(a=self._cast_to_int(other), b=self.value).port_output_int_Difference

    def __mod__(self, other: Any) -> Any:
        return nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).port_output_int_Remainder

    def __rmod__(self, other: Any) -> Any:
        return nodes.int_modulo(a=self._cast_to_int(other), b=self.value).port_output_int_Remainder

    def __ifloordiv__(self, other: Any) -> IntVar:
        self.set(nodes.int_divide(a=self.value, b=self._cast_to_int(other)).port_output_int_Quotient)
        return self

    def __floordiv__(self, other: Any) -> Any:
        return nodes.int_divide(a=self.value, b=self._cast_to_int(other)).port_output_int_Quotient

    def __rfloordiv__(self, other: Any) -> Any:
        return nodes.int_divide(a=self._cast_to_int(other), b=self.value).port_output_int_Quotient

    def __itruediv__(self, other: Any) -> IntVar:
        f_self = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
        f_other = to_float_port(other)
        f_result = nodes.divide_node(a=f_self, b=f_other).port_output_float_Quotient
        self.set(nodes.float_to_int(float_val=f_result).port_output_int_IntValue)
        return self

    def __truediv__(self, other: Any) -> Any:
        f_self = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
        f_other = to_float_port(other)
        return nodes.divide_node(a=f_self, b=f_other).port_output_float_Quotient

    def __rtruediv__(self, other: Any) -> Any:
        f_self = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
        f_other = to_float_port(other)
        return nodes.divide_node(a=f_other, b=f_self).port_output_float_Quotient

    def __imul__(self, other: Any) -> IntVar:
        if isinstance(other, float) or (hasattr(other, "value") and getattr(other, "__class__").__name__ == "FloatVar"):
            f_self = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
            f_other = to_float_port(other)
            f_result = nodes.multiply_node(a=f_self, b=f_other).port_output_float_Product
            self.set(nodes.float_to_int(float_val=f_result).port_output_int_IntValue)
        else:
            self.set(nodes.int_multiply(a=self.value, b=self._cast_to_int(other)).port_output_int_Product)
        return self

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, float) or (hasattr(other, "value") and getattr(other, "__class__").__name__ == "FloatVar"):
            f_self = nodes.int_to_float(int_val=self.value).port_output_float_FloatValue
            f_other = to_float_port(other)
            return nodes.multiply_node(a=f_self, b=f_other).port_output_float_Product
        return nodes.int_multiply(a=self.value, b=self._cast_to_int(other)).port_output_int_Product

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def __eq__(self, other: Any) -> Any:  # type: ignore
        return self.value == self._cast_to_int(other)  # type: ignore

    def __ne__(self, other: Any) -> Any:  # type: ignore
        return self.value != self._cast_to_int(other)  # type: ignore

    def __gt__(self, other: Any) -> Any:
        return self.value > self._cast_to_int(other)

    def __lt__(self, other: Any) -> Any:
        return self.value < self._cast_to_int(other)

    def __ge__(self, other: Any) -> Any:
        return self.value >= self._cast_to_int(other)

    def __le__(self, other: Any) -> Any:
        return self.value <= self._cast_to_int(other)

    def __repr__(self) -> str:
        return f"<IntVar value={self.value}>"


class FloatVar:
    """Use to create a Variable Float Value. Don't use = to set the value, use .set() instead."""

    def __init__(self, start_val: Any = 0.0, node_ref: Any = None, name: str = "浮点数") -> None:
        self._nodes_by_scope: dict[str, Any] = {}

        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = (
                float(start_val)
                if isinstance(start_val, (int, float)) and not isinstance(start_val, bool)
                else 0.0
            )
            self._node = nodes.float_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, (int, float)) or isinstance(start_val, bool):
                saved_stack = _ctx.trigger_stack[:]
                _ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_float_variable_value(
                    variable=self.variable, value=self._cast_to_float(start_val)
                )
                _ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                _ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self) -> Any:
        scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if hasattr(self._node, "asset") and self._node.asset is not None:
                new_node = nodes.float_variable(asset=self._node.asset)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self) -> bool:
        return True

    def _get_primary_port(self) -> Any:
        return self.value

    @property
    def variable(self) -> Any:
        return self._get_current_node().port_output_floatvariable_Variable

    @property
    def value(self) -> Any:
        return nodes.get_float_variable_value(variable=self.variable).port_output_float_Value

    def set(self, value: Any) -> FloatVar:
        node = nodes.set_float_variable_value(variable=self.variable, value=self._cast_to_float(value))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def _cast_to_float(self, val: Any) -> Any:
        cls_name = val.__class__.__name__
        if cls_name == "FloatVar":
            return val.value
        if cls_name == "IntVar":
            return nodes.int_to_float(int_val=val.value).port_output_float_FloatValue
        if cls_name == "BoolVar":
            raise TypeError("Cannot implicitly cast a BoolVar to a FloatVar.")
        if isinstance(val, bool):
            return 1.0 if val else 0.0
        if isinstance(val, float):
            return val
        if isinstance(val, int):
            return float(val)
        return to_float_port(val)

    def to_string(self, decimals: int = 2) -> Any:
        dec_node = nodes.int_value(val=decimals).port_output_int_Value
        return nodes.float_to_string(float_val=self.value, decimals=dec_node).port_output_string_StringValue

    def __iadd__(self, other: Any) -> FloatVar:
        self.set(nodes.add_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Result)
        return self

    def add_in_place(self, amount: Any) -> FloatVar:
        node = nodes.float_variable_arithmetic(variable=self.variable, operand=self._cast_to_float(amount))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def __isub__(self, other: Any) -> FloatVar:
        self.set(nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Difference)
        return self

    def __imul__(self, other: Any) -> FloatVar:
        self.set(nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Product)
        return self

    def __itruediv__(self, other: Any) -> FloatVar:
        self.set(nodes.divide_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Quotient)
        return self

    def __add__(self, other: Any) -> Any:
        return nodes.add_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Result

    def __radd__(self, other: Any) -> Any:
        return nodes.add_node(a=self._cast_to_float(other), b=self.value).port_output_float_Result

    def __sub__(self, other: Any) -> Any:
        return nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Difference

    def __rsub__(self, other: Any) -> Any:
        return nodes.subtract_node(a=self._cast_to_float(other), b=self.value).port_output_float_Difference

    def __mul__(self, other: Any) -> Any:
        return nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Product

    def __rmul__(self, other: Any) -> Any:
        return nodes.multiply_node(a=self._cast_to_float(other), b=self.value).port_output_float_Product

    def __truediv__(self, other: Any) -> Any:
        return nodes.divide_node(a=self.value, b=self._cast_to_float(other)).port_output_float_Quotient

    def __rtruediv__(self, other: Any) -> Any:
        return nodes.divide_node(a=self._cast_to_float(other), b=self.value).port_output_float_Quotient

    def __eq__(self, other: Any) -> Any:  # type: ignore
        return self.value == self._cast_to_float(other)  # type: ignore

    def __ne__(self, other: Any) -> Any:  # type: ignore
        return self.value != self._cast_to_float(other)  # type: ignore

    def __gt__(self, other: Any) -> Any:
        return self.value > self._cast_to_float(other)

    def __lt__(self, other: Any) -> Any:
        return self.value < self._cast_to_float(other)

    def __ge__(self, other: Any) -> Any:
        return self.value >= self._cast_to_float(other)

    def __le__(self, other: Any) -> Any:
        return self.value <= self._cast_to_float(other)

    def __repr__(self) -> str:
        return f"<FloatVar value={self.value}>"


class BoolVar:
    """Use to create a Variable Bool Value. Don't use = to set the value, use .set() instead."""

    def __init__(self, start_val: Any = False, node_ref: Any = None, name: str = "布尔值") -> None:
        self._nodes_by_scope: dict[str, Any] = {}

        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = bool(start_val) if isinstance(start_val, bool) else False
            self._node = nodes.bool_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, bool):
                saved_stack = _ctx.trigger_stack[:]
                _ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_bool_variable_value(
                    variable=self.variable, value=self._cast_to_bool(start_val)
                )
                _ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                _ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self) -> Any:
        scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if hasattr(self._node, "asset") and self._node.asset is not None:
                new_node = nodes.bool_variable(asset=self._node.asset)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _is_float_port(self) -> bool:
        return False

    def _get_primary_port(self) -> Any:
        return self.value

    @property
    def variable(self) -> Any:
        return self._get_current_node().port_output_boolvariable_Variable

    @property
    def value(self) -> Any:
        return nodes.get_bool_variable_value(variable=self.variable).port_output_bool_Value

    def set(self, value: Any) -> BoolVar:
        node = nodes.set_bool_variable_value(variable=self.variable, value=self._cast_to_bool(value))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def _cast_to_bool(self, val: Any) -> Any:
        cls_name = val.__class__.__name__
        if cls_name == "BoolVar":
            return val.value
        if isinstance(val, bool):
            return val
        return to_bool_port(val)

    def __invert__(self) -> Any:
        return nodes.not_node(input=self.value).port_output_bool_Output

    def __and__(self, other: Any) -> Any:
        return nodes.and_node(a=self.value, b=self._cast_to_bool(other)).port_output_bool_Result

    def __rand__(self, other: Any) -> Any:
        return nodes.and_node(a=self._cast_to_bool(other), b=self.value).port_output_bool_Result

    def __or__(self, other: Any) -> Any:
        return nodes.or_node(a=self.value, b=self._cast_to_bool(other)).port_output_bool_Result

    def __ror__(self, other: Any) -> Any:
        return nodes.or_node(a=self._cast_to_bool(other), b=self.value).port_output_bool_Result

    def __eq__(self, other: Any) -> Any:  # type: ignore
        return self.value == self._cast_to_bool(other)  # type: ignore

    def __ne__(self, other: Any) -> Any:  # type: ignore
        return self.value != self._cast_to_bool(other)  # type: ignore

    def __repr__(self) -> str:
        return f"<BoolVar value={self.value}>"


__all__ = ["IntVar", "FloatVar", "BoolVar"]
