"""
Power, root, exponential, and logarithmic functions for visual scripting.
"""

from __future__ import annotations
import math
import builtins
from typing import Any

from .constants import E
from ... import nodes
from ...node_base import PortReference


def pow(base: Any, exp: Any) -> Any:
    """Calculates base raised to the power of exp using native PowerNode."""
    from ...Nodes.Original.Calculate.power_node import PowerNode
    from ...Nodes.Original.Node import to_port

    raw_base = base.value if hasattr(base, "value") else base
    raw_exp = exp.value if hasattr(exp, "value") else exp

    if (
        isinstance(raw_base, (int, float))
        and isinstance(raw_exp, (int, float))
        and not hasattr(raw_base, "node")
        and not hasattr(raw_exp, "node")
        and not isinstance(raw_base, PortReference)
        and not isinstance(raw_exp, PortReference)
    ):
        return builtins.pow(raw_base, raw_exp)

    node = PowerNode()
    to_port(base).connect(node.get_input(PowerNode.Base_input_float))
    to_port(exp).connect(node.get_input(PowerNode.Exponent_input_float))
    return node.get_output(PowerNode.Result_output_float)


def natural_pow(base: Any, exp: Any) -> Any:
    """Calculates base raised to an exponent using native PowerNode."""
    return pow(base, exp)


def sqrt(val: Any) -> Any:
    """Calculates the square root of val natively using PowerNode(val, 0.5)."""
    raw_val = val.value if hasattr(val, "value") else val
    if (
        isinstance(raw_val, (int, float))
        and not hasattr(raw_val, "node")
        and not isinstance(raw_val, PortReference)
    ):
        if raw_val < 0:
            raise ValueError(
                f"❌ Error: Cannot calculate square root of negative number '{raw_val}'."
            )
        return math.sqrt(raw_val)

    return pow(val, 0.5)


def cbrt(val: Any) -> Any:
    """Calculates the cube root of val natively using PowerNode(val, 1/3)."""
    raw_val = val.value if hasattr(val, "value") else val
    if (
        isinstance(raw_val, (int, float))
        and not hasattr(raw_val, "node")
        and not isinstance(raw_val, PortReference)
    ):
        return (
            math.cbrt(raw_val)
            if hasattr(math, "cbrt")
            else (raw_val ** (1 / 3) if raw_val >= 0 else -((-raw_val) ** (1 / 3)))
        )

    return pow(val, 1.0 / 3.0)


def hypot(x: Any, y: Any) -> Any:
    """Calculates Euclidean norm / hypotenuse sqrt(x*x + y*y)."""
    raw_x = x.value if hasattr(x, "value") else x
    raw_y = y.value if hasattr(y, "value") else y

    if (
        isinstance(raw_x, (int, float))
        and isinstance(raw_y, (int, float))
        and not hasattr(raw_x, "node")
        and not hasattr(raw_y, "node")
        and not isinstance(raw_x, PortReference)
        and not isinstance(raw_y, PortReference)
    ):
        return math.hypot(raw_x, raw_y)

    return sqrt(x * x + y * y)


def log(val: Any, base: Any = E) -> Any:
    """Calculates logarithm of val with base using native LogarithmNode."""
    from ...Nodes.Original.Calculate.logarithm_node import LogarithmNode
    from ...Nodes.Original.Node import to_port

    raw_val = val.value if hasattr(val, "value") else val
    raw_base = base.value if hasattr(base, "value") else base

    if (
        isinstance(raw_val, (int, float))
        and isinstance(raw_base, (int, float))
        and not hasattr(raw_val, "node")
        and not hasattr(raw_base, "node")
        and not isinstance(raw_val, PortReference)
        and not isinstance(raw_base, PortReference)
    ):
        return math.log(raw_val, raw_base)

    node = LogarithmNode()
    to_port(val).connect(node.get_input(LogarithmNode.Number_input_float))
    to_port(base).connect(node.get_input(LogarithmNode.Base_input_float))
    return node.get_output(LogarithmNode.Result_output_float)


def log2(val: Any) -> Any:
    """Calculates base-2 logarithm of val using native LogarithmNode."""
    raw_val = val.value if hasattr(val, "value") else val
    if (
        isinstance(raw_val, (int, float))
        and not hasattr(raw_val, "node")
        and not isinstance(raw_val, PortReference)
    ):
        return math.log2(raw_val)
    return log(val, 2.0)


def log10(val: Any) -> Any:
    """Calculates base-10 logarithm of val using native LogarithmNode."""
    raw_val = val.value if hasattr(val, "value") else val
    if (
        isinstance(raw_val, (int, float))
        and not hasattr(raw_val, "node")
        and not isinstance(raw_val, PortReference)
    ):
        return math.log10(raw_val)
    return log(val, 10.0)


def exp(val: Any) -> Any:
    """Calculates e raised to power val (e^val) using native PowerNode."""
    raw_val = val.value if hasattr(val, "value") else val
    if (
        isinstance(raw_val, (int, float))
        and not hasattr(raw_val, "node")
        and not isinstance(raw_val, PortReference)
    ):
        return math.exp(raw_val)
    return pow(E, val)


__all__ = [
    "pow",
    "natural_pow",
    "sqrt",
    "cbrt",
    "hypot",
    "log",
    "log2",
    "log10",
    "exp",
]
