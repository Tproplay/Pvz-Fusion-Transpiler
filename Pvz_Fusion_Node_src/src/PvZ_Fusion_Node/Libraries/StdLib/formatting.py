"""
String formatting and dynamic text concatenation utilities.
"""

from __future__ import annotations
from typing import Any
from enum import Enum


def format_string(*args: Any) -> Any:
    """Dynamically chains text, variables, node ports, and constants into a single string port.

    Evaluates various input types (booleans, enums, objects with `to_string()`) and 
    generates a physical string concatenation chain on the visual node canvas.

    Args:
        *args: Variable number of arguments to concatenate.

    Returns:
        PortReference: The output port of the final StringConcat node.

    Example:
        ```python
        msg = pvn.StdLib.format_string("Wave ", wave_num, " has arrived!")
        pvn.Print(msg)
        ```
    """
    if not args:
        from ...nodes import string_value

        return string_value(val="").value

    from ...node_base import PortReference
    from ...nodes import string_concat, string_value

    def _parse_arg(arg: Any) -> Any:
        if hasattr(arg, "to_string") and callable(arg.to_string):
            return arg.to_string()

        if isinstance(arg, PortReference):
            return arg._to_string_port()

        from ...Nodes.Original.Node import Port

        if isinstance(arg, Port):
            return arg._to_string_port()

        if hasattr(arg, "node"):
            from ...node_base import PortReference as PR

            port_name = getattr(arg, "port_name", getattr(arg, "out_port", "Output"))
            return PR(arg.node, port_name)._to_string_port()

        if isinstance(arg, bool):
            return string_value(val="True" if arg else "False").value

        if isinstance(arg, Enum):
            return string_value(val=arg.name).value

        return string_value(val=str(arg)).value

    current_chain = _parse_arg(args[0])

    if len(args) == 1:
        return current_chain

    for i in range(1, len(args)):
        next_piece = _parse_arg(args[i])
        current_chain = string_concat(a=current_chain, b=next_piece).result

    return current_chain


__all__ = [
    "format_string",
]
