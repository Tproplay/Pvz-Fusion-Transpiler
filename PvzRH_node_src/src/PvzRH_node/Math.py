"""Comprehensive mathematical standard library for node-based graph scripting.

Provides compile-time constant evaluation and dynamic visual script node generation.
Static numeric literals are evaluated immediately in Python, while dynamic graph
references (`PortReference`, `IntVar`, `FloatVar`) are compiled into optimized,
timeline-safe node subgraphs (such as Taylor series approximations, Newton-Raphson
solvers, and pulse-merged conditional branches).

Key Features:
    * Fundamental mathematical constants (`PI`, `E`, `TAU`).
    * Range restriction and interpolation (`clamp`, `clamp01`, `lerp`, `lerp_unclamped`).
    * Safe branching arithmetic (`abs`, `max`, `min`, `sign`, `copy_sign`).
    * Dynamic iterative solvers for root extraction (`sqrt`, `cbrt`).
    * Natural power unrolling and runtime loop exponentiation (`natural_pow`).
    * Prime detection with compile-time or runtime O(sqrt(N)) loops (`is_prime`).
    * Full trigonometric & inverse suites with range wrapping (`sin`, `cos`, `atan`, etc.).
    * Angle utilities and shortest-path angular interpolation (`delta_angle`, `lerp_angle`).
    * 2D gradient noise generation (`perlin_noise`).
    * Complete 2D spatial vector mathematics and operator overloading (`Vector2`).
"""

__all__ = [
    "PI",
    "HALF_PI",
    "E",
    "TAU",
    "abs",
    "max",
    "min",
    "clamp",
    "floor",
    "ceil",
    "clamp01",
    "lerp",
    "lerp_unclamped",
    "sign",
    "round",
    "copy_sign",
    "sqrt",
    "cbrt",
    "natural_pow",
    "is_prime",
    "rad2deg",
    "deg2rad",
    "normalize_angle_360",
    "normalize_angle_180",
    "delta_angle",
    "lerp_angle",
    "sin",
    "cos",
    "tan",
    "cosec",
    "sec",
    "cot",
    "asin",
    "acos",
    "atan",
    "acot",
    "asec",
    "acosec",
    "perlin_noise",
    "Vector2"
]

from .Libraries.Math import *