from .core import ctx, single_group

__all__ =[
    # For users
    "to_float_port",
    "to_int_port",
    "to_bool_port",
    "single_group"
]

def _enforce_int(value) -> str:
    if hasattr(value, "id"): return value.id
    if isinstance(value, str): raise TypeError(f"Cannot cast string '{value}' to an Integer.")
    
    value = int(value) if isinstance(value, float) else value
    value = 1 if isinstance(value, bool) else value

    node_id = ctx._generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "IntValueNode", 
        "kwargs": {
            "value": int(value),
            "value_PortName": "值"
        }
    })
    return node_id

def _enforce_float(value) -> str:
    if hasattr(value, "id"): return value.id
    if isinstance(value, str): raise TypeError(f"Cannot cast string '{value}' to a Float.")

    node_id = ctx._generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "FloatValueNode", 
        "kwargs": {
            "value": float(value),
            "value_PortName": "值"
        }
    })
    return node_id

def _enforce_bool(value) -> str:
    if hasattr(value, "id"): return value.id
    node_id = ctx._generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "BoolValueNode", 
        "kwargs": {
            "value": bool(value),
            "value_PortName": "值"
        }
    })
    return node_id

def _enforce_string(value) -> str:
    if hasattr(value, "id"): return value.id
    node_id = ctx._generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "StringValueNode", 
        "kwargs": {
            "value": str(value),
            "value_PortName": "值"
        }
    })
    return node_id

class _staticproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        try:
            return self.fget(owner)
        except TypeError:
            return self.fget()

from .node_base import PortReference
from . import nodes

@staticmethod
def to_float_port(val):
    """Converts a raw value, variable, or node port into a valid float output port.

    Handles literal numeric values by instantiating a `float_value` node, promotes
    integer ports via an `int_to_float` conversion node, and unwraps variable
    wrappers (such as `FloatVar` or `IntVar`) down to their underlying port reference.

    Args:
        val (int | float | PortReference | FloatVar | IntVar | Any): The value or port
            reference to standardize into a float port.

    Returns:
        PortReference: A node output port guaranteed to produce a float value.
    """
    if isinstance(val, (int, float)) and not isinstance(val, PortReference):
        return nodes.float_value(val=float(val)).value
    if hasattr(val, "_is_float_port") and not val._is_float_port():
        return nodes.int_to_float(int_val=val).float
    if hasattr(val, "value"):
        return val.value  # type: ignore
    return val


@staticmethod
def to_int_port(val):
    """Converts a raw value, variable, or node port into a valid integer output port.

    Handles literal numeric values by instantiating an `int_value` node, truncates
    float ports via a `float_to_int` conversion node, and unwraps variable
    wrappers (such as `IntVar` or `FloatVar`) down to their underlying port reference.

    Args:
        val (int | float | PortReference | IntVar | FloatVar | Any): The value or port
            reference to standardize into an integer port.

    Returns:
        PortReference: A node output port guaranteed to produce an integer value.
    """
    if isinstance(val, (int, float)) and not isinstance(val, PortReference):
        return nodes.int_value(val=int(val)).value
    if hasattr(val, "_is_float_port") and val._is_float_port():
        return nodes.float_to_int(float_val=val).int
    if hasattr(val, "value"):
        return val.value  # type: ignore
    return val


@staticmethod
def to_bool_port(val):
    """Converts a literal boolean, condition expression, or variable into a boolean output port.

    Converts Python `True`/`False` literals into a static `bool_value` graph node,
    and unwraps higher-level `BoolVar` instances to retrieve their active port reference.

    Args:
        val (bool | PortReference | BoolVar | Any): The boolean literal, conditional port,
            or variable wrapper to convert.

    Returns:
        PortReference: A node output port representing a boolean condition wire.
    """
    if isinstance(val, bool) and not isinstance(val, PortReference):
        return nodes.bool_value(val=val).value
    if hasattr(val, "value"):
        return val.value
    return val
