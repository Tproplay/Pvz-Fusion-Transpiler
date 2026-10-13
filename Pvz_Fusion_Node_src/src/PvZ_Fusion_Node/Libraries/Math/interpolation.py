"""
Interpolation, mapping, easing, and step functions for visual scripting.
"""

from __future__ import annotations
from typing import Any

from .arithmetic import clamp01, lerp, abs, sign, floor
from .trigonometry import delta_angle


def inverse_lerp(a: Any, b: Any, value: Any) -> Any:
    """Calculates the linear parameter t that produces value when interpolating between a and b.
    Returns clamp01((value - a) / (b - a)).
    """
    diff = b - a
    return clamp01((value - a) / diff)


def remap(
    in_min: Any,
    in_max: Any,
    out_min: Any,
    out_max: Any,
    value: Any,
) -> Any:
    """Remaps value from input range [in_min, in_max] to output range [out_min, out_max]."""
    t = inverse_lerp(in_min, in_max, value)
    return lerp(out_min, out_max, t)


def smoothstep(edge0: Any, edge1: Any, x: Any) -> Any:
    """Performs smooth cubic Hermite interpolation between 0 and 1 for edge0 <= x <= edge1."""
    t = clamp01((x - edge0) / (edge1 - edge0))
    return t * t * (3.0 - 2.0 * t)


def smootherstep(edge0: Any, edge1: Any, x: Any) -> Any:
    """Performs Ken Perlin's improved 5th-order smootherstep interpolation (6t^5 - 15t^4 + 10t^3)."""
    t = clamp01((x - edge0) / (edge1 - edge0))
    return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)


def pingpong(t: Any, length: Any) -> Any:
    """Bounces value t continuously between 0 and length."""
    raw_l = length.value if hasattr(length, "value") else length
    if isinstance(raw_l, (int, float)) and raw_l <= 0:
        return 0.0

    two_l = length * 2.0
    mod_val = t - floor(t / two_l) * two_l
    return length - abs(mod_val - length)


def repeat(t: Any, length: Any) -> Any:
    """Loops value t continuously between 0 and length."""
    raw_l = length.value if hasattr(length, "value") else length
    if isinstance(raw_l, (int, float)) and raw_l <= 0:
        return 0.0

    return t - floor(t / length) * length


def move_towards(current: Any, target: Any, max_delta: Any) -> Any:
    """Moves current towards target by at most max_delta without overshooting."""
    diff = target - current
    dist = abs(diff)

    from ...Nodes.Extentions.extensions import If, FloatVar
    res = FloatVar("move_towards_res", current)

    with If(dist <= max_delta):
        res.set(target)
    with If(dist > max_delta):
        res.set(current + sign(diff) * max_delta)

    return res.value


def move_towards_angle(current: Any, target: Any, max_delta: Any) -> Any:
    """Rotates angle current towards target by at most max_delta degrees without overshooting."""
    delta = delta_angle(current, target)
    from ...Nodes.Extentions.extensions import If, FloatVar
    res = FloatVar("move_angle_res", current)

    with If(abs(delta) <= max_delta):
        res.set(target)
    with If(abs(delta) > max_delta):
        res.set(current + sign(delta) * max_delta)

    return res.value


__all__ = [
    "inverse_lerp",
    "remap",
    "smoothstep",
    "smootherstep",
    "pingpong",
    "repeat",
    "move_towards",
    "move_towards_angle",
]
