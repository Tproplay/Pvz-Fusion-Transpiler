from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DamageZombieNode(Node):
    node_type = "DamageZombieNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "伤害值": PortDef("伤害值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
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
            node_type="DamageZombieNode",
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
        data["damage_PortName"] = "伤害值"
        return data
