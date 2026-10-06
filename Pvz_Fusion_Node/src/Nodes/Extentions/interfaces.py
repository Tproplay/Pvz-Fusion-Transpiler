"""
Core interfaces for visual script node expressions and high-level extensions.
Provides formal protocols for equality, ordering, arithmetic, and logical operations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class IEquatable(Protocol):
    """Interface for nodes or expressions that support equality checks (==, !=).
    
    In the visual scripting DSL, evaluating equality typically produces a
    conditional boolean port (e.g. CompareIntNode, CompareFloatNode) rather
    than an immediate Python boolean.
    """

    @abstractmethod
    def __eq__(self, other: Any) -> Any:
        """Emits an equality comparison node graph."""
        ...

    @abstractmethod
    def __ne__(self, other: Any) -> Any:
        """Emits an inequality comparison node graph."""
        ...

    def equals(self, other: Any) -> Any:
        """Explicit method call alias for __eq__."""
        return self.__eq__(other)


@runtime_checkable
class IComparable(Protocol):
    """Interface for nodes or expressions that support relational ordering (<, <=, >, >=).
    
    Translates relational comparisons into graph comparison nodes.
    """

    @abstractmethod
    def __lt__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __le__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __gt__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __ge__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def compare_to(self, other: Any) -> Any:
        """Returns a comparison result port or integer indicator."""
        ...


@runtime_checkable
class IArithmetic(Protocol):
    """Interface for numeric nodes supporting mathematical operators (+, -, *, /, %)."""

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __sub__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __mul__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __truediv__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __mod__(self, other: Any) -> Any:
        ...


@runtime_checkable
class ILogical(Protocol):
    """Interface for boolean condition nodes supporting boolean algebra (&, |, ~)."""

    @abstractmethod
    def __and__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __or__(self, other: Any) -> Any:
        ...

    @abstractmethod
    def __invert__(self) -> Any:
        ...

