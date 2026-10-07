from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnZombieDieNode(Node):
    node_type = "OnZombieDieNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Output, PortType.Zombie),
    }

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="OnZombieDieNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["zombie_PortName"] = "僵尸"
        return data
