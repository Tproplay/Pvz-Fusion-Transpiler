from __future__ import annotations
from typing import Any, Optional
from ..extension_node import ExtensionNode
from .... import nodes


class Mouse(ExtensionNode):
    """Smart wrapper around the mouse input event node."""

    def __init__(self, mouse_ref: Optional[Any] = None) -> None:
        if mouse_ref is None:
            mouse_ref = nodes.on_mouse_click()
        self.node = mouse_ref
        super().__init__(root_node=self.node)

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
    def isLeftClick(self) -> Any:
        return self.node.isLeftButton

    @property
    def world_position(self) -> Any:
        from ...Original.ObjectOperation.get_mouse_world_position_node import GetMouseWorldPositionNode
        node = GetMouseWorldPositionNode()
        return node.get_output(GetMouseWorldPositionNode.Position_output_vector3)


__all__ = ["Mouse"]

