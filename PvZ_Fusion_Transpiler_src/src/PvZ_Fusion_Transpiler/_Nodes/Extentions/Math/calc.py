from __future__ import annotations

from typing import Any
from .... import nodes


class Math:
    """Mathematical utility functions and node wrappers."""

    @staticmethod
    def pow(value: Any, exponent: Any) -> Any:
        """Calculates value raised to the exponent power."""
        return nodes.power(value=value, exponent=exponent).port_output_float_Result

    power = pow

    @staticmethod
    def log(value: Any, base: Any = 2.718281828459045) -> Any:
        """Calculates the logarithm of value with given base (default e)."""
        return nodes.logarithm(value=value, base=base).port_output_float_Result

    logarithm = log

    @staticmethod
    def greater(a: Any, b: Any) -> Any:
        """Compares if a > b (auto-detects float or int)."""
        if isinstance(a, float) or isinstance(b, float):
            return nodes.compare_float(a=a, b=b).port_output_bool_Greater
        return nodes.compare_int(a=a, b=b).port_output_bool_Greater

    @staticmethod
    def less(a: Any, b: Any) -> Any:
        """Compares if a < b (auto-detects float or int)."""
        if isinstance(a, float) or isinstance(b, float):
            return nodes.compare_float(a=a, b=b).port_output_bool_Less
        return nodes.compare_int(a=a, b=b).port_output_bool_Less

    @staticmethod
    def equal(a: Any, b: Any) -> Any:
        """Compares if a == b (auto-detects float or int)."""
        if isinstance(a, float) or isinstance(b, float):
            return nodes.compare_float(a=a, b=b).port_output_bool_Equal
        return nodes.compare_int(a=a, b=b).port_output_bool_Equal

    @staticmethod
    def same_object(a: Any, b: Any) -> Any:
        """Compares if two GameObjects are the same object."""
        return nodes.compare_game_object(a=a, b=b).port_output_bool_Same


Compare = Math

__all__ = ["Math", "Compare"]
