"""
Base class for all reactive canvas variables (IntVar, FloatVar, BoolVar, StrVar, ListVar).
Inherits from ExtensionNode and adds persistent VariableAsset binding, getter/setter
abstractions, and operator overloading.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Optional, Union

from ..extension_node import ExtensionNode
from ..interfaces import (
    IArithmetic,
    IComparable,
    IEquatable,
    ILogical,
    IVariable,
)

from ...Original.Node import Node, Port
from ...Original.VariableAsset import VariableAsset


class VariableExtension(
    ExtensionNode,
    IVariable,
    IEquatable,
    IComparable,
    IArithmetic,
    ILogical,
):
    """Abstract base class for all persistent canvas variables.

    Pairs an in-memory VariableAsset with active Getter and Setter nodes,
    exposing intuitive Python operators that emit arithmetic/comparison subgraphs.
    """

    def __init__(self, name: str, asset: VariableAsset) -> None:
        super().__init__()
        self._name = name
        self._asset = asset

    @property
    def name(self) -> str:
        return self._name

    @property
    def asset(self) -> VariableAsset:
        return self._asset

    @property
    def variable_id(self) -> str:
        return self._asset.variable_id

    # =========================================================================
    # ABSTRACT GETTER & SETTER FACTORIES
    # =========================================================================

    @abstractmethod
    def get(self) -> Port:
        """Returns the primary active getter node output port for this variable."""
        pass

    @abstractmethod
    def set(self, value: Any) -> Node:
        """Emits a setter node assigning value to this variable."""
        pass

    def get_primary_port(self) -> Optional[Port]:
        """By default, returns the output port of the getter."""
        return self.get()

    @property
    def value(self) -> Port:
        """Alias for get()."""
        return self.get()

    # =========================================================================
    # EQUALITY & COMPARISON OVERLOADS
    # =========================================================================

    def __eq__(self, other: Any) -> Any:
        return self._create_comparison_node("eq", other)

    def __ne__(self, other: Any) -> Any:
        return self._create_comparison_node("ne", other)

    def equals(self, other: Any) -> Any:
        return self.__eq__(other)

    def __lt__(self, other: Any) -> Any:
        return self._create_comparison_node("lt", other)

    def __le__(self, other: Any) -> Any:
        return self._create_comparison_node("le", other)

    def __gt__(self, other: Any) -> Any:
        return self._create_comparison_node("gt", other)

    def __ge__(self, other: Any) -> Any:
        return self._create_comparison_node("ge", other)

    def compare_to(self, other: Any) -> Any:
        return self._create_comparison_node("compare", other)

    # =========================================================================
    # ARITHMETIC OPERATOR OVERLOADS
    # =========================================================================

    def __add__(self, other: Any) -> Any:
        return self._create_binary_op_node("add", other)

    def __radd__(self, other: Any) -> Any:
        return self._create_binary_op_node("add", other, reverse=True)

    def __sub__(self, other: Any) -> Any:
        return self._create_binary_op_node("sub", other)

    def __rsub__(self, other: Any) -> Any:
        return self._create_binary_op_node("sub", other, reverse=True)

    def __mul__(self, other: Any) -> Any:
        return self._create_binary_op_node("mul", other)

    def __rmul__(self, other: Any) -> Any:
        return self._create_binary_op_node("mul", other, reverse=True)

    def __truediv__(self, other: Any) -> Any:
        return self._create_binary_op_node("div", other)

    def __rtruediv__(self, other: Any) -> Any:
        return self._create_binary_op_node("div", other, reverse=True)

    def __mod__(self, other: Any) -> Any:
        return self._create_binary_op_node("mod", other)

    def __rmod__(self, other: Any) -> Any:
        return self._create_binary_op_node("mod", other, reverse=True)

    # =========================================================================
    # LOGICAL OPERATOR OVERLOADS
    # =========================================================================

    def __and__(self, other: Any) -> Any:
        return self._create_logical_op_node("and", other)

    def __or__(self, other: Any) -> Any:
        return self._create_logical_op_node("or", other)

    def __invert__(self) -> Any:
        return self._create_logical_op_node("not", None)

    # =========================================================================
    # EXTENSION DISPATCH HOOKS (Implemented by concrete typed variables)
    # =========================================================================

    def _create_comparison_node(self, op: str, other: Any) -> Any:
        raise NotImplementedError(
            f"Comparison '{op}' is not supported by {self.__class__.__name__}."
        )

    def _create_binary_op_node(self, op: str, other: Any, reverse: bool = False) -> Any:
        raise NotImplementedError(
            f"Arithmetic '{op}' is not supported by {self.__class__.__name__}."
        )

    def _create_logical_op_node(self, op: str, other: Any) -> Any:
        raise NotImplementedError(
            f"Logical '{op}' is not supported by {self.__class__.__name__}."
        )
