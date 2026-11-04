from __future__ import annotations

from typing import Any, Optional
from .... import nodes


class Mouse:
    """Helper wrapper for mouse click event data."""

    def __init__(self, mouse_ref: Any = None) -> None:
        if mouse_ref is None:
            mouse_ref = nodes.on_mouse_click()
        self.node = mouse_ref

    @property
    def col(self) -> Any:
        return self.node.column

    @property
    def row(self) -> Any:
        return self.node.row

    @property
    def theItemType(self) -> Any:
        return self.node.item

    @property
    def item(self) -> Any:
        return self.node.item

    @property
    def isLeftClick(self) -> Any:
        return self.node.isLeftButton

    @property
    def is_left_click(self) -> Any:
        return self.node.isLeftButton


__all__ = ["Mouse"]
