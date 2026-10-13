"""
High-level IntVar combining IntVariableAsset, IntVariableNode, GetIntVariableValueNode, and SetIntVariableValueNode.
Inherits from VariableExtension.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection, to_port
from .variable_extension import VariableExtension
from ...Original.Variables.Integer.int_variable_asset import IntVariableAsset
from ...Original.Variables.Integer.int_variable_node import IntVariableNode
from ...Original.Variables.Integer.get_int_variable_value_node import GetIntVariableValueNode
from ...Original.Variables.Integer.set_int_variable_value_node import SetIntVariableValueNode
from ...Original.Variables.Integer.int_variable_arithmetic_node import IntVariableArithmeticNode
from ...Original.Constants.int_value_node import IntValueNode
from ...Original.Calculate.int_add_node import IntAddNode
from ...Original.Calculate.int_subtract_node import IntSubtractNode
from ...Original.Calculate.int_multiply_node import IntMultiplyNode
from ...Original.Calculate.int_divide_node import IntDivideNode
from ...Original.Calculate.int_modulo_node import IntModuloNode


class IntVar(VariableExtension):
    """Unified high-level Integer Variable register and expression."""

    def __init__(
        self,
        name: str = "整数",
        start_val: int = 0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        asset = IntVariableAsset(
            name=name,
            initial_value=int(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        super().__init__(name=name, asset=asset)

        # 1. Canvas Variable Definition Node
        self.var_node = IntVariableNode(
            var_name=name,
            initial_value=int(start_val),
            asset=self._asset,
        )
        self.attach_node(self.var_node)

        # 2. Canvas Getter Node wired to Variable Definition
        self._get_node = GetIntVariableValueNode()
        self.attach_node(self._get_node)
        self.var_node.get_output("变量") >> self._get_node.get_input("变量")

    def get(self) -> Port:
        """Returns the output Port of the Get node containing the runtime integer value."""
        return self._get_node.get_output("值")

    def set(self, value: Union[int, Port, Node, Any]) -> SetIntVariableValueNode:
        """Emits a SetIntVariableValueNode to mutate this variable on the active execution timeline."""
        set_node = SetIntVariableValueNode()
        self.attach_node(set_node)
        self.var_node.get_output("变量") >> set_node.get_input("变量")
        val_port = to_port(value)
        val_port >> set_node.get_input("新值")
        return set_node

    # In-place arithmetic assignment (+=, -=, *=, //=, %=)
    def __iadd__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=0)  # Add
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __isub__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=1)  # Subtract
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __imul__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=2)  # Multiply
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __ifloordiv__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=3)  # Divide
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def __imod__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=4)  # Modulo
        self.attach_node(arith)
        self.var_node.get_output("变量") >> arith.get_input("变量")
        to_port(other) >> arith.get_input("操作数")
        return self

    def _create_binary_op_node(self, op: str, other: Any, reverse: bool = False) -> Any:
        if op == "add":
            n = IntAddNode()
        elif op == "sub":
            n = IntSubtractNode()
        elif op == "mul":
            n = IntMultiplyNode()
        elif op == "div":
            n = IntDivideNode()
        elif op == "mod":
            n = IntModuloNode()
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
        from ...Original.Comparison.compare_int_node import CompareIntNode
        cmp_node = CompareIntNode()
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
