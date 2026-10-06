from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlaySoundNode(Node):
    node_type = "PlaySoundNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "音效ID": PortDef("音效ID", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        sound_id: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="PlaySoundNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("soundId", int(sound_id))

    @property
    def sound_id(self) -> int:
        return self.get_property("soundId", 0)

    @sound_id.setter
    def sound_id(self, val: int) -> None:
        self.set_property("soundId", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["soundId_PortName"] = "音效ID"
        return data
