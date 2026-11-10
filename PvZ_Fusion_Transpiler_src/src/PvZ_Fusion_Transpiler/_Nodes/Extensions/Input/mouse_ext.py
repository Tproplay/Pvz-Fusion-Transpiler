from __future__ import annotations

from typing import Any
from .... import nodes


class _MouseMeta(type):
    """Metaclass exposing live world-mouse queries directly on the Mouse class."""

    @property
    def col(cls) -> Any:
        return nodes.get_mouse_world_position().port_output_int_Col

    @property
    def row(cls) -> Any:
        return nodes.get_mouse_world_position().port_output_int_Row

    @property
    def position(cls) -> Any:
        return nodes.get_mouse_world_position().port_output_vector3_Position

    @property
    def world_position(cls) -> Any:
        return nodes.get_mouse_world_position().port_output_vector3_Position


class Mouse(metaclass=_MouseMeta):
    """Helper wrapper for mouse click event data and live cursor queries."""

    def __init__(self, mouse_ref: Any = None) -> None:
        if mouse_ref is None:
            mouse_ref = nodes.on_mouse_click()
        self.node = mouse_ref

    @property
    def col(self) -> Any:
        return self.node.port_output_int_Col

    @property
    def row(self) -> Any:
        return self.node.port_output_int_Row

    @property
    def theItemType(self) -> Any:
        return self.node.port_output_tooltype_HeldItem

    @property
    def item(self) -> Any:
        return self.node.port_output_tooltype_HeldItem

    @property
    def isLeftClick(self) -> Any:
        return self.node.port_output_bool_IsLeftButton

    @property
    def is_left_click(self) -> Any:
        return self.node.port_output_bool_IsLeftButton


__all__ = ["Mouse"]
