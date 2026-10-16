from __future__ import annotations
from typing import Any, Optional
from ..extension_node import ExtensionNode
from .... import nodes
from ...Original.Node import Port
from ..GameObject.game_object import Vector3
from ...Original.ObjectOperation.get_mouse_world_position_node import GetMouseWorldPositionNode


class Mouse(ExtensionNode):
    """Smart wrapper around the mouse input event node."""

    def __init__(self, mouse_ref: Optional[Any] = None) -> None:
        if mouse_ref is None:
            mouse_ref = nodes.on_mouse_click()
        self.node = mouse_ref
        super().__init__(root_node=self.node)

    @property
    def col(self) -> Port:
        return self.node.column

    @property
    def row(self) -> Port:
        return self.node.row

    @property
    def theItemType(self) -> Port:
        return self.node.item

    @property
    def isLeftClick(self) -> Port:
        return self.node.isLeftButton

    @property
    def world_position(self) -> Vector3:
        node = GetMouseWorldPositionNode()
        pos_port = node.get_output(GetMouseWorldPositionNode.Position_output_vector3)
        return Vector3(port=pos_port)


__all__ = ["Mouse"]


