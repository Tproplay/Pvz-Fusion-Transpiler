from __future__ import annotations

from enum import Enum
from typing import Any, Optional
from .Core.connection_manager import Port, PortDirection, PortType


class _staticproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        try:
            return self.fget(owner)
        except TypeError:
            return self.fget()


class PortReference:
    """Convenience proxy representing a port on a node canvas."""

    def __new__(cls, node: Any, port_name: str) -> Any:
        if hasattr(node, "get_port"):
            try:
                return node.get_port(port_name)
            except Exception:
                pass
        for p in getattr(node, "ports", []):
            if p.name == port_name:
                return p
        raise KeyError(f"Port '{port_name}' not found on {node}")


def to_port(val: Any) -> Port:
    """Coerces any Python value, enum, variable wrapper, or port proxy into a concrete Port."""
    if isinstance(val, Port):
        return val

    if hasattr(val, "_get_primary_port"):
        p = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
        if p is not None:
            return to_port(p)

    if hasattr(val, "primary_port") and getattr(val, "primary_port") is not None:
        return to_port(getattr(val, "primary_port"))

    if hasattr(val, "port") and isinstance(val.port, Port):
        return val.port

    if hasattr(val, "value") and not isinstance(val, (int, float, bool, str, Enum)):
        return to_port(val.value)

    if isinstance(val, bool):
        from ._Nodes.Original.Constants.bool_value_node import BoolValueNode
        return BoolValueNode(value=val).port_output_bool_Value

    if isinstance(val, int):
        from ._Nodes.Original.Constants.int_value_node import IntValueNode
        return IntValueNode(value=val).port_output_int_Value

    if isinstance(val, float):
        from ._Nodes.Original.Constants.float_value_node import FloatValueNode
        return FloatValueNode(value=val).port_output_float_Value

    if isinstance(val, str):
        from ._Nodes.Original.Constants.string_value_node import StringValueNode
        return StringValueNode(value=val).port_output_string_Value

    if isinstance(val, Enum):
        from ._Nodes.Original.PlantFunction.plant_type_value_node import PlantTypeValueNode
        from ._Nodes.Original.ZombieFunction.zombie_type_value_node import ZombieTypeValueNode
        from ._Nodes.Original.Constants.int_value_node import IntValueNode

        val_num = int(val.value) if hasattr(val, "value") else 0
        if val.__class__.__name__ == "PlantType":
            return PlantTypeValueNode(value=val_num).port_output_planttype_PlantType
        elif val.__class__.__name__ == "ZombieType":
            return ZombieTypeValueNode(value=val_num).port_output_zombietype_ZombieType
        return IntValueNode(value=val_num).port_output_int_Value

    raise TypeError(f"Cannot coerce object of type '{type(val).__name__}' to a Port: {val!r}")


def to_int_port(val: Any) -> Port:
    """Converts a raw value, variable, or node port into a valid integer output port."""
    port = to_port(val)
    if port.port_type in (PortType.Float, PortType.FloatVariable):
        from ._Nodes.Original.TypeConvert.float_to_int_node import FloatToIntNode
        conv = FloatToIntNode()
        port.connect(conv.port_input_float_Float)
        return conv.port_output_int_Int
    return port


def to_float_port(val: Any) -> Port:
    """Converts a raw value, variable, or node port into a valid float output port."""
    port = to_port(val)
    if port.port_type in (PortType.Int, PortType.IntVariable):
        from ._Nodes.Original.TypeConvert.int_to_float_node import IntToFloatNode
        conv = IntToFloatNode()
        port.connect(conv.port_input_int_Int)
        return conv.port_output_float_Float
    return port


def to_bool_port(val: Any) -> Port:
    """Converts a literal boolean, condition expression, or variable into a boolean output port."""
    port = to_port(val)
    if port.port_type == PortType.Int:
        from ._Nodes.Original.TypeConvert.int_to_bool_node import IntToBoolNode
        conv = IntToBoolNode()
        port.connect(conv.port_input_int_Value)
        return conv.port_output_bool_Bool
    elif port.port_type == PortType.Float:
        from ._Nodes.Original.TypeConvert.float_to_bool_node import FloatToBoolNode
        conv = FloatToBoolNode()
        port.connect(conv.port_input_float_Value)
        return conv.port_output_bool_Bool
    return port


def to_string_port(val: Any) -> Port:
    """Converts a value or port into a String output port."""
    port = to_port(val)
    if port.port_type == PortType.Int:
        from ._Nodes.Original.TypeConvert.int_to_string_node import IntToStringNode
        conv = IntToStringNode()
        port.connect(conv.port_input_int_Value)
        return conv.port_output_string_String
    elif port.port_type == PortType.Float:
        from ._Nodes.Original.TypeConvert.float_to_string_node import FloatToStringNode
        from ._Nodes.Original.Constants.int_value_node import IntValueNode
        conv = FloatToStringNode()
        dec = IntValueNode(value=2)
        port.connect(conv.port_input_float_Value)
        dec.port_output_int_Value.connect(conv.port_input_int_Decimals)
        return conv.port_output_string_String
    return port


__all__ = [
    "_staticproperty",
    "PortReference",
    "to_port",
    "to_int_port",
    "to_float_port",
    "to_bool_port",
    "to_string_port",
]
