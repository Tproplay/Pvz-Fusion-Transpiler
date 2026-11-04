"""
Core interfaces and protocols for visual script composite extensions.
"""

from __future__ import annotations

from typing import Any, Optional, Protocol, Union, runtime_checkable


@runtime_checkable
class IEquatable(Protocol):
    """Protocol for nodes/expressions supporting equality checks (==, !=)."""

    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...


@runtime_checkable
class IComparable(Protocol):
    """Protocol for nodes/expressions supporting ordering comparisons (<, <=, >, >=)."""

    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...


@runtime_checkable
class IArithmetic(Protocol):
    """Protocol for numeric nodes supporting mathematical operators (+, -, *, /, %)."""

    def __add__(self, other: Any) -> Any: ...
    def __sub__(self, other: Any) -> Any: ...
    def __mul__(self, other: Any) -> Any: ...
    def __truediv__(self, other: Any) -> Any: ...
    def __mod__(self, other: Any) -> Any: ...


@runtime_checkable
class ILogical(Protocol):
    """Protocol for condition nodes supporting boolean algebra (&, |, ~)."""

    def __and__(self, other: Any) -> Any: ...
    def __or__(self, other: Any) -> Any: ...
    def __invert__(self) -> Any: ...


@runtime_checkable
class IVariable(Protocol):
    """Protocol for persistent canvas variables and state containers."""

    @property
    def value(self) -> Any: ...
    def set(self, value: Any) -> Any: ...


__all__ = [
    "IEquatable",
    "IComparable",
    "IArithmetic",
    "ILogical",
    "IVariable",
]
