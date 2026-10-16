from __future__ import annotations

from typing import Any
from ....typing import to_string_port
from .... import nodes


def format_string(*args: Any) -> Any:
    """Dynamically chains text and variables into a single formatted String port."""
    if not args:
        return nodes.string_value(val="").port_output_string_Value

    def _to_str_item(arg: Any) -> Any:
        if hasattr(arg, "to_string") and callable(arg.to_string):
            return to_string_port(arg.to_string())
        return to_string_port(arg)

    current = _to_str_item(args[0])
    for item in args[1:]:
        next_piece = _to_str_item(item)
        current = nodes.string_concat(a=current, b=next_piece).port_output_string_Result
    return current


__all__ = ["format_string"]
