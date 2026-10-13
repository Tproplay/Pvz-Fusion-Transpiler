"""
Trigonometric functions, angular conversions, and arc functions for visual scripting.
"""

from __future__ import annotations
import math
from typing import Any

from .constants import PI, HALF_PI, TWO_PI, DEG2RAD, RAD2DEG
from .powers import sqrt
from .arithmetic import _ensure_float_port
from ... import nodes
from ...node_base import PortReference
from ...Nodes.Extentions.extensions import FloatVar, If


def rad2deg(rad: Any) -> Any:
    """Converts radians to degrees (rad * 180 / PI)."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return raw_val * RAD2DEG

    return nodes.multiply_node(a=raw_val, b=RAD2DEG).result


def deg2rad(deg: Any) -> Any:
    """Converts degrees to radians (deg * PI / 180)."""
    raw_val = _ensure_float_port(deg)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return raw_val * DEG2RAD

    return nodes.multiply_node(a=raw_val, b=DEG2RAD).result


def normalize_angle_360(angle: Any) -> Any:
    """Wraps any angle in degrees to the range [0.0, 360.0)."""
    raw_val = _ensure_float_port(angle)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return raw_val % 360.0

    return PortReference._float_modulo(raw_val, 360.0)


def normalize_angle_180(angle: Any) -> Any:
    """Wraps any angle in degrees to the range [-180.0, 180.0).
    Calculates: ((angle + 180) % 360) - 180
    """
    raw_val = _ensure_float_port(angle)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return ((raw_val + 180.0) % 360.0) - 180.0

    add_180 = nodes.add_node(a=raw_val, b=180.0).result
    mod_360 = PortReference._float_modulo(add_180, 360.0)
    return nodes.subtract_node(a=mod_360, b=180.0).result


def delta_angle(current: Any, target: Any) -> Any:
    """Calculates the shortest difference between two angles in degrees [-180.0, 180.0]."""
    raw_curr = _ensure_float_port(current)
    raw_targ = _ensure_float_port(target)

    is_curr_static = isinstance(raw_curr, (int, float)) and not isinstance(raw_curr, PortReference) and not hasattr(raw_curr, "node")
    is_targ_static = isinstance(raw_targ, (int, float)) and not isinstance(raw_targ, PortReference) and not hasattr(raw_targ, "node")

    if is_curr_static and is_targ_static:
        return normalize_angle_180(raw_targ - raw_curr)

    diff = raw_targ - raw_curr
    return normalize_angle_180(diff)


def lerp_angle(a: Any, b: Any, t: Any) -> Any:
    """Linearly interpolates between two angles in degrees taking the shortest path."""
    delta = delta_angle(a, b)
    return a + (delta * t)


def _wrap_rad(rad: Any) -> Any:
    """Wraps radians into the range [-PI, PI] for optimal Taylor series convergence."""
    if isinstance(rad, (int, float)) and not isinstance(rad, PortReference) and not hasattr(rad, "node"):
        return ((rad + math.pi) % (2.0 * math.pi)) - math.pi

    add_pi = nodes.add_node(a=rad, b=PI).result
    mod_2pi = PortReference._float_modulo(add_pi, TWO_PI)
    return nodes.subtract_node(a=mod_2pi, b=PI).result


def sin(rad: Any, terms: int = 5) -> Any:
    """Calculates sine (in radians) with range reduction and Taylor series."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.sin(raw_val)

    wrapped = _wrap_rad(raw_val)
    result = wrapped
    x_power = wrapped
    sign_val = -1.0

    for n in range(3, 3 + (terms - 1) * 2, 2):
        x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        fact = float(math.factorial(n))
        term = nodes.divide_node(a=x_power, b=fact).result
        term_scaled = nodes.multiply_node(a=term, b=sign_val).result

        result = nodes.add_node(a=result, b=term_scaled).result
        sign_val *= -1.0

    return result


def cos(rad: Any, terms: int = 5) -> Any:
    """Calculates cosine (in radians) with range reduction and Taylor series."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.cos(raw_val)

    wrapped = _wrap_rad(raw_val)
    result = nodes.float_value(val=1.0).value
    x_power = nodes.float_value(val=1.0).value
    sign_val = -1.0

    for n in range(2, 2 + terms * 2, 2):
        x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        fact = float(math.factorial(n))
        term = nodes.divide_node(a=x_power, b=fact).result
        term_scaled = nodes.multiply_node(a=term, b=sign_val).result

        result = nodes.add_node(a=result, b=term_scaled).result
        sign_val *= -1.0

    return result


def sincos(rad: Any, terms: int = 5) -> tuple[Any, Any]:
    """Calculates both sine and cosine simultaneously, returning (sin, cos)."""
    return sin(rad, terms=terms), cos(rad, terms=terms)


def tan(rad: Any, terms: int = 5) -> Any:
    """Calculates tangent (sin / cos)."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.tan(raw_val)

    s = sin(raw_val, terms=terms)
    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=s, b=c).result


def cosec(rad: Any, terms: int = 5) -> Any:
    """Calculates cosecant (1 / sin)."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return 1.0 / math.sin(raw_val)

    s = sin(raw_val, terms=terms)
    return nodes.divide_node(a=1.0, b=s).result


def sec(rad: Any, terms: int = 5) -> Any:
    """Calculates secant (1 / cos)."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return 1.0 / math.cos(raw_val)

    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=1.0, b=c).result


def cot(rad: Any, terms: int = 5) -> Any:
    """Calculates cotangent (cos / sin)."""
    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return 1.0 / math.tan(raw_val)

    s = sin(raw_val, terms=terms)
    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=c, b=s).result


def asin(val: Any, terms: int = 5) -> Any:
    """Calculates arcsine in radians [-pi/2, pi/2]. Input domain [-1, 1]."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.asin(raw_val)

    result = raw_val
    x_power = raw_val

    for n in range(1, terms):
        two_n = 2 * n
        x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        coeff = float(math.factorial(two_n)) / (
            (4.0**n) * (math.factorial(n) ** 2) * (two_n + 1)
        )
        term = nodes.multiply_node(a=x_power, b=coeff).result
        result = nodes.add_node(a=result, b=term).result

    return result


def acos(val: Any, terms: int = 5) -> Any:
    """Calculates arccosine in radians [0, pi] via (pi/2 - asin(val))."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.acos(raw_val)

    asin_val = asin(raw_val, terms=terms)
    return nodes.subtract_node(a=HALF_PI, b=asin_val).result


def atan(val: Any, terms: int = 5) -> Any:
    """Calculates arctangent in radians [-pi/2, pi/2]."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.atan(raw_val)

    # Stabilize domain via atan(x) = asin(x / sqrt(1 + x^2))
    x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
    one_plus_x_sq = nodes.add_node(a=1.0, b=x_sq).result
    denom = sqrt(one_plus_x_sq)
    ratio = nodes.divide_node(a=raw_val, b=denom).result

    return asin(ratio, terms=terms)


def atan2(y: Any, x: Any, terms: int = 5) -> Any:
    """Calculates the angle in radians of vector (x, y) with quadrant correction [-pi, pi]."""
    raw_y = y.value if hasattr(y, "value") else y
    raw_x = x.value if hasattr(x, "value") else x

    if (
        isinstance(raw_y, (int, float))
        and isinstance(raw_x, (int, float))
        and not hasattr(raw_y, "node")
        and not hasattr(raw_x, "node")
        and not isinstance(raw_y, PortReference)
        and not isinstance(raw_x, PortReference)
    ):
        return math.atan2(raw_y, raw_x)

    res = FloatVar("atan2_res", 0.0)

    with If(x > 0):
        res.set(atan(y / x, terms=terms))
    with If((x < 0) & (y >= 0)):
        res.set(atan(y / x, terms=terms) + PI)
    with If((x < 0) & (y < 0)):
        res.set(atan(y / x, terms=terms) - PI)
    with If((x == 0) & (y > 0)):
        res.set(HALF_PI)
    with If((x == 0) & (y < 0)):
        res.set(-HALF_PI)

    return res.value


def acosec(val: Any, terms: int = 5) -> Any:
    """Calculates arccosecant in radians (asin(1 / val))."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.asin(1.0 / raw_val)

    reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
    return asin(reciprocal, terms=terms)


def asec(val: Any, terms: int = 5) -> Any:
    """Calculates arcsecant in radians (acos(1 / val))."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.acos(1.0 / raw_val)

    reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
    return acos(reciprocal, terms=terms)


def acot(val: Any, terms: int = 5) -> Any:
    """Calculates arccotangent in radians (pi/2 - atan(val))."""
    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node"):
        return math.atan(1.0 / raw_val)

    atan_val = atan(raw_val, terms=terms)
    return nodes.subtract_node(a=HALF_PI, b=atan_val).result


__all__ = [
    "rad2deg",
    "deg2rad",
    "normalize_angle_360",
    "normalize_angle_180",
    "delta_angle",
    "lerp_angle",
    "sin",
    "cos",
    "sincos",
    "tan",
    "cosec",
    "sec",
    "cot",
    "asin",
    "acos",
    "atan",
    "atan2",
    "acosec",
    "asec",
    "acot",
]
