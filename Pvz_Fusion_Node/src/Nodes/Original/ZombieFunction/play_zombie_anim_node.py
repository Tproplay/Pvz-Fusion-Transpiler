from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlayZombieAnimNode(Node):
    node_type = "PlayZombieAnimNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        animation_name: str = "idle",
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="PlayZombieAnimNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("animationName", str(animation_name))

    @property
    def animation_name(self) -> str:
        return self.get_property("animationName", "idle")

    @animation_name.setter
    def animation_name(self, val: str) -> None:
        self.set_property("animationName", str(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["zombie_PortName"] = "僵尸"
        return data
