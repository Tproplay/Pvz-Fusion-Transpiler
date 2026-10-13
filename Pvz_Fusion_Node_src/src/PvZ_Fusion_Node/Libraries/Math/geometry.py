"""
2D Geometric vectors, transformations, and coordinate helpers.
"""

from __future__ import annotations
from typing import Any

from .powers import sqrt
from .trigonometry import rad2deg, atan2


class Vector2:
    """A 2D Vector structure supporting physical node canvas and static calculations."""

    def __init__(self, x: Any = 0.0, y: Any = 0.0):
        self.x = x.value if hasattr(x, "value") and not hasattr(x, "_is_float_port") else x
        self.y = y.value if hasattr(y, "value") and not hasattr(y, "_is_float_port") else y

    # Static Factories
    @classmethod
    def zero(cls) -> Vector2:
        return cls(0.0, 0.0)

    @classmethod
    def one(cls) -> Vector2:
        return cls(1.0, 1.0)

    @classmethod
    def up(cls) -> Vector2:
        return cls(0.0, 1.0)

    @classmethod
    def down(cls) -> Vector2:
        return cls(0.0, -1.0)

    @classmethod
    def left(cls) -> Vector2:
        return cls(-1.0, 0.0)

    @classmethod
    def right(cls) -> Vector2:
        return cls(1.0, 0.0)

    # Vector Mathematics
    def sqr_magnitude(self) -> Any:
        """Returns squared length of the vector (x^2 + y^2)."""
        return (self.x * self.x) + (self.y * self.y)

    def magnitude(self) -> Any:
        """Returns length/magnitude of the vector."""
        return sqrt(self.sqr_magnitude())

    def normalized(self) -> Vector2:
        """Returns a normalized vector of length 1."""
        mag = self.magnitude()
        return self / mag

    @staticmethod
    def dot(v1: Vector2, v2: Vector2) -> Any:
        """Calculates dot product of two vectors (v1.x * v2.x + v1.y * v2.y)."""
        return (v1.x * v2.x) + (v1.y * v2.y)

    @staticmethod
    def cross(v1: Vector2, v2: Vector2) -> Any:
        """Calculates 2D cross product scalar (v1.x * v2.y - v1.y * v2.x)."""
        return (v1.x * v2.y) - (v1.y * v2.x)

    @staticmethod
    def distance(v1: Vector2, v2: Vector2) -> Any:
        """Calculates Euclidean distance between two vectors."""
        return (v1 - v2).magnitude()

    @staticmethod
    def lerp(v1: Vector2, v2: Vector2, t: Any) -> Vector2:
        """Linearly interpolates between vector v1 and vector v2 by t [0, 1]."""
        return v1 + (v2 - v1) * t

    @staticmethod
    def reflect(in_direction: Vector2, in_normal: Vector2) -> Vector2:
        """Reflects a vector off a plane defined by a normal."""
        factor = Vector2.dot(in_direction, in_normal) * 2.0
        return in_direction - (in_normal * factor)

    @staticmethod
    def angle(from_v: Vector2, to_v: Vector2) -> Any:
        """Returns unsigned angle in degrees between from_v and to_v."""
        denominator = sqrt(from_v.sqr_magnitude() * to_v.sqr_magnitude())
        from .trigonometry import acos, rad2deg
        from .arithmetic import clamp
        dot_div = Vector2.dot(from_v, to_v) / denominator
        return rad2deg(acos(clamp(dot_div, -1.0, 1.0)))

    # Formatting Integration
    def to_string(self) -> Any:
        """Formats the vector as '(x, y)' using StringConcatNodes."""
        from ..StdLib.formatting import format_string
        return format_string("(", self.x, ", ", self.y, ")")

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    # Operator Overloading (+, -, *, /, ==, -v)
    def __add__(self, other: Any) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __radd__(self, other: Any) -> Vector2:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __rsub__(self, other: Any) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(other.x - self.x, other.y - self.y)
        return Vector2(other - self.x, other - self.y)

    def __mul__(self, other: Any) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other: Any) -> Vector2:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def __neg__(self) -> Vector2:
        return Vector2(-self.x, -self.y)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, Vector2):
            return (self.x == other.x) & (self.y == other.y)
        return False


# Standalone Vector helper functions
def distance(v1: Vector2, v2: Vector2) -> Any:
    return Vector2.distance(v1, v2)


def dot(v1: Vector2, v2: Vector2) -> Any:
    return Vector2.dot(v1, v2)


def cross(v1: Vector2, v2: Vector2) -> Any:
    return Vector2.cross(v1, v2)


def reflect(in_direction: Vector2, in_normal: Vector2) -> Vector2:
    return Vector2.reflect(in_direction, in_normal)


__all__ = [
    "Vector2",
    "distance",
    "dot",
    "cross",
    "reflect",
]
