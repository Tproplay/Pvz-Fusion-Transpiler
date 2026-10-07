"""
Abstract extension and composite node architecture for PvzRH visual scripts.
Bridges low-level Unity Node instances with high-level Pythonic operator overloading,
implementing IEquatable and IComparable interfaces.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Tuple, Union

from ..Original.Node import Node, Port, PortType, PortDirection
from .interfaces import IEquatable, IComparable, IArithmetic, ILogical


class ExtensionNode(ABC, IEquatable, IComparable, IArithmetic, ILogical):
    """Abstract base class for all extension, wrapper, and combined nodes.
    
    Provides high-level abstraction over one or more low-level Node primitives,
    managing port delegation, expression graphs, and interface compliance.
    """

    def __init__(self, root_node: Optional[Node] = None) -> None:
        self._nodes: List[Node] = []
        if root_node:
            self._nodes.append(root_node)

    # =========================================================================
    # COMPOSITION & NODE MANAGEMENT
    # =========================================================================

    @property
    def nodes(self) -> List[Node]:
        """Returns all underlying low-level Node instances managed by this composite."""
        return list(self._nodes)

    def attach_node(self, node: Node) -> Node:
        """Registers an additional internal node into this composite's graph."""
        if node not in self._nodes:
            self._nodes.append(node)
        return node

    @property
    def root_node(self) -> Optional[Node]:
        """Returns the primary or root node of this composite."""
        return self._nodes[0] if self._nodes else None

    @abstractmethod
    def get_primary_port(self) -> Optional[Port]:
        """Returns the primary data or flow port representing this node's value or signal."""
        pass

    @property
    def primary_port(self) -> Optional[Port]:
        return self.get_primary_port()

    # =========================================================================
    # HELPER RESOLUTION
    # =========================================================================

    @staticmethod
    def resolve_port(target: Any) -> Optional[Port]:
        """Extracts the underlying low-level Port from an ExtensionNode, Port, or wrapped object."""
        if isinstance(target, Port):
            return target
        if isinstance(target, ExtensionNode):
            return target.get_primary_port()
        if hasattr(target, "primary_port"):
            return target.primary_port
        if hasattr(target, "port"):
            return target.port
        return None

    # =========================================================================
    # IEQUATABLE IMPLEMENTATION
    # =========================================================================

    def __eq__(self, other: Any) -> Any:
        """Equality comparison (==) emitting the appropriate comparison expression."""
        return self._create_comparison_node("eq", other)

    def __ne__(self, other: Any) -> Any:
        """Inequality comparison (!=) emitting the appropriate comparison expression."""
        return self._create_comparison_node("ne", other)

    def equals(self, other: Any) -> Any:
        return self.__eq__(other)

    # =========================================================================
    # ICOMPARABLE IMPLEMENTATION
    # =========================================================================

    def __lt__(self, other: Any) -> Any:
        return self._create_comparison_node("lt", other)

    def __le__(self, other: Any) -> Any:
        return self._create_comparison_node("le", other)

    def __gt__(self, other: Any) -> Any:
        return self._create_comparison_node("gt", other)

    def __ge__(self, other: Any) -> Any:
        return self._create_comparison_node("ge", other)

    def compare_to(self, other: Any) -> Any:
        """Emits a general comparison node."""
        return self._create_comparison_node("compare", other)

    # =========================================================================
    # IARITHMETIC IMPLEMENTATION
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
    # ILOGICAL IMPLEMENTATION
    # =========================================================================

    def __and__(self, other: Any) -> Any:
        return self._create_logical_op_node("and", other)

    def __or__(self, other: Any) -> Any:
        return self._create_logical_op_node("or", other)

    def __invert__(self) -> Any:
        return self._create_logical_op_node("not", None)

    # =========================================================================
    # EXTENSION DISPATCH HOOKS (Can be overridden by specialized subclasses)
    # =========================================================================

    def _create_comparison_node(self, op: str, other: Any) -> Any:
        """Hook for compiling relational comparison nodes (CompareInt, CompareFloat, etc.)."""
        raise NotImplementedError(
            f"Comparison operation '{op}' is not implemented for {self.__class__.__name__}."
        )

    def _create_binary_op_node(self, op: str, other: Any, reverse: bool = False) -> Any:
        """Hook for compiling arithmetic operation nodes (Add, Multiply, etc.)."""
        raise NotImplementedError(
            f"Arithmetic operation '{op}' is not implemented for {self.__class__.__name__}."
        )

    def _create_logical_op_node(self, op: str, other: Any) -> Any:
        """Hook for compiling logical operation nodes (And, Or, Not)."""
        raise NotImplementedError(
            f"Logical operation '{op}' is not implemented for {self.__class__.__name__}."
        )

    def __repr__(self) -> str:
        primary = self.primary_port
        port_info = f" primary_port={primary.name}" if primary else ""
        return f"<{self.__class__.__name__} [{len(self._nodes)} inner nodes]{port_info}>"

