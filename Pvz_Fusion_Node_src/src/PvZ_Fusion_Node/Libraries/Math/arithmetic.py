"""
Common arithmetic operations, clamping, bounds, rounding, and number-theory utilities.
"""

from __future__ import annotations
import math
import builtins
import uuid
from typing import Any

from ... import nodes
from ...Core.context import ctx, ExecutionPath
from ...node_base import PortReference
from ...Nodes.Extentions.extensions import BoolVar, If, IntVar
from ...Nodes.Original import (
    BranchNode,
    ForLoopNode,
    PulseNode,
    SetIntVariableValueNode,
)


def abs(val: Any) -> Any:
    """Returns the absolute value of an integer or float wire configuration.
    Calculates natively via: result = (val < 0) ? (val * -1) : val
    """
    if isinstance(val, (int, float)) and not isinstance(val, PortReference) and not hasattr(val, "node"):
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

    ctx.add_connection(branch.id, BranchNode.Then_output_trigger, set_true.id, SetIntVariableValueNode.Trigger_input_trigger)
    ctx.add_connection(branch.id, BranchNode.Else_output_trigger, set_false.id, SetIntVariableValueNode.Trigger_input_trigger)

    ctx.trigger_stack.extend(saved_stack)

    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, BranchNode.Trigger_input_trigger)
        ctx.trigger_stack[-1] = ExecutionPath(set_true.id, SetIntVariableValueNode.Complete_output_trigger)
        ctx.add_connection(set_false.id, SetIntVariableValueNode.Complete_output_trigger, set_true.id, SetIntVariableValueNode.Complete_output_trigger)

    return final_port


def _binary_max(a: Any, b: Any) -> Any:
    """Internal helper to compare exactly two values inside the node graph."""
    a_raw = a.value if hasattr(a, "value") else a
    b_raw = b.value if hasattr(b, "value") else b

    saved_stack = ctx.trigger_stack[:]
    ctx.trigger_stack.clear()

    branch = nodes.branch_node(condition=(a_raw > b_raw))

    a_is_float = isinstance(a_raw, float) or (hasattr(a_raw, "_is_float_port") and a_raw._is_float_port())
    b_is_float = isinstance(b_raw, float) or (hasattr(b_raw, "_is_float_port") and b_raw._is_float_port())
    is_float = a_is_float or b_is_float

    if is_float:
        if not a_is_float:
            a_raw = float(a_raw) if isinstance(a_raw, int) else nodes.int_to_float(int_val=a_raw).float
        if not b_is_float:
            b_raw = float(b_raw) if isinstance(b_raw, int) else nodes.int_to_float(int_val=b_raw).float

        reg = nodes.float_variable(var_name="max_temp_f")
        set_true = nodes.set_float_variable_value(variable=reg.variable, value=a_raw)
        set_false = nodes.set_float_variable_value(variable=reg.variable, value=b_raw)
        final_port = nodes.get_float_variable_value(variable=reg.variable).value
    else:
        reg = nodes.int_variable(var_name="max_temp_i")
        set_true = nodes.set_int_variable_value(variable=reg.variable, value=a_raw)
        set_false = nodes.set_int_variable_value(variable=reg.variable, value=b_raw)
        final_port = nodes.get_int_variable_value(variable=reg.variable).value

    ctx.add_connection(branch.id, BranchNode.Then_output_trigger, set_true.id, SetIntVariableValueNode.Trigger_input_trigger)
    ctx.add_connection(branch.id, BranchNode.Else_output_trigger, set_false.id, SetIntVariableValueNode.Trigger_input_trigger)

    merge_node = nodes.pulse_node()
    ctx.add_connection(set_true.id, SetIntVariableValueNode.Complete_output_trigger, merge_node.id, PulseNode.Trigger_input_trigger)
    ctx.add_connection(set_false.id, SetIntVariableValueNode.Complete_output_trigger, merge_node.id, PulseNode.Trigger_input_trigger)

    ctx.trigger_stack.extend(saved_stack)
    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, BranchNode.Trigger_input_trigger)
        ctx.trigger_stack[-1] = ExecutionPath(merge_node.id, PulseNode.OnPulse_output_trigger)

    return final_port


def max(*args: Any) -> Any:
    """Returns the largest of a variable number of arguments or a sequence."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]

    if not args:
        raise ValueError("max() requires at least one argument.")

    def _is_static(x: Any) -> bool:
        raw = x.value if hasattr(x, "value") else x
        return isinstance(raw, (int, float)) and not hasattr(raw, "node")

    if all(_is_static(x) for x in args):
        raw_args = [x.value if hasattr(x, "value") else x for x in args]
        return builtins.max(raw_args)

    res = args[0]
    for next_val in args[1:]:
        res = _binary_max(res, next_val)
    return res


def _binary_min(a: Any, b: Any) -> Any:
    """Internal helper to compare exactly two values inside the node graph."""
    a_raw = a.value if hasattr(a, "value") else a
    b_raw = b.value if hasattr(b, "value") else b

    saved_stack = ctx.trigger_stack[:]
    ctx.trigger_stack.clear()

    branch = nodes.branch_node(condition=(a_raw < b_raw))

    a_is_float = isinstance(a_raw, float) or (hasattr(a_raw, "_is_float_port") and a_raw._is_float_port())
    b_is_float = isinstance(b_raw, float) or (hasattr(b_raw, "_is_float_port") and b_raw._is_float_port())
    is_float = a_is_float or b_is_float

    if is_float:
        if not a_is_float:
            a_raw = float(a_raw) if isinstance(a_raw, int) else nodes.int_to_float(int_val=a_raw).float
        if not b_is_float:
            b_raw = float(b_raw) if isinstance(b_raw, int) else nodes.int_to_float(int_val=b_raw).float

        reg = nodes.float_variable(var_name="min_temp_f")
        set_true = nodes.set_float_variable_value(variable=reg.variable, value=a_raw)
        set_false = nodes.set_float_variable_value(variable=reg.variable, value=b_raw)
        final_port = nodes.get_float_variable_value(variable=reg.variable).value
    else:
        reg = nodes.int_variable(var_name="min_temp_i")
        set_true = nodes.set_int_variable_value(variable=reg.variable, value=a_raw)
        set_false = nodes.set_int_variable_value(variable=reg.variable, value=b_raw)
        final_port = nodes.get_int_variable_value(variable=reg.variable).value

    ctx.add_connection(branch.id, BranchNode.Then_output_trigger, set_true.id, SetIntVariableValueNode.Trigger_input_trigger)
    ctx.add_connection(branch.id, BranchNode.Else_output_trigger, set_false.id, SetIntVariableValueNode.Trigger_input_trigger)

    merge_node = nodes.pulse_node()
    ctx.add_connection(set_true.id, SetIntVariableValueNode.Complete_output_trigger, merge_node.id, PulseNode.Trigger_input_trigger)
    ctx.add_connection(set_false.id, SetIntVariableValueNode.Complete_output_trigger, merge_node.id, PulseNode.Trigger_input_trigger)

    ctx.trigger_stack.extend(saved_stack)
    if ctx.trigger_stack:
        prev_node = ctx.trigger_stack[-1]
        ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, BranchNode.Trigger_input_trigger)
        ctx.trigger_stack[-1] = ExecutionPath(merge_node.id, PulseNode.OnPulse_output_trigger)

    return final_port


def min(*args: Any) -> Any:
    """Returns the smallest of a variable number of arguments or a sequence."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]

    if not args:
        raise ValueError("min() requires at least one argument.")

    def _is_static(x: Any) -> bool:
        raw = x.value if hasattr(x, "value") else x
        return isinstance(raw, (int, float)) and not hasattr(raw, "node")

    if all(_is_static(x) for x in args):
        raw_args = [x.value if hasattr(x, "value") else x for x in args]
        return builtins.min(raw_args)

    res = args[0]
    for next_val in args[1:]:
        res = _binary_min(res, next_val)
    return res


def clamp(value: Any, min_value: Any, max_value: Any) -> Any:
    """Clamps a value to the inclusive range [min_value, max_value]."""
    return max(min_value, min(value, max_value))


def clamp01(value: Any) -> Any:
    """Clamps a value to the inclusive range [0.0, 1.0]."""
    return clamp(value, 0.0, 1.0)


def floor(value: Any) -> int | IntVar:
    """Calculates floor (largest integer <= value)."""
    if isinstance(value, (int, float)) and not hasattr(value, "node"):
        return math.floor(value)

    truncated = nodes.float_to_int(float_val=value).int
    trunc_as_float = nodes.int_to_float(int_val=truncated).float

    res = IntVar(name="Floor_Result")
    res.set(truncated)

    with If(value < trunc_as_float):
        res -= 1

    return res


def ceil(value: Any) -> int | IntVar:
    """Calculates ceil (smallest integer >= value)."""
    if isinstance(value, (int, float)) and not hasattr(value, "node"):
        return math.ceil(value)

    truncated = nodes.float_to_int(float_val=value).int
    trunc_as_float = nodes.int_to_float(int_val=truncated).float

    res = IntVar(name="Ceil_Result")
    res.set(truncated)

    with If(value > trunc_as_float):
        res += 1

    return res


def lerp(start: Any, end: Any, t: Any) -> Any:
    """Linearly interpolates between start and end by t clamped to [0, 1]."""
    return start + (end - start) * clamp01(t)


def lerp_unclamped(start: Any, end: Any, t: Any) -> Any:
    """Linearly interpolates between start and end by t without clamping."""
    return start + (end - start) * t


def sign(value: Any) -> Any:
    """Returns 1 if value is positive, -1 if negative, and 0 if zero."""
    if isinstance(value, (int, float)) and not hasattr(value, "node"):
        return (value > 0) - (value < 0)

    with If(value > 0) as branch:
        return 1
    with branch.Elif(value < 0):
        return -1
    with branch.Else:
        return 0


def round(value: Any) -> Any:
    """Rounds a value to the nearest integer."""
    if isinstance(value, (int, float)) and not hasattr(value, "node"):
        return builtins.round(value)

    with If(value - floor(value) < 0.5) as branch:
        return floor(value)
    with branch.Else:
        return ceil(value)


def copy_sign(magnitude: Any, sign_val: Any) -> Any:
    """Returns a value with the magnitude of magnitude and sign of sign_val."""
    return sign(sign_val) * abs(magnitude)


def mod(a: Any, b: Any) -> Any:
    """Calculates integer modulo using native IntModuloNode."""
    from ...Nodes.Original.Calculate.int_modulo_node import IntModuloNode
    from ...Nodes.Original.Node import to_port

    raw_a = a.value if hasattr(a, "value") else a
    raw_b = b.value if hasattr(b, "value") else b

    if (
        isinstance(raw_a, int)
        and isinstance(raw_b, int)
        and not hasattr(raw_a, "node")
        and not hasattr(raw_b, "node")
        and not isinstance(raw_a, PortReference)
        and not isinstance(raw_b, PortReference)
    ):
        return raw_a % raw_b

    node = IntModuloNode()
    to_port(a).connect(node.get_input(IntModuloNode.Dividend_input_int))
    to_port(b).connect(node.get_input(IntModuloNode.Divisor_input_int))
    return node.get_output(IntModuloNode.Remainder_output_int)


def _ensure_float_port(val: Any) -> Any:
    """Helper to safely promote integers or integer node ports to float ports."""
    raw_val = val.value if hasattr(val, "value") else val

    if isinstance(raw_val, int) and not isinstance(raw_val, bool):
        return float(raw_val)

    if isinstance(raw_val, float):
        return raw_val

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
        if raw_val.node.type in int_nodes:
            is_int_port = True

    if is_int_port:
        return nodes.int_to_float(int_val=raw_val).float

    return raw_val


def _ensure_int_port(val: Any) -> Any:
    """Helper to safely promote floats or float node ports to integer ports."""
    raw_val = val.value if hasattr(val, "value") else val

    if isinstance(raw_val, float):
        return int(raw_val)

    if isinstance(raw_val, int) and not isinstance(raw_val, bool):
        return raw_val

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


def is_prime(val: Any) -> Any:
    """Checks if a number is prime.
    Evaluates statically if constant, or constructs an O(sqrt(N)) runtime loop on the node canvas.
    """
    raw_val = _ensure_int_port(val)
    is_static = isinstance(raw_val, int) and not isinstance(raw_val, PortReference) and not hasattr(raw_val, "node")

    if is_static:
        if raw_val <= 1:
            return False
        for i in range(2, math.isqrt(raw_val) + 1):
            if raw_val % i == 0:
                return False
        return True

    from .powers import sqrt
    uid = uuid.uuid4().hex[:6]
    result_var = BoolVar(start_val=True, name=f"is_prime_res_{uid}")
    val_var = IntVar(start_val=0, name=f"prime_val_{uid}")
    val_var.set(raw_val)

    with If(val_var <= 1):
        result_var.set(False)

    with If(val_var > 1):
        sqrt_float = sqrt(val_var)
        sqrt_int = nodes.float_to_int(float_val=sqrt_float).int

        loop_count = nodes.int_subtract(a=sqrt_int, b=1).result
        loop_node = nodes.for_loop_node(count=loop_count)

        class _LoopScope:
            def __init__(self, node_id: str, port: str):
                self.id = node_id
                self.out_trigger = port

        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.append(_LoopScope(loop_node.id, ForLoopNode.LoopBody_output_trigger))

        current_index = PortReference(loop_node, ForLoopNode.Index_output_int)
        divisor = nodes.int_add(a=current_index, b=2).result
        mod_res = nodes.int_modulo(a=val_var.value, b=divisor).result

        with If(mod_res == 0):
            result_var.set(False)

        ctx.trigger_stack.clear()
        ctx.trigger_stack.extend(saved_stack)

    return result_var.value


def gcd(a: Any, b: Any) -> Any:
    """Calculates the greatest common divisor of a and b."""
    raw_a = a.value if hasattr(a, "value") else a
    raw_b = b.value if hasattr(b, "value") else b

    if (
        isinstance(raw_a, int)
        and isinstance(raw_b, int)
        and not hasattr(raw_a, "node")
        and not hasattr(raw_b, "node")
        and not isinstance(raw_a, PortReference)
        and not isinstance(raw_b, PortReference)
    ):
        return math.gcd(raw_a, raw_b)

    from ...Nodes.Extentions.Loops import While
    var_a = IntVar("gcd_a", a)
    var_b = IntVar("gcd_b", b)
    temp = IntVar("gcd_temp", 0)

    with While(var_b != 0):
        temp.set(var_b.value)
        var_b.set(mod(var_a.value, var_b.value))
        var_a.set(temp.value)

    return var_a.value


def lcm(a: Any, b: Any) -> Any:
    """Calculates the least common multiple of a and b."""
    raw_a = a.value if hasattr(a, "value") else a
    raw_b = b.value if hasattr(b, "value") else b

    if (
        isinstance(raw_a, int)
        and isinstance(raw_b, int)
        and not hasattr(raw_a, "node")
        and not hasattr(raw_b, "node")
        and not isinstance(raw_a, PortReference)
        and not isinstance(raw_b, PortReference)
    ):
        return math.lcm(raw_a, raw_b)

    return abs(a * b) // gcd(a, b)


__all__ = [
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
]
