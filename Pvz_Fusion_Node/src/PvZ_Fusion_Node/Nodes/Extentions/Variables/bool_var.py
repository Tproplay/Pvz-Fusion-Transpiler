"""
High-level BoolVar combining BoolVariableAsset, GetBoolVariableValueNode, and SetBoolVariableValueNode.
Implements IEquatable and ILogical.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection
from ..extension_node import ExtensionNode
from ...Original.Variables.Boolean.bool_variable_asset import BoolVariableAsset
from ...Original.Variables.Boolean.get_bool_variable_value_node import GetBoolVariableValueNode
from ...Original.Variables.Boolean.set_bool_variable_value_node import SetBoolVariableValueNode


class BoolVar(ExtensionNode):
    """Unified high-level Boolean Variable register and expression."""

    def __init__(
        self,
        name: str = "布尔值",
        start_val: bool = False,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__()
        self.asset = BoolVariableAsset(
            name=name,
            initial_value=bool(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        self._get_node = GetBoolVariableValueNode()
        self.attach_node(self._get_node)

    @property
    def name(self) -> str:
        return self.asset.name

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[bool, Port, ExtensionNode]) -> SetBoolVariableValueNode:
        set_node = SetBoolVariableValueNode()
        self.attach_node(set_node)
        return set_node

    def get_primary_port(self) -> Port:
        return self.get()

    @property
    def value(self) -> Port:
        return self.get()

    def _create_logical_op_node(self, op: str, other: Any) -> Any:
        from ...Original.Logic.and_node import AndNode
        from ...Original.Logic.or_node import OrNode
        from ...Original.Logic.not_node import NotNode
        if op == "not":
            n = NotNode()
        elif op == "and":
            n = AndNode()
        elif op == "or":
            n = OrNode()
        else:
            raise NotImplementedError(f"Logic op {op} not supported")
        self.attach_node(n)
        return n
