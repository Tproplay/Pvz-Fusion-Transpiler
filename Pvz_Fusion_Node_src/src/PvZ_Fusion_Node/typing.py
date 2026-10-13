from __future__ import annotations

from typing import Any
from .Core.context import ctx, single_group
from .Nodes.Original.Node import to_port, Port


class _staticproperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        try:
            return self.fget(owner)
        except TypeError:
            return self.fget()


def _enforce_int(value: Any) -> Any:
    return to_int_port(value)


def _enforce_float(value: Any) -> Any:
    return to_float_port(value)


def _enforce_bool(value: Any) -> Any:
    return to_bool_port(value)


def _enforce_string(value: Any) -> Any:
    if hasattr(value, "id"):
        return value.id
    from .nodes import string_value
    return string_value(val=str(value)).value


def to_float_port(val: Any) -> Any:
    """Converts a raw value, variable, or node port into a valid float output port."""
    from . import nodes
    if isinstance(val, (int, float)) and not isinstance(val, Port):
        return nodes.float_value(val=float(val)).value
    if hasattr(val, "_is_float_port") and not val._is_float_port():
        return nodes.int_to_float(int_val=val).float
    if hasattr(val, "_get_primary_port"):
        val = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
    if hasattr(val, "value"):
        return val.value
    return val


def to_int_port(val: Any) -> Any:
    """Converts a raw value, variable, or node port into a valid integer output port."""
    from . import nodes
    if isinstance(val, (int, float)) and not isinstance(val, Port):
        return nodes.int_value(val=int(val)).value
    if hasattr(val, "_is_float_port") and val._is_float_port():
        return nodes.float_to_int(float_val=val).int
    if hasattr(val, "_get_primary_port"):
        val = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
    if hasattr(val, "value"):
        return val.value
    return val


def to_bool_port(val: Any) -> Any:
    """Converts a literal boolean, condition expression, or variable into a boolean output port."""
    from . import nodes
    if isinstance(val, bool) and not isinstance(val, Port):
        return nodes.bool_value(val=val).value
    if hasattr(val, "_get_primary_port"):
        val = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
    if hasattr(val, "value"):
        return val.value
    return val


__all__ = [
    "to_float_port",
    "to_int_port",
    "to_bool_port",
    "single_group",
    "_staticproperty",
    "_enforce_int",
    "_enforce_float",
    "_enforce_bool",
    "_enforce_string",
]
