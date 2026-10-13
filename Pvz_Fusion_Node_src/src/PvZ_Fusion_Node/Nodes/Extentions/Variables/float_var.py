"""
High-level FloatVar combining FloatVariableAsset, FloatVariableNode, GetFloatVariableValueNode, and SetFloatVariableValueNode.
Inherits from VariableExtension.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection, to_port
from .variable_extension import VariableExtension
from ...Original.Variables.Float.float_variable_asset import FloatVariableAsset
from ...Original.Variables.Float.float_variable_node import FloatVariableNode
from ...Original.Variables.Float.get_float_variable_value_node import GetFloatVariableValueNode
from ...Original.Variables.Float.set_float_variable_value_node import SetFloatVariableValueNode
from ...Original.Variables.Float.float_variable_arithmetic_node import FloatVariableArithmeticNode
from ...Original.Constants.float_value_node import FloatValueNode
from ...Original.Calculate.add_node import AddNode
from ...Original.Calculate.subtract_node import SubtractNode
from ...Original.Calculate.multiply_node import MultiplyNode
from ...Original.Calculate.divide_node import DivideNode


class FloatVar(VariableExtension):
    """Unified high-level Float Variable register and expression."""

    def __init__(
        self,
        name: str = "浮点数",
        start_val: float = 0.0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        asset = FloatVariableAsset(
            name=name,
            initial_value=float(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        super().__init__(name=name, asset=asset)

        # 1. Canvas Variable Definition Node
        self.var_node = FloatVariableNode(
            var_name=name,
            initial_value=float(start_val),
            asset=self._asset,
        )
        self.attach_node(self.var_node)

        # 2. Canvas Getter Node wired to Variable Definition
        self._get_node = GetFloatVariableValueNode()
        self.attach_node(self._get_node)
        self.var_node.get_output("变量") >> self._get_node.get_input("变量")

    def get(self) -> Port:
        return self._get_node.get_output("值")

    def set(self, value: Union[float, Port, Node, Any]) -> SetFloatVariableValueNode:
        set_node = SetFloatVariableValueNode()
        self.attach_node(set_node)
        self.var_node.get_output("变量") >> set_node.get_input("变量")
        val_port = to_port(value)
        val_port >> set_node.get_input("新值")
        return set_node

    def __iadd__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=0)
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __isub__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=1)
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __imul__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=2)
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __itruediv__(self, other: Any) -> FloatVar:
        arith = FloatVariableArithmeticNode(operation=3)
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
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
        if reverse:
            to_port(other) >> n.get_input("A")
            self.get() >> n.get_input("B")
        else:
            self.get() >> n.get_input("A")
            to_port(other) >> n.get_input("B")
        return n

    def _create_comparison_node(self, op: str, other: Any) -> Any:
        from ...Original.Comparison.compare_float_node import CompareFloatNode
        cmp_node = CompareFloatNode()
        self.attach_node(cmp_node)
        self.get() >> cmp_node.get_input("A")
        to_port(other) >> cmp_node.get_input("B")
        if op in ("eq", "=="):
            return cmp_node.get_output("等于")
        elif op in ("lt", "<"):
            return cmp_node.get_output("小于")
        elif op in ("gt", ">"):
            return cmp_node.get_output("大于")
        elif op in ("le", "<="):
            from ...Original.Logic.not_node import NotNode
            not_node = NotNode()
            self.attach_node(not_node)
            cmp_node.get_output("大于") >> not_node.get_input("值")
            return not_node.get_output("值")
        elif op in ("ge", ">="):
            from ...Original.Logic.not_node import NotNode
            not_node = NotNode()
            self.attach_node(not_node)
            cmp_node.get_output("小于") >> not_node.get_input("值")
            return not_node.get_output("值")
        elif op in ("ne", "!="):
            from ...Original.Logic.not_node import NotNode
            not_node = NotNode()
            self.attach_node(not_node)
            cmp_node.get_output("等于") >> not_node.get_input("值")
            return not_node.get_output("值")
        return cmp_node
