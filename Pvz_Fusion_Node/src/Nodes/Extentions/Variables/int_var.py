"""
High-level IntVar combining IntVariableAsset, GetIntVariableValueNode, and SetIntVariableValueNode.
Implements IEquatable, IComparable, and IArithmetic.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection
from ..extension_node import ExtensionNode
from ...Original.Variables.Integer.int_variable_asset import IntVariableAsset
from ...Original.Variables.Integer.get_int_variable_value_node import GetIntVariableValueNode
from ...Original.Variables.Integer.set_int_variable_value_node import SetIntVariableValueNode
from ...Original.Variables.Integer.int_variable_arithmetic_node import IntVariableArithmeticNode
from ...Original.Constants.int_value_node import IntValueNode
from ...Original.Calculate.int_add_node import IntAddNode
from ...Original.Calculate.int_subtract_node import IntSubtractNode
from ...Original.Calculate.int_multiply_node import IntMultiplyNode
from ...Original.Calculate.int_divide_node import IntDivideNode
from ...Original.Calculate.int_modulo_node import IntModuloNode


class IntVar(ExtensionNode):
    """Unified high-level Integer Variable register and expression."""

    def __init__(
        self,
        name: str = "整数",
        start_val: int = 0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__()
        self.asset = IntVariableAsset(
            name=name,
            initial_value=int(start_val),
            variable_id=variable_id,
            rid=rid,
        )
        self._get_node = GetIntVariableValueNode()
        self.attach_node(self._get_node)

    @property
    def name(self) -> str:
        return self.asset.name

    def get(self) -> Port:
        """Returns the output Port of the Get node containing the runtime integer value."""
        return self._get_node.get_output("值")

    def set(self, value: Union[int, Port, ExtensionNode]) -> SetIntVariableValueNode:
        """Emits a SetIntVariableValueNode to mutate this variable on the active execution timeline."""
        set_node = SetIntVariableValueNode()
        self.attach_node(set_node)
        return set_node

    def get_primary_port(self) -> Port:
        return self.get()

    @property
    def value(self) -> Port:
        return self.get()

    # In-place arithmetic assignment (+=, -=, *=, /=, %=)
    def __iadd__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=0) # Add
        self.attach_node(arith)
        return self

    def __isub__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=1) # Subtract
        self.attach_node(arith)
        return self

    def __imul__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=2) # Multiply
        self.attach_node(arith)
        return self

    def __ifloordiv__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=3) # Divide
        self.attach_node(arith)
        return self

    def __imod__(self, other: Any) -> IntVar:
        arith = IntVariableArithmeticNode(operation=4) # Modulo
        self.attach_node(arith)
        return self

    def _create_binary_op_node(self, op: str, other: Any, reverse: bool = False) -> Any:
        p_self = self.get_primary_port()
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
        return n

    def _create_comparison_node(self, op: str, other: Any) -> Any:
        from ...Original.Calculate.compare_int_node import CompareIntNode
        cmp_node = CompareIntNode()
        self.attach_node(cmp_node)
        return cmp_node
