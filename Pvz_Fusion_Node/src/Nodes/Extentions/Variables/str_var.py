"""
High-level StrVar combining StringVariableAsset, GetStringVariableValueNode, and SetStringVariableValueNode.
Implements IEquatable and string concatenation.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection
from ..extension_node import ExtensionNode
from ...Original.Variables.String.string_variable_asset import StringVariableAsset
from ...Original.Variables.String.get_string_variable_value_node import GetStringVariableValueNode
from ...Original.Variables.String.set_string_variable_value_node import SetStringVariableValueNode
from ...Original.Calculate.string_concat_node import StringConcatNode


class StrVar(ExtensionNode):
    """Unified high-level String Variable register and expression."""

    def __init__(
        self,
        name: str = "字符串",
        start_val: str = "",
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__()
        self.asset = StringVariableAsset(
            name=name,
            initial_value=str(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        self._get_node = GetStringVariableValueNode()
        self.attach_node(self._get_node)

    @property
    def name(self) -> str:
        return self.asset.name

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[str, Port, ExtensionNode]) -> SetStringVariableValueNode:
        set_node = SetStringVariableValueNode()
        self.attach_node(set_node)
        return set_node

    def get_primary_port(self) -> Port:
        return self.get()

    @property
    def value(self) -> Port:
        return self.get()

    def __add__(self, other: Any) -> Any:
        concat = StringConcatNode()
        self.attach_node(concat)
        return concat

    def __radd__(self, other: Any) -> Any:
        concat = StringConcatNode()
        self.attach_node(concat)
        return concat
