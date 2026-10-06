from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ChangeEventMapNode(Node):
    node_type = "ChangeEventMapNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        scene: int = 1,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ChangeEventMapNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("scene", int(scene))

    @property
    def scene(self) -> int:
        return self.get_property("scene", 1)

    @scene.setter
    def scene(self, val: int) -> None:
        self.set_property("scene", int(val))
