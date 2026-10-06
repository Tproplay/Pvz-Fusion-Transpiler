"""
High-level FloatVar combining FloatVariableAsset, GetFloatVariableValueNode, and SetFloatVariableValueNode.
Implements IEquatable, IComparable, and IArithmetic.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection
from ..extension_node import ExtensionNode
from ...Original.Variables.Float.float_variable_asset import FloatVariableAsset
from ...Original.Variables.Float.get_float_variable_value_node import GetFloatVariableValueNode
from ...Original.Variables.Float.set_float_variable_value_node import SetFloatVariableValueNode
from ...Original.Variables.Float.float_variable_arithmetic_node import FloatVariableArithmeticNode
from ...Original.Constants.float_value_node import FloatValueNode
from ...Original.Calculate.add_node import AddNode
from ...Original.Calculate.subtract_node import SubtractNode
from ...Original.Calculate.multiply_node import MultiplyNode
from ...Original.Calculate.divide_node import DivideNode


class FloatVar(ExtensionNode):
    """Unified high-level Float Variable register and expression."""

    def __init__(
        self,
        name: str = "浮点数",
        start_val: float = 0.0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__()
        self.asset = FloatVariableAsset(
            name=name,
            initial_value=float(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        self._get_node = GetFloatVariableValueNode()
        self.attach_node(self._get_node)

    @property
    def name(self) -> str:
        return self.asset.name

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[float, Port, ExtensionNode]) -> SetFloatVariableValueNode:
        set_node = SetFloatVariableValueNode()
        self.attach_node(set_node)
        return set_node

    def get_primary_port(self) -> Port:
        return self.get()

    @property
    def value(self) -> Port:
        return self.get()

    def __iadd__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=0)
        self.attach_node(arith)
        return self

    def __isub__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=1)
        self.attach_node(arith)
        return self

    def __imul__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=2)
        self.attach_node(arith)
        return self

    def __itruediv__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=3)
        self.attach_node(arith)
        return self

    def _create_binary_op_node(self, op: str, other: Any, reverse: bool = False) -> Any:
        if op == "add":
            n = AddNode()
        elif op == "sub":
            n = SubtractNode()
        elif op == "mul":
            n = MultiplyNode()
        elif op == "div":
            n = DivideNode()
        else:
            raise NotImplementedError(f"Operation {op} not supported")
        self.attach_node(n)
        return n

    def _create_comparison_node(self, op: str, other: Any) -> Any:
        from ....Original.Calculate.compare_float_node import CompareFloatNode
        cmp_node = CompareFloatNode()
        self.attach_node(cmp_node)
        return cmp_node
