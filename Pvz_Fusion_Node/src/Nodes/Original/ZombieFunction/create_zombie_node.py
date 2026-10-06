from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CreateZombieNode(Node):
    node_type = "CreateZombieNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
        "僵尸类型": PortDef("僵尸类型", PortDirection.Input, PortType.ZombieType),
        "是否魅惑": PortDef("是否魅惑", PortDirection.Input, PortType.Bool),
        "创建成功": PortDef("创建成功", PortDirection.Output, PortType.Trigger),
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
            node_type="CreateZombieNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["row_PortName"] = "行"
        data["column_PortName"] = "列"
        data["zombieType_PortName"] = "僵尸类型"
        data["isMindControlled_PortName"] = "是否魅惑"
        data["onCreated_PortName"] = "创建成功"
        data["zombie_PortName"] = "僵尸"
        return data
