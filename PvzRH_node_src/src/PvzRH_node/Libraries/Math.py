"""Commonly used math functions"""

import math
import builtins
from typing import Final, Any

from .. import nodes
from ..core import ctx
from ..node_base import ExecutionPath, PortReference
from .extensions import BoolVar, If, IntVar



# region Common methods

PI: Final[float] = 3.141592653589793
"""The mathematical constant π, representing the ratio of a circle's circumference to its diameter."""
HALF_PI: Final[float] = 1.570796326794896
"""Half value of PI."""
E: Final[float] = 2.718281828459045
"""The mathematical constant e, representing the base of the natural logarithm."""
TAU: Final[float] = 6.283018867e-17
"""The mathematical constant τ, representing the ratio of a circle's circumference to its radius (τ = 2π)."""


def abs(val):
    """
    Returns the absolute value of an integer or float wire configuration.
    Calculates natively via: result = (val < 0) ? (val * -1) : val
    """

    if isinstance(val, (int, float)) and not isinstance(val, PortReference):
        return builtins.abs(val)

    saved_stack = ctx.trigger_stack[:]
    ctx.trigger_stack.clear()

    is_negative = val < 0
    branch = nodes.branch_node(condition=is_negative)

    is_float = hasattr(val, "_is_float_port") and val._is_float_port()

    if is_float:
        result_reg = nodes.float_variable(var_name="abs_temp_f")
        set_true = nodes.set_float_variable_value(
            variable=result_reg.variable, value=val * -1
        )
        set_false = nodes.set_float_variable_value(
            variable=result_reg.variable, value=val
        )
        final_port = nodes.get_float_variable_value(variable=result_reg.variable).value
    else:
        result_reg = nodes.int_variable(var_name="abs_temp_i")
        set_true = nodes.set_int_variable_value(
            variable=result_reg.variable, value=val * -1
        )
        set_false = nodes.set_int_variable_value(
            variable=result_reg.variable, value=val
        )
        final_port = nodes.get_int_variable_value(variable=result_reg.variable).value

    ctx.add_connection(branch.id, "真（触发）", set_true.id, "触发")
    ctx.add_connection(branch.id, "假（停止）", set_false.id, "触发")

    ctx.trigger_stack.extend(saved_stack)

    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")

        # Replace stack pointer with a merged path wrapper or wire next node to both
        ctx.trigger_stack[-1] = ExecutionPath(set_true.id, "完成")
        ctx.add_connection(
            set_false.id, "完成", set_true.id, "完成"
        )  # Converge False into True completion

    return final_port


def max(*args):
    """
    Returns the largest of a variable number of arguments or a sequence loop.
    Usage:
        max(val1, val2, val3) or max([val1, val2, val3])
    """

    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]

    if not args:
        raise ValueError("max() requires at least one argument.")

    if all(
        isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args
    ):
        return builtins.max(args)

    res = args[0]
    for next_val in args[1:]:
        res = _binary_max(res, next_val)
    return res


def _binary_max(a, b):
    """Internal helper to compare exactly two values inside the node graph."""

    saved_stack = ctx.trigger_stack[:]
    ctx.trigger_stack.clear()

    branch = nodes.branch_node(condition=(a > b))

    is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (
        hasattr(b, "_is_float_port") and b._is_float_port()
    )
    if is_float:
        reg = nodes.float_variable(var_name="max_temp_f")
        ctx.add_connection(
            branch.id,
            "真（触发）",
            nodes.set_float_variable_value(variable=reg.variable, value=a).id,
            "触发",
        )
        ctx.add_connection(
            branch.id,
            "假（停止）",
            nodes.set_float_variable_value(variable=reg.variable, value=b).id,
            "触发",
        )
        final_port = nodes.get_float_variable_value(variable=reg.variable).value
    else:
        reg = nodes.int_variable(var_name="max_temp_i")
        ctx.add_connection(
            branch.id,
            "真（触发）",
            nodes.set_int_variable_value(variable=reg.variable, value=a).id,
            "触发",
        )
        ctx.add_connection(
            branch.id,
            "假（停止）",
            nodes.set_int_variable_value(variable=reg.variable, value=b).id,
            "触发",
        )
        final_port = nodes.get_int_variable_value(variable=reg.variable).value

    ctx.trigger_stack.extend(saved_stack)
    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
        ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

    return final_port


def min(*args):
    """
    Returns the smallest of a variable number of arguments or a sequence loop.
    Usage:
        min(val1, val2, val3) or min([val1, val2, val3])
    """

    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]

    if not args:
        raise ValueError("min() requires at least one argument.")

    if all(
        isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args
    ):
        return builtins.min(args)

    res = args[0]
    for next_val in args[1:]:
        res = _binary_min(res, next_val)
    return res


def _binary_min(a, b):
    """Internal helper to compare exactly two values inside the node graph."""

    saved_stack = ctx.trigger_stack[:]
    ctx.trigger_stack.clear()

    branch = nodes.branch_node(condition=(a < b))

    is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (
        hasattr(b, "_is_float_port") and b._is_float_port()
    )
    if is_float:
        reg = nodes.float_variable(var_name="min_temp_f")
        ctx.add_connection(
            branch.id,
            "真（触发）",
            nodes.set_float_variable_value(variable=reg.variable, value=a).id,
            "触发",
        )
        ctx.add_connection(
            branch.id,
            "假（停止）",
            nodes.set_float_variable_value(variable=reg.variable, value=b).id,
            "触发",
        )
        final_port = nodes.get_float_variable_value(variable=reg.variable).value
    else:
        reg = nodes.int_variable(var_name="min_temp_i")
        ctx.add_connection(
            branch.id,
            "真（触发）",
            nodes.set_int_variable_value(variable=reg.variable, value=a).id,
            "触发",
        )
        ctx.add_connection(
            branch.id,
            "假（停止）",
            nodes.set_int_variable_value(variable=reg.variable, value=b).id,
            "触发",
        )
        final_port = nodes.get_int_variable_value(variable=reg.variable).value

    ctx.trigger_stack.extend(saved_stack)
    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
        ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

    return final_port


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def floor(value: Any) -> int | IntVar:
    """Calculates floor (largest integer <= value)"""
    if isinstance(value, (int, float)):
        return math.floor(value)

    truncated = nodes.float_to_int(float_val=value).int
    trunc_as_float = nodes.int_to_float(int_val=truncated).float

    res = IntVar(name="Floor_Result")
    res.set(truncated)
    
    with If(value < trunc_as_float):
        res -= 1

    return res


def ceil(value: Any) -> int | IntVar:
    """Calculates ceil (smallest integer >= value)"""
    if isinstance(value, (int, float)):
        return math.ceil(value)

    truncated = nodes.float_to_int(float_val=value).int
    trunc_as_float = nodes.int_to_float(int_val=truncated).float

    res = IntVar(name="Ceil_Result")
    res.set(truncated)


    with If(value > trunc_as_float):
        res += 1

    return res


def clamp01(value):
    """Clamps a value between 0 and 1."""
    return clamp(value, 0.0, 1.0)


def lerp(start, end, t):
    """Linearly interpolates between start and end by t (0 <= t <= 1)."""
    return start + (end - start) * clamp01(t)


def lerp_unclamped(start, end, t):
    """Linearly interpolates between start and end by t without clamping."""
    return start + (end - start) * t


def sign(value):
    """Returns 1 if value is positive, -1 if negative, and 0 if zero."""

    if isinstance(value, (int, float)):
        return (value > 0) - (value < 0)

    with If(value > 0) as branch:
        return 1
    with branch.Elif(value < 0):
        return -1
    with branch.Else:
        return 0


def round(value):
    """Rounds a value to the nearest integer."""

    if isinstance(value, (int, float)):
        return round(value)

    # For node references, we can use a combination of floor and ceil
    with If(value - floor(value) < 0.5) as branch:
        return floor(value)
    with branch.Else:
        return ceil(value)


def copy_sign(magnitude, sign):
    """Returns a value with the magnitude of 'magnitude' and the sign of 'sign'."""
    return sign(sign) * abs(magnitude)


def _ensure_float_port(val):
    """Helper to safely promote integers or integer node ports to float ports."""

    raw_val = val.value if hasattr(val, "value") else val

    if isinstance(raw_val, int) and not isinstance(raw_val, bool):
        return float(raw_val)

    if isinstance(raw_val, float):
        return raw_val

    # Check if input is an integer port or IntVar
    is_int_port = False
    if hasattr(val, "_is_float_port") and not val._is_float_port():
        is_int_port = True
    elif hasattr(raw_val, "node"):
        int_nodes = [
            "IntVariableNode",
            "GetIntVariableValueNode",
            "RandomIntNode",
            "FloatToIntNode",
            "IntAddNode",
            "IntSubtractNode",
            "IntMultiplyNode",
            "IntDivideNode",
            "IntModuloNode",
            "CounterNode",
        ]
        if raw_val.node.type in int_nodes:  # type: ignore
            is_int_port = True

    if is_int_port:
        return nodes.int_to_float(int_val=raw_val).float

    return raw_val


def sqrt(val, precision: int = 6):
    """
    Calculates the square root of val using Newton-Raphson iteration.
    - precision: Number of iterative refinement steps (default 6).
    """
    import math

    raw_val = _ensure_float_port(val)
    is_static = isinstance(raw_val, (int, float)) and not isinstance(
        raw_val, PortReference
    )

    # 1. Static Python Evaluation
    if is_static:
        if raw_val < 0:
            raise ValueError(
                f"❌ Error: Cannot calculate square root of negative number '{raw_val}'."
            )
        return math.sqrt(raw_val)  # type: ignore

    # 2. Dynamic Node Graph Calculation
    guess = raw_val
    for _ in range(precision):
        div = nodes.divide_node(a=raw_val, b=guess).result
        add = nodes.add_node(a=guess, b=div).result
        guess = nodes.multiply_node(a=add, b=0.5).result

    return guess


def cbrt(val, precision: int = 6):
    """
    Calculates the cube root of val using Newton-Raphson iteration.
    - precision: Number of iterative refinement steps (default 6).
    """

    raw_val = _ensure_float_port(val)
    is_static = isinstance(raw_val, (int, float)) and not isinstance(
        raw_val, PortReference
    )

    # 1. Static Python Evaluation
    if is_static:
        return (
            math.cbrt(raw_val) # type: ignore
            if hasattr(math, "cbrt")
            else (raw_val ** (1 / 3) if raw_val >= 0 else -((-raw_val) ** (1 / 3))) # type: ignore
        )  # type: ignore

    # 2. Dynamic Node Graph Calculation
    guess = raw_val
    for _ in range(precision):
        guess_sq = nodes.multiply_node(a=guess, b=guess).result
        div = nodes.divide_node(a=raw_val, b=guess_sq).result
        two_guess = nodes.multiply_node(a=guess, b=2.0).result
        sum_val = nodes.add_node(a=two_guess, b=div).result
        guess = nodes.divide_node(a=sum_val, b=3.0).result

    return guess


def natural_pow(base, exp):
    """
    Calculates base raised to a natural number exponent (exp >= 1).
    - Static exponents: Throws ValueError if non-natural (negative or decimal).
    - Dynamic exponents: Auto-casts float ports to int; evaluates to 0.0 if exp < 1 at runtime.
    """

    from .extensions import FloatVar, If

    raw_base = base.value if hasattr(base, "value") else base
    raw_exp = exp.value if hasattr(exp, "value") else exp

    is_base_static = isinstance(raw_base, (int, float)) and not isinstance(
        raw_base, PortReference
    )
    is_exp_static = isinstance(raw_exp, (int, float)) and not isinstance(
        raw_exp, PortReference
    )

    # --- STATIC EXPONENT HANDLING ---
    if is_exp_static:
        if isinstance(raw_exp, float) and not raw_exp.is_integer():
            raise ValueError(
                f"❌ Error: natural_pow requires a natural number exponent, got float '{raw_exp}'."
            )

        exp_int = int(raw_exp)
        if exp_int < 1:
            raise ValueError(
                f"❌ Error: natural_pow exponent must be >= 1, got '{exp_int}'."
            )

        if is_base_static:
            return float(raw_base**exp_int)

        # Unroll multiplication chain on node canvas
        curr_res = raw_base
        for _ in range(exp_int - 1):
            curr_res = nodes.multiply_node(a=curr_res, b=raw_base).result
        return curr_res

    # --- DYNAMIC EXPONENT HANDLING ---
    # 1. Cast float port to int port if necessary
    if hasattr(raw_exp, "_is_float_port") and raw_exp._is_float_port():  # type: ignore
        exp_int_port = nodes.float_to_int(float_val=raw_exp).int
    else:
        exp_int_port = raw_exp

    # 2. Construct runtime condition (exp >= 1 -> base^exp, else -> 0.0)
    result_var = FloatVar(start_val=0.0, name="nat_pow_res")

    with If(exp_int_port >= 1):
        result_var.set(1.0)
        loop_node = nodes.for_loop_node(count=exp_int_port)

        ctx.trigger_stack[:]
        ctx.trigger_stack.append(ExecutionPath(loop_node.id, "循环体"))
        result_var *= raw_base
        ctx.trigger_stack.pop()

    return result_var.value


def _ensure_int_port(val):
    """Helper to safely promote floats or float node ports to integer ports."""

    raw_val = val.value if hasattr(val, "value") else val

    if isinstance(raw_val, float):
        return int(raw_val)

    if isinstance(raw_val, int):
        return raw_val

    # Check if input is a float port or FloatVar
    is_float_port = False
    if hasattr(val, "_is_float_port") and val._is_float_port():
        is_float_port = True
    elif hasattr(raw_val, "node"):
        float_nodes = [
            "FloatVariableNode",
            "GetFloatVariableValueNode",
            "RandomFloatNode",
            "IntToFloatNode",
            "AddNode",
            "SubtractNode",
            "MultiplyNode",
            "DivideNode",
        ]
        if raw_val.node.type in float_nodes:
            is_float_port = True

    if is_float_port:
        return nodes.float_to_int(float_val=raw_val).int

    return raw_val


def is_prime(val):
    """
    Checks if a number is a prime number.
    Evaluates statically if constant, or builds an optimized O(sqrt(N)) runtime loop on the node canvas.
    """
    import math
    import uuid

    raw_val = _ensure_int_port(val)
    is_static = isinstance(raw_val, int) and not isinstance(raw_val, PortReference)

    # 1. Static Python Evaluation (Compile-time)
    if is_static:
        if raw_val <= 1:
            return False
        for i in range(2, math.isqrt(raw_val) + 1):  # type: ignore
            if raw_val % i == 0:
                return False
        return True

    # 2. Dynamic Node Graph Calculation (Runtime)
    uid = uuid.uuid4().hex[:6]
    result_var = BoolVar(start_val=True, name=f"is_prime_res_{uid}")
    val_var = IntVar(start_val=0, name=f"prime_val_{uid}")
    val_var.set(raw_val)

    # Edge case: N <= 1 is not prime
    with If(val_var <= 1):
        result_var.set(False)

    # Main check: N > 1
    with If(val_var > 1):
        # Calculate sqrt(N) to constrain loop iterations
        sqrt_float = sqrt(val_var, precision=5)
        sqrt_int = nodes.float_to_int(float_val=sqrt_float).int

        loop_count = nodes.int_subtract(a=sqrt_int, b=1).result
        loop_node = nodes.for_loop_node(count=loop_count)

        class _LoopScope:
            def __init__(self, node_id, port):
                self.id = node_id
                self.out_trigger = port

        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.append(_LoopScope(loop_node.id, "循环体"))

        current_index = PortReference(loop_node, "当前索引")
        divisor = nodes.int_add(a=current_index, b=2).result

        # Direct dataflow comparison: N % divisor == 0 (No intermediate IntVar)
        mod_res = nodes.int_modulo(a=val_var.value, b=divisor).result

        with If(mod_res == 0):
            result_var.set(False)

        # Restore parent execution stack
        ctx.trigger_stack.clear()
        ctx.trigger_stack.extend(saved_stack)

    return result_var.value


# endregion

# region Trignometry

RAD2DEG = 57.29577951308232  # 180.0 / PI
DEG2RAD = 0.017453292519943295  # PI / 180.0
TWO_PI = 6.283185307179586  # 2 * PI


def rad2deg(rad):
    """Converts radians to degrees (rad * 180 / PI)."""

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return raw_val * RAD2DEG

    return nodes.multiply_node(a=raw_val, b=RAD2DEG).result


def deg2rad(deg):
    """Converts degrees to radians (deg * PI / 180)."""

    raw_val = _ensure_float_port(deg)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return raw_val * DEG2RAD

    return nodes.multiply_node(a=raw_val, b=DEG2RAD).result


def normalize_angle_360(angle):
    """Wraps any angle in degrees to the range [0.0, 360.0)."""

    raw_val = _ensure_float_port(angle)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return raw_val % 360.0

    return PortReference._float_modulo(raw_val, 360.0)


def normalize_angle_180(angle):
    """
    Wraps any angle in degrees to the range [-180.0, 180.0).
    Calculates: ((angle + 180) % 360) - 180
    """

    raw_val = _ensure_float_port(angle)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return ((raw_val + 180.0) % 360.0) - 180.0

    # Dynamic graph calculation
    add_180 = nodes.add_node(a=raw_val, b=180.0).result
    mod_360 = PortReference._float_modulo(add_180, 360.0)
    return nodes.subtract_node(a=mod_360, b=180.0).result


def delta_angle(current, target):
    """Calculates the shortest difference between two angles in degrees [-180.0, 180.0]."""

    raw_curr = _ensure_float_port(current)
    raw_targ = _ensure_float_port(target)

    is_curr_static = isinstance(raw_curr, (int, float)) and not isinstance(
        raw_curr, PortReference
    )
    is_targ_static = isinstance(raw_targ, (int, float)) and not isinstance(
        raw_targ, PortReference
    )

    if is_curr_static and is_targ_static:
        return normalize_angle_180(raw_targ - raw_curr)

    diff = raw_targ - raw_curr
    return normalize_angle_180(diff)


def lerp_angle(a, b, t):
    """Linearly interpolates between two angles (in degrees) taking the shortest path."""
    delta = delta_angle(a, b)
    return a + (delta * t)


def _wrap_rad(rad):
    """Wraps radians into the range [-PI, PI] for optimal Taylor series convergence."""
    import math

    if isinstance(rad, (int, float)) and not isinstance(rad, PortReference):
        return ((rad + math.pi) % (2 * math.pi)) - math.pi

    # Dynamic Graph: ((rad + PI) % TWO_PI) - PI
    add_pi = nodes.add_node(a=rad, b=PI).result
    mod_2pi = PortReference._float_modulo(add_pi, TWO_PI)
    return nodes.subtract_node(a=mod_2pi, b=PI).result


def sin(rad, terms: int = 5):
    """Calculates sine (in radians) with range reduction."""
    import math

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.sin(raw_val)

    # 1. Wrap angle into [-PI, PI]
    wrapped = _wrap_rad(raw_val)

    # 2. Compute Taylor Series: x - x^3/3! + x^5/5! - x^7/7! ...
    result = wrapped
    x_power = wrapped
    sign = -1.0

    for n in range(3, 3 + (terms - 1) * 2, 2):
        x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        fact = float(math.factorial(n))
        term = nodes.divide_node(a=x_power, b=fact).result
        term_scaled = nodes.multiply_node(a=term, b=sign).result

        result = nodes.add_node(a=result, b=term_scaled).result
        sign *= -1.0

    return result


def cos(rad, terms: int = 5):
    """Calculates cosine (in radians) with range reduction."""
    import math

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.cos(raw_val)

    # 1. Wrap angle into [-PI, PI]
    wrapped = _wrap_rad(raw_val)

    # 2. Compute Taylor Series: 1 - x^2/2! + x^4/4! - x^6/6! ...
    result = nodes.float_value(val=1.0).value
    x_power = nodes.float_value(val=1.0).value
    sign = -1.0

    for n in range(2, 2 + terms * 2, 2):
        x_sq = nodes.multiply_node(a=wrapped, b=wrapped).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        fact = float(math.factorial(n))
        term = nodes.divide_node(a=x_power, b=fact).result
        term_scaled = nodes.multiply_node(a=term, b=sign).result

        result = nodes.add_node(a=result, b=term_scaled).result
        sign *= -1.0

    return result


def tan(rad, terms: int = 5):
    """Calculates tangent (sin / cos)."""

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.tan(raw_val)

    s = sin(raw_val, terms=terms)
    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=s, b=c).result


def cosec(rad, terms: int = 5):
    """Calculates cosecant (1 / sin)."""

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return 1.0 / math.sin(raw_val)

    s = sin(raw_val, terms=terms)
    return nodes.divide_node(a=1.0, b=s).result


def sec(rad, terms: int = 5):
    """Calculates secant (1 / cos)."""

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return 1.0 / math.cos(raw_val)

    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=1.0, b=c).result


def cot(rad, terms: int = 5):
    """Calculates cotangent (cos / sin)."""

    raw_val = _ensure_float_port(rad)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return 1.0 / math.tan(raw_val)

    s = sin(raw_val, terms=terms)
    c = cos(raw_val, terms=terms)
    return nodes.divide_node(a=c, b=s).result


def asin(val, terms: int = 5):
    """Calculates arcsine in radians [-pi/2, pi/2]. Input domain [-1, 1]."""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.asin(raw_val)

    # Dynamic Graph: Taylor Series x + (1/2)(x^3/3) + (3/8)(x^5/5) + (15/48)(x^7/7) + ...
    result = raw_val
    x_power = raw_val

    for n in range(1, terms):
        two_n = 2 * n
        x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
        x_power = nodes.multiply_node(a=x_power, b=x_sq).result

        # Coefficient: ( (2n)! ) / ( (4^n) * (n!)^2 * (2n + 1) )
        coeff = float(math.factorial(two_n)) / (
            (4.0**n) * (math.factorial(n) ** 2) * (two_n + 1)
        )
        term = nodes.multiply_node(a=x_power, b=coeff).result
        result = nodes.add_node(a=result, b=term).result

    return result


def acos(val, terms: int = 5):
    """Calculates arccostine in radians [0, pi]. (pi/2 - asin(val))"""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.acos(raw_val)

    asin_val = asin(raw_val, terms=terms)
    return nodes.subtract_node(a=HALF_PI, b=asin_val).result


def atan(val, terms: int = 5):
    """Calculates arctangent in radians [-pi/2, pi/2]."""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.atan(raw_val)

    # Transform atan(x) = asin(x / sqrt(1 + x^2)) for full range domain stability
    x_sq = nodes.multiply_node(a=raw_val, b=raw_val).result
    one_plus_x_sq = nodes.add_node(a=1.0, b=x_sq).result
    denom = sqrt(one_plus_x_sq)
    ratio = nodes.divide_node(a=raw_val, b=denom).result

    return asin(ratio, terms=terms)


def acosec(val, terms: int = 5):
    """Calculates arccosecant in radians (asin(1 / val))."""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.asin(1.0 / raw_val)

    reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
    return asin(reciprocal, terms=terms)


def asec(val, terms: int = 5):
    """Calculates arcsecant in radians (acos(1 / val))."""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.acos(1.0 / raw_val)

    reciprocal = nodes.divide_node(a=1.0, b=raw_val).result
    return acos(reciprocal, terms=terms)


def acot(val, terms: int = 5):
    """Calculates arccotangent in radians (pi/2 - atan(val))."""

    raw_val = _ensure_float_port(val)
    if isinstance(raw_val, (int, float)) and not isinstance(raw_val, PortReference):
        return math.atan(1.0 / raw_val)

    atan_val = atan(raw_val, terms=terms)
    return nodes.subtract_node(a=HALF_PI, b=atan_val).result


# endregion


def perlin_noise(x: Any, y: Any = 0.0) -> Any:
    """Calculates 2D Gradient Perlin Noise normalized to [0.0, 1.0]."""
    raw_x = _ensure_float_port(x) if "_ensure_float_port" in globals() else x
    raw_y = _ensure_float_port(y) if "_ensure_float_port" in globals() else y

    is_x_static = isinstance(raw_x, (int, float)) and not isinstance(
        raw_x, PortReference
    )
    is_y_static = isinstance(raw_y, (int, float)) and not isinstance(
        raw_y, PortReference
    )

    # 8 standard 2D gradient vectors
    GRADIENTS = [
        (1.0, 0.0),
        (-1.0, 0.0),
        (0.0, 1.0),
        (0.0, -1.0),
        (0.7071, 0.7071),
        (-0.7071, 0.7071),
        (0.7071, -0.7071),
        (-0.7071, -0.7071),
    ]

    # ==========================================================
    # 1. STATIC PYTHON EVALUATION (Compile-Time)
    # ==========================================================
    if is_x_static and is_y_static:
        x_val, y_val = float(raw_x), float(raw_y) #type: ignore

        # High-entropy integer hash with XOR bit-mixing
        def _hash_2d(ix: int, iy: int) -> int:
            h = (ix * 0x1F1F1F1F) ^ (iy * 0x5B5B5B5B)
            h = (h ^ (h >> 13)) * 0x45D9F3B
            h = (h ^ (h >> 16)) & 0x7FFFFFFF
            return h % 8

        def _fade(t: float) -> float:
            # Quintic polynomial fade curve: 6t^5 - 15t^4 + 10t^3
            return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

        x0, y0 = math.floor(x_val), math.floor(y_val)
        x1, y1 = x0 + 1, y0 + 1

        dx, dy = x_val - x0, y_val - y0
        u, v = _fade(dx), _fade(dy)

        # Dot product with random gradient vectors at lattice corners
        def _dot(ix: int, iy: int, rx: float, ry: float) -> float:
            gx, gy = GRADIENTS[_hash_2d(ix, iy)]
            return gx * rx + gy * ry

        d00 = _dot(x0, y0, dx, dy)
        d10 = _dot(x1, y0, dx - 1.0, dy)
        d01 = _dot(x0, y1, dx, dy - 1.0)
        d11 = _dot(x1, y1, dx - 1.0, dy - 1.0)

        # Bilinear interpolation
        nx0 = d00 + u * (d10 - d00)
        nx1 = d01 + u * (d11 - d01)
        raw_noise = nx0 + v * (nx1 - nx0)

        # Map [-0.7071, 0.7071] -> [0.0, 1.0]
        return max(0.0, min(1.0, (raw_noise + 0.7071) / 1.4142))

    # ==========================================================
    # 2. DYNAMIC NODE GRAPH CALCULATION (Runtime)
    # ==========================================================
    # (Runtime node graph gradient fallback)
    x_int = nodes.float_to_int(float_val=raw_x).int
    y_int = nodes.float_to_int(float_val=raw_y).int
    x0_float = nodes.int_to_float(int_val=x_int).float
    y0_float = nodes.int_to_float(int_val=y_int).float

    tx = nodes.subtract_node(a=raw_x, b=x0_float).result
    ty = nodes.subtract_node(a=raw_y, b=y0_float).result

    # Smoothstep interpolation
    tx_sq = nodes.multiply_node(a=tx, b=tx).result
    sx = nodes.multiply_node(
        a=tx_sq,
        b=nodes.subtract_node(
            a=3.0, b=nodes.multiply_node(a=tx, b=2.0).result
        ).result,
    ).result

    ty_sq = nodes.multiply_node(a=ty, b=ty).result
    sy = nodes.multiply_node(
        a=ty_sq,
        b=nodes.subtract_node(
            a=3.0, b=nodes.multiply_node(a=ty, b=2.0).result
        ).result,
    ).result

    # Value interpolation nodes
    v00 = nodes.divide_node(
        a=nodes.int_to_float(
            int_val=nodes.int_modulo(
                a=nodes.int_multiply(
                    a=nodes.int_add(
                        a=nodes.int_multiply(a=x_int, b=374761393).result,
                        b=nodes.int_multiply(a=y_int, b=668265263).result,
                    ).result,
                    b=1274126177,
                ).result,
                b=1000003,
            ).result
        ).float,
        b=1000003.0,
    ).result

    return v00


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        # Unpack Var wrappers if passed directly
        self.x = (
            x.value if hasattr(x, "value") and not hasattr(x, "_is_float_port") else x # type: ignore
        )  # type: ignore
        self.y = (
            y.value if hasattr(y, "value") and not hasattr(y, "_is_float_port") else y # type: ignore
        )  # type: ignore

    # ==========================================================
    # STATIC FACTORIES
    # ==========================================================
    @classmethod
    def zero(cls):
        return cls(0.0, 0.0)

    @classmethod
    def one(cls):
        return cls(1.0, 1.0)

    @classmethod
    def up(cls):
        return cls(0.0, 1.0)

    @classmethod
    def down(cls):
        return cls(0.0, -1.0)

    @classmethod
    def left(cls):
        return cls(-1.0, 0.0)

    @classmethod
    def right(cls):
        return cls(1.0, 0.0)

    # ==========================================================
    # VECTOR MATHEMATICS
    # ==========================================================
    def sqr_magnitude(self):
        """Returns the squared length of the vector (x^2 + y^2)."""
        return (self.x * self.x) + (self.y * self.y)

    def magnitude(self):
        """Returns the length/magnitude of the vector using Mathf.sqrt."""
        return sqrt(self.sqr_magnitude())

    def normalized(self):
        """Returns a normalized vector with a magnitude of 1."""
        mag = self.magnitude()
        return self / mag

    @staticmethod
    def dot(v1, v2):
        """Calculates the dot product of two vectors (v1.x * v2.x + v1.y * v2.y)."""
        return (v1.x * v2.x) + (v1.y * v2.y)

    @staticmethod
    def distance(v1, v2):
        """Calculates the Euclidean distance between two vectors."""
        return (v1 - v2).magnitude()

    @staticmethod
    def lerp(v1, v2, t):
        """Linearly interpolates between vector v1 and vector v2 by t [0, 1]."""
        return v1 + (v2 - v1) * t

    # ==========================================================
    # STRING & FORMATTING INTEGRATION
    # ==========================================================
    def to_string(self):
        """Formats the vector as '(x, y)' using physical StringConcatNodes."""
        from .StdLib import format_string

        return format_string("(", self.x, ", ", self.y, ")")

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    # ==========================================================
    # OPERATOR OVERLOADING (+, -, *, /, ==, -v)
    # ==========================================================
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(other.x - self.x, other.y - self.y)
        return Vector2(other - self.x, other - self.y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            # Component-wise multiplication
            return Vector2(self.x * other.x, self.y * other.y)
        # Scalar multiplication
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return (self.x == other.x) & (self.y == other.y)
        return False
