from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ChangeEventMusicNode(Node):
    node_type = "ChangeEventMusicNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        music: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ChangeEventMusicNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("music", int(music))

    @property
    def music(self) -> int:
        return self.get_property("music", 0)

    @music.setter
    def music(self, val: int) -> None:
        self.set_property("music", int(val))
