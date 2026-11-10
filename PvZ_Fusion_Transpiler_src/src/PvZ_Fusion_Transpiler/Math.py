"""Extended mathematical utilities and vector helpers for PvZ Fusion Transpiler."""

from __future__ import annotations

import builtins
import math
from typing import Any, Final

from .Core.connection_manager import Port
from ._Nodes.Extensions.Math.calc import Math as _CalcMath, Compare
from ._Nodes.Extensions.Branching import If
from ._Nodes.Extensions.Loops import For
from ._Nodes.Extensions.Variables import IntVar, FloatVar, BoolVar
from . import nodes


PI: Final[float] = 3.141592653589793
HALF_PI: Final[float] = 1.570796326794896
TWO_PI: Final[float] = 6.283185307179586
E: Final[float] = 2.718281828459045
TAU: Final[float] = 6.283185307179586
RAD2DEG: Final[float] = 57.29577951308232
DEG2RAD: Final[float] = 0.017453292519943295

# Re-export native Calc/Compare methods
pow = _CalcMath.pow
power = _CalcMath.power
log = _CalcMath.log
logarithm = _CalcMath.logarithm
greater = _CalcMath.greater
less = _CalcMath.less
equal = _CalcMath.equal
same_object = _CalcMath.same_object


def _is_static(val: Any) -> bool:
    return isinstance(val, (int, float)) and not isinstance(val, bool)


def _unwrap_port(val: Any) -> Any:
    if hasattr(val, "_get_primary_port"):
        return val._get_primary_port()
    return val


def _ensure_float_port(val: Any) -> Any:
    val = _unwrap_port(val)
    if _is_static(val):
        return float(val)
    if isinstance(val, Port) and not val._is_float_port():
        return nodes.int_to_float(int_val=val).port_output_float_Float
    return val


def _ensure_int_port(val: Any) -> Any:
    val = _unwrap_port(val)
    if isinstance(val, int) and not isinstance(val, bool):
        return val
    if isinstance(val, float):
        return int(val)
    if isinstance(val, Port) and val._is_float_port():
        return nodes.float_to_int(float_val=val).port_output_int_Int
    return val


def _is_float_dynamic(val: Any) -> bool:
    p = _unwrap_port(val)
    if isinstance(p, float):
        return True
    return isinstance(p, Port) and p._is_float_port()


def abs(val: Any) -> Any:
    """Returns the absolute value of a static number, variable, or port."""
    if _is_static(val):
        return builtins.abs(val)

    p = _unwrap_port(val)
    res: Any = FloatVar(name="abs_res_f") if _is_float_dynamic(p) else IntVar(name="abs_res_i")
    with If(p < 0) as flow:
        res.set(p * -1)
    with flow.Else:
        res.set(p)
    return res.value


def _binary_max(a: Any, b: Any) -> Any:
    is_f = _is_float_dynamic(a) or _is_float_dynamic(b)
    res: Any = FloatVar(name="max_res_f") if is_f else IntVar(name="max_res_i")
    with If(a > b) as flow:
        res.set(a)
    with flow.Else:
        res.set(b)
    return res.value


def max(*args: Any) -> Any:
    """Returns the largest value among arguments or iterable."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = tuple(args[0])
    if not args:
        raise ValueError("max() requires at least one argument.")
    if all(_is_static(x) for x in args):
        return builtins.max(args)
    res = args[0]
    for next_val in args[1:]:
        res = _binary_max(res, next_val)
    return res


def _binary_min(a: Any, b: Any) -> Any:
    is_f = _is_float_dynamic(a) or _is_float_dynamic(b)
    res: Any = FloatVar(name="min_res_f") if is_f else IntVar(name="min_res_i")
    with If(a < b) as flow:
        res.set(a)
    with flow.Else:
        res.set(b)
    return res.value


def min(*args: Any) -> Any:
    """Returns the smallest value among arguments or iterable."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = tuple(args[0])
    if not args:
        raise ValueError("min() requires at least one argument.")
    if all(_is_static(x) for x in args):
        return builtins.min(args)
    res = args[0]
    for next_val in args[1:]:
        res = _binary_min(res, next_val)
    return res


def clamp(value: Any, min_value: Any, max_value: Any) -> Any:
    """Clamps value between min_value and max_value."""
    return max(min_value, min(value, max_value))


def clamp01(value: Any) -> Any:
    """Clamps a value between 0.0 and 1.0."""
    return clamp(value, 0.0, 1.0)


def floor(value: Any) -> Any:
    """Calculates floor (largest integer <= value)."""
    if _is_static(value):
        return math.floor(value)

    f_port = _ensure_float_port(value)
    truncated = nodes.float_to_int(float_val=f_port).port_output_int_Int
    trunc_as_float = nodes.int_to_float(int_val=truncated).port_output_float_Float

    res = IntVar(name="Floor_Result")
    res.set(truncated)
    with If(f_port < trunc_as_float):
        res -= 1
    return res.value


def ceil(value: Any) -> Any:
    """Calculates ceil (smallest integer >= value)."""
    if _is_static(value):
        return math.ceil(value)

    f_port = _ensure_float_port(value)
    truncated = nodes.float_to_int(float_val=f_port).port_output_int_Int
    trunc_as_float = nodes.int_to_float(int_val=truncated).port_output_float_Float

    res = IntVar(name="Ceil_Result")
    res.set(truncated)
    with If(f_port > trunc_as_float):
        res += 1
    return res.value


def round(value: Any) -> Any:
    """Rounds a value to the nearest integer."""
    if _is_static(value):
        return builtins.round(value)

    f_port = _ensure_float_port(value)
    fl = _ensure_float_port(floor(f_port))
    res = IntVar(name="Round_Result")
    with If((f_port - fl) < 0.5) as flow:
        res.set(floor(f_port))
    with flow.Else:
        res.set(ceil(f_port))
    return res.value


def lerp(start: Any, end: Any, t: Any) -> Any:
    """Linearly interpolates between start and end by t in [0, 1]."""
    return start + ((end - start) * clamp01(t))


def lerp_unclamped(start: Any, end: Any, t: Any) -> Any:
    """Linearly interpolates between start and end by t without clamping."""
    return start + ((end - start) * t)


def sqrt(val: Any, precision: int = 6) -> Any:
    """Calculates square root using Newton-Raphson iteration."""
    raw_val = _ensure_float_port(val)
    if _is_static(raw_val):
        if raw_val < 0:
            raise ValueError(f"Cannot calculate square root of negative number '{raw_val}'.")
        return math.sqrt(raw_val)

    guess = raw_val
    for _ in range(precision):
        guess = (guess + (raw_val / guess)) * 0.5
    return guess


def cbrt(val: Any, precision: int = 6) -> Any:
    """Calculates cube root using Newton-Raphson iteration."""
    raw_val = _ensure_float_port(val)
    if _is_static(raw_val):
        if hasattr(math, "cbrt"):
            return math.cbrt(raw_val)
        return raw_val ** (1.0 / 3.0) if raw_val >= 0 else -((-raw_val) ** (1.0 / 3.0))

    guess = raw_val
    for _ in range(precision):
        guess_sq = guess * guess
        guess = ((guess * 2.0) + (raw_val / guess_sq)) / 3.0
    return guess


def is_prime(val: Any) -> Any:
    """Checks if an integer is prime (compile-time if static, runtime loop if dynamic)."""
    raw_val = _ensure_int_port(val)
    if _is_static(raw_val):
        n = int(raw_val)
        if n <= 1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    result_var = BoolVar(start_val=True, name="is_prime_res")
    val_var = IntVar(start_val=0, name="prime_val")
    val_var.set(raw_val)

    with If(val_var <= 1):
        result_var.set(False)

    with If(val_var > 1):
        sqrt_int = _ensure_int_port(sqrt(val_var, precision=5))
        loop_count = sqrt_int - 1
        with For(loop_count) as loop:
            divisor = loop.index + 2
            mod_res = val_var.value % divisor
            with If(mod_res == 0):
                result_var.set(False)

    return result_var.value


def rad2deg(rad: Any) -> Any:
    """Converts radians to degrees."""
    raw_val = _ensure_float_port(rad)
    if _is_static(raw_val):
        return raw_val * RAD2DEG
    return raw_val * RAD2DEG


def deg2rad(deg: Any) -> Any:
    """Converts degrees to radians."""
    raw_val = _ensure_float_port(deg)
    if _is_static(raw_val):
        return raw_val * DEG2RAD
    return raw_val * DEG2RAD


def _float_modulo(a: Any, b: Any) -> Any:
    if _is_static(a) and _is_static(b):
        return a % b
    q_f = _ensure_float_port(floor(a / b))
    return a - (q_f * b)


def _wrap_rad(rad: Any) -> Any:
    if _is_static(rad):
        return ((rad + math.pi) % TWO_PI) - math.pi
    return _float_modulo(rad + PI, TWO_PI) - PI


def sin(rad: Any, terms: int = 5) -> Any:
    """Calculates sine (in radians) using Taylor series approximation."""
    raw_val = _ensure_float_port(rad)
    if _is_static(raw_val):
        return math.sin(raw_val)

    wrapped = _wrap_rad(raw_val)
    result = wrapped
    x_power = wrapped
    x_sq = wrapped * wrapped
    sign = -1.0
    for n in range(3, 3 + (terms - 1) * 2, 2):
        x_power = x_power * x_sq
        fact = float(math.factorial(n))
        result = result + ((x_power / fact) * sign)
        sign *= -1.0
    return result


def cos(rad: Any, terms: int = 5) -> Any:
    """Calculates cosine (in radians) using Taylor series approximation."""
    raw_val = _ensure_float_port(rad)
    if _is_static(raw_val):
        return math.cos(raw_val)

    wrapped = _wrap_rad(raw_val)
    result = nodes.float_value(val=1.0).port_output_float_Value
    x_power = nodes.float_value(val=1.0).port_output_float_Value
    x_sq = wrapped * wrapped
    sign = -1.0
    for n in range(2, 2 + terms * 2, 2):
        x_power = x_power * x_sq
        fact = float(math.factorial(n))
        result = result + ((x_power / fact) * sign)
        sign *= -1.0
    return result


def tan(rad: Any, terms: int = 5) -> Any:
    """Calculates tangent (sin / cos)."""
    raw_val = _ensure_float_port(rad)
    if _is_static(raw_val):
        return math.tan(raw_val)
    return sin(raw_val, terms=terms) / cos(raw_val, terms=terms)


_NOISE_GRADIENTS = [
    (1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -1.0),
    (0.7071, 0.7071), (-0.7071, 0.7071), (0.7071, -0.7071), (-0.7071, -0.7071),
]


def _perlin_static(x_val: float, y_val: float) -> float:
    def _hash_2d(ix: int, iy: int) -> int:
        h = (ix * 0x1F1F1F1F) ^ (iy * 0x5B5B5B5B)
        h = (h ^ (h >> 13)) * 0x45D9F3B
        h = (h ^ (h >> 16)) & 0x7FFFFFFF
        return h % 8

    def _fade(t: float) -> float:
        return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

    def _dot(ix: int, iy: int, rx: float, ry: float) -> float:
        gx, gy = _NOISE_GRADIENTS[_hash_2d(ix, iy)]
        return gx * rx + gy * ry

    x0, y0 = math.floor(x_val), math.floor(y_val)
    x1, y1 = x0 + 1, y0 + 1
    dx, dy = x_val - x0, y_val - y0
    u, v = _fade(dx), _fade(dy)

    d00 = _dot(x0, y0, dx, dy)
    d10 = _dot(x1, y0, dx - 1.0, dy)
    d01 = _dot(x0, y1, dx, dy - 1.0)
    d11 = _dot(x1, y1, dx - 1.0, dy - 1.0)

    nx0 = d00 + u * (d10 - d00)
    nx1 = d01 + u * (d11 - d01)
    raw_noise = nx0 + v * (nx1 - nx0)
    return builtins.max(0.0, builtins.min(1.0, (raw_noise + 0.7071) / 1.4142))


def perlin_noise(x: Any, y: Any = 0.0) -> Any:
    """Calculates 2D Gradient Perlin Noise normalized to [0.0, 1.0]."""
    raw_x = _ensure_float_port(x)
    raw_y = _ensure_float_port(y)

    if _is_static(raw_x) and _is_static(raw_y):
        return _perlin_static(float(raw_x), float(raw_y))

    x_int = _ensure_int_port(raw_x)
    y_int = _ensure_int_port(raw_y)
    hashed = ((x_int * 374761393) + (y_int * 668265263)) * 1274126177
    mod_val = hashed % 1000003
    return _ensure_float_port(mod_val) / 1000003.0


class Vector2:
    """2D vector class supporting arithmetic and string conversion on graph ports."""

    def __init__(self, x: Any = 0.0, y: Any = 0.0) -> None:
        self.x = _unwrap_port(x)
        self.y = _unwrap_port(y)

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

    def sqr_magnitude(self) -> Any:
        return (self.x * self.x) + (self.y * self.y)

    def magnitude(self) -> Any:
        return sqrt(self.sqr_magnitude())

    def normalized(self) -> Vector2:
        return self / self.magnitude()

    @staticmethod
    def dot(v1: Vector2, v2: Vector2) -> Any:
        return (v1.x * v2.x) + (v1.y * v2.y)

    @staticmethod
    def distance(v1: Vector2, v2: Vector2) -> Any:
        return (v1 - v2).magnitude()

    @staticmethod
    def lerp(v1: Vector2, v2: Vector2, t: Any) -> Vector2:
        return v1 + ((v2 - v1) * t)

    def to_string(self) -> Any:
        from .StdLib import format_string
        return format_string("(", self.x, ", ", self.y, ")")

    def __repr__(self) -> str:
        return f"Vector2({self.x!r}, {self.y!r})"

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


__all__ = [
    "PI",
    "HALF_PI",
    "TWO_PI",
    "E",
    "TAU",
    "RAD2DEG",
    "DEG2RAD",
    "Compare",
    "pow",
    "power",
    "log",
    "logarithm",
    "greater",
    "less",
    "equal",
    "same_object",
    "abs",
    "max",
    "min",
    "clamp",
    "clamp01",
    "floor",
    "ceil",
    "round",
    "lerp",
    "lerp_unclamped",
    "sqrt",
    "cbrt",
    "is_prime",
    "rad2deg",
    "deg2rad",
    "sin",
    "cos",
    "tan",
    "perlin_noise",
    "Vector2",
]
