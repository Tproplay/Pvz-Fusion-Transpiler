"""
PvZ Fusion Math Module.
Provides mathematical operations, trigonometry, constants, interpolation, noise, and vector geometry for visual scripting.
"""

from .constants import (
    PI,
    HALF_PI,
    TWO_PI,
    TAU,
    E,
    SQRT2,
    DEG2RAD,
    RAD2DEG,
    EPSILON,
    INFINITY,
    NEGATIVE_INFINITY,
)

from .powers import (
    pow,
    natural_pow,
    sqrt,
    cbrt,
    hypot,
    log,
    log2,
    log10,
    exp,
)

from .arithmetic import (
    abs,
    sign,
    round,
    floor,
    ceil,
    clamp,
    clamp01,
    min,
    max,
    lerp,
    lerp_unclamped,
    mod,
    copy_sign,
    is_prime,
    gcd,
    lcm,
)

from .trigonometry import (
    rad2deg,
    deg2rad,
    normalize_angle_360,
    normalize_angle_180,
    delta_angle,
    lerp_angle,
    sin,
    cos,
    sincos,
    tan,
    cosec,
    sec,
    cot,
    asin,
    acos,
    atan,
    atan2,
    acosec,
    asec,
    acot,
)

from .interpolation import (
    inverse_lerp,
    remap,
    smoothstep,
    smootherstep,
    pingpong,
    repeat,
    move_towards,
    move_towards_angle,
)

from .noise import (
    perlin_noise,
    noise1d,
)

from .geometry import (
    Vector2,
    Vector3,
    distance,
    dot,
    cross,
    reflect,
)

__all__ = [
    # Constants
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
    # Powers, Roots & Logs
    "pow",
    "natural_pow",
    "sqrt",
    "cbrt",
    "hypot",
    "log",
    "log2",
    "log10",
    "exp",
    # Arithmetic & Number Theory
    "abs",
    "sign",
    "round",
    "floor",
    "ceil",
    "clamp",
    "clamp01",
    "min",
    "max",
    "lerp",
    "lerp_unclamped",
    "mod",
    "copy_sign",
    "is_prime",
    "gcd",
    "lcm",
    # Trigonometry
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
    # Interpolation
    "inverse_lerp",
    "remap",
    "smoothstep",
    "smootherstep",
    "pingpong",
    "repeat",
    "move_towards",
    "move_towards_angle",
    # Noise
    "perlin_noise",
    "noise1d",
    # Geometry & Vectors
    "Vector2",
    "Vector3",
    "distance",
    "dot",
    "cross",
    "reflect",
]
