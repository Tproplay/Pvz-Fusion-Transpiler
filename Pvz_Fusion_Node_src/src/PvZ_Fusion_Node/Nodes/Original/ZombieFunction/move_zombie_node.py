from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MoveZombieNode(Node):
    node_type = "MoveZombieNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "目标列": PortDef("目标列", PortDirection.Input, PortType.Int),
        "目标行": PortDef("目标行", PortDirection.Input, PortType.Int),
        "移动成功": PortDef("移动成功", PortDirection.Output, PortType.Trigger),
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
            node_type="MoveZombieNode",
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
        data["column_PortName"] = "目标列"
        data["row_PortName"] = "目标行"
        data["onMoved_PortName"] = "移动成功"
        data["movedZombie_PortName"] = "僵尸"
        return data
