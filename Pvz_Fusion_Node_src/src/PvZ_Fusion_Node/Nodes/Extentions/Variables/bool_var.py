"""
High-level BoolVar combining BoolVariableAsset, BoolVariableNode, GetBoolVariableValueNode, and SetBoolVariableValueNode.
Inherits from VariableExtension.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection, to_port
from .variable_extension import VariableExtension
from ...Original.Variables.Boolean.bool_variable_asset import BoolVariableAsset
from ...Original.Variables.Boolean.bool_variable_node import BoolVariableNode
from ...Original.Variables.Boolean.get_bool_variable_value_node import GetBoolVariableValueNode
from ...Original.Variables.Boolean.set_bool_variable_value_node import SetBoolVariableValueNode


class BoolVar(VariableExtension):
    """Unified high-level Boolean Variable register and expression."""

    def __init__(
        self,
        name: str = "布尔值",
        start_val: bool = False,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        asset = BoolVariableAsset(
            name=name,
            initial_value=bool(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        super().__init__(name=name, asset=asset)

        # 1. Canvas Variable Definition Node
        self.var_node = BoolVariableNode(
            var_name=name,
            initial_value=bool(start_val),
            asset=self._asset,
        )
        self.attach_node(self.var_node)

        # 2. Canvas Getter Node wired to Variable Definition
        self._get_node = GetBoolVariableValueNode()
        self.attach_node(self._get_node)
        self.var_node.get_output("变量") >> self._get_node.get_input("变量")

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[bool, Port, Node, Any]) -> SetBoolVariableValueNode:
        set_node = SetBoolVariableValueNode()
        self.attach_node(set_node)
        self.var_node.get_output("变量") >> set_node.get_input("变量")
        val_port = to_port(value)
        val_port >> set_node.get_input("新值")
        return set_node

    def _create_logical_op_node(self, op: str, other: Any) -> Any:
        from ...Original.Logic.and_node import AndNode
        from ...Original.Logic.or_node import OrNode
        from ...Original.Logic.not_node import NotNode
        if op == "not":
            n = NotNode()
            self.attach_node(n)
            self.get() >> n.get_input("值")
            return n.get_output("值")
        elif op == "and":
            n = AndNode()
            self.attach_node(n)
            self.get() >> n.get_input("A")
            to_port(other) >> n.get_input("B")
            return n.get_output("结果")
        elif op == "or":
            n = OrNode()
            self.attach_node(n)
            self.get() >> n.get_input("A")
            to_port(other) >> n.get_input("B")
            return n.get_output("结果")
        else:
            raise NotImplementedError(f"Logic op {op} not supported")
