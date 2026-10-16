from __future__ import annotations

from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_string_port


class StringVar:
    """Use to create a Variable String Value. Don't use = to set the value, use .set() instead."""

    def __init__(self, start_val: Any = "", node_ref: Any = None, name: str = "字符串") -> None:
        self._nodes_by_scope: dict[str, Any] = {}

        if node_ref:
            self._node = node_ref
            self._asset_dict = getattr(node_ref, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = node_ref
        else:
            asset_init_val = start_val if isinstance(start_val, str) else ""
            self._node = nodes.string_variable(var_name=name, initial_value=asset_init_val)
            self._asset_dict = getattr(self._node, "asset_dict", None)
            scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
            self._nodes_by_scope[scope_key] = self._node

            if not isinstance(start_val, str) or start_val != "":
                saved_stack = _ctx.trigger_stack[:]
                _ctx.trigger_stack.clear()
                init_trigger = nodes.on_board_start()
                set_node = nodes.set_string_variable_value(
                    variable=self.variable, value=to_string_port(start_val)
                )
                _ctx.add_connection(init_trigger.id, "触发", set_node.id, "触发")
                _ctx.trigger_stack.extend(saved_stack)

    def _get_current_node(self) -> Any:
        scope_key = _ctx.trigger_stack[-1].id if _ctx.trigger_stack else "global"
        if scope_key not in self._nodes_by_scope:
            if hasattr(self._node, "asset") and self._node.asset is not None:
                new_node = nodes.string_variable(asset=self._node.asset)
            else:
                new_node = self._node
            self._nodes_by_scope[scope_key] = new_node
        return self._nodes_by_scope[scope_key]

    def _get_primary_port(self) -> Any:
        return self.value

    @property
    def variable(self) -> Any:
        return self._get_current_node().port_output_stringvariable_Variable

    @property
    def value(self) -> Any:
        return nodes.get_string_variable_value(variable=self.variable).port_output_string_Value

    def set(self, value: Any) -> StringVar:
        node = nodes.set_string_variable_value(variable=self.variable, value=to_string_port(value))
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = ExecutionPath(node.port_output_trigger_Complete)
        return self

    def __iadd__(self, other: Any) -> StringVar:
        concatenated = nodes.string_concat(a=self.value, b=to_string_port(other)).port_output_string_Result
        return self.set(concatenated)

    def __add__(self, other: Any) -> Any:
        return nodes.string_concat(a=self.value, b=to_string_port(other)).port_output_string_Result

    def __radd__(self, other: Any) -> Any:
        return nodes.string_concat(a=to_string_port(other), b=self.value).port_output_string_Result

    def to_string(self) -> Any:
        return self.value


__all__ = ["StringVar"]
