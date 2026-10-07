from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ModifyZombieHealthNode(Node):
    node_type = "ModifyZombieHealthNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "血量倍率": PortDef("血量倍率", PortDirection.Input, PortType.Float),
        "修改成功": PortDef("修改成功", PortDirection.Output, PortType.Trigger),
        "僵尸Out": PortDef("僵尸", PortDirection.Output, PortType.Zombie),
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
            node_type="ModifyZombieHealthNode",
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
        data["ratio_PortName"] = "血量倍率"
        data["onModified_PortName"] = "修改成功"
        data["zombieOut_PortName"] = "僵尸"
        return data
