"""
High-level StrVar combining StringVariableAsset, StringVariableNode, GetStringVariableValueNode, and SetStringVariableValueNode.
Inherits from VariableExtension.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection, to_port
from .variable_extension import VariableExtension
from ...Original.Variables.String.string_variable_asset import StringVariableAsset
from ...Original.Variables.String.string_variable_node import StringVariableNode
from ...Original.Variables.String.get_string_variable_value_node import GetStringVariableValueNode
from ...Original.Variables.String.set_string_variable_value_node import SetStringVariableValueNode
from ...Original.Calculate.string_concat_node import StringConcatNode


class StrVar(VariableExtension):
    """Unified high-level String Variable register and expression."""

    def __init__(
        self,
        name: str = "字符串",
        start_val: str = "",
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        asset = StringVariableAsset(
            name=name,
            initial_value=str(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        super().__init__(name=name, asset=asset)

        # 1. Canvas Variable Definition Node
        self.var_node = StringVariableNode(
            var_name=name,
            initial_value=str(start_val),
            asset=self._asset,
        )
        self.attach_node(self.var_node)

        # 2. Canvas Getter Node wired to Variable Definition
        self._get_node = GetStringVariableValueNode()
        self.attach_node(self._get_node)
        self.var_node.get_output("变量") >> self._get_node.get_input("变量")

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[str, Port, Node, Any]) -> SetStringVariableValueNode:
        set_node = SetStringVariableValueNode()
        self.attach_node(set_node)
        self.var_node.get_output("变量") >> set_node.get_input("变量")
        val_port = to_port(value)
        val_port >> set_node.get_input("新值")
        return set_node

    def __add__(self, other: Any) -> Any:
        concat = StringConcatNode()
        self.attach_node(concat)
        self.get() >> concat.get_input("A")
        to_port(other) >> concat.get_input("B")
        return concat

    def __radd__(self, other: Any) -> Any:
        concat = StringConcatNode()
        self.attach_node(concat)
        to_port(other) >> concat.get_input("A")
        self.get() >> concat.get_input("B")
        return concat
