from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ModifyPlantAttackNode(Node):
    node_type = "ModifyPlantAttackNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "攻击力加成x100%": PortDef("攻击力加成x100%", PortDirection.Input, PortType.Float),
        "修改成功": PortDef("修改成功", PortDirection.Output, PortType.Trigger),
        "植物Out": PortDef("植物", PortDirection.Output, PortType.Plant),
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
            node_type="ModifyPlantAttackNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plant_PortName"] = "植物"
        data["multiplier_PortName"] = "攻击力加成x100%"
        data["onModified_PortName"] = "修改成功"
        data["plantOut_PortName"] = "植物"
        return data
