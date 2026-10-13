"""
Mathematical constants used in visual scripting calculations.
"""

from typing import Final
import math

PI: Final[float] = math.pi
"""The mathematical constant π (3.141592653589793)."""

HALF_PI: Final[float] = math.pi / 2.0
"""Half value of π (π / 2)."""

TWO_PI: Final[float] = math.pi * 2.0
"""2 * π (6.283185307179586)."""

TAU: Final[float] = math.tau
"""The mathematical constant τ, representing the ratio of a circle's circumference to its radius (2π)."""

E: Final[float] = math.e
"""The mathematical constant e, representing the base of the natural logarithm (2.718281828459045)."""

SQRT2: Final[float] = math.sqrt(2.0)
"""The square root of 2 (1.4142135623730951)."""

DEG2RAD: Final[float] = math.pi / 180.0
"""Degrees to radians conversion multiplier (π / 180)."""

RAD2DEG: Final[float] = 180.0 / math.pi
"""Radians to degrees conversion multiplier (180 / π)."""

EPSILON: Final[float] = 1e-6
"""A small floating-point value threshold for numerical stability."""

INFINITY: Final[float] = float("inf")
"""Positive infinity."""

NEGATIVE_INFINITY: Final[float] = float("-inf")
"""Negative infinity."""

__all__ = [
    "PI",
    "HALF_PI",
    "TWO_PI",
    "TAU",
    "E",
    "SQRT2",
    "DEG2RAD",
    "RAD2DEG",
    "EPSILON",
    "INFINITY",
    "NEGATIVE_INFINITY",
]
