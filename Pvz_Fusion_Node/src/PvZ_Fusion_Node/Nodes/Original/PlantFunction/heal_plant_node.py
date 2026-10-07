from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class HealPlantNode(Node):
    node_type = "HealPlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "回血量": PortDef("回血量", PortDirection.Input, PortType.Float),
        "回血成功": PortDef("回血成功", PortDirection.Output, PortType.Trigger),
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
            node_type="HealPlantNode",
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
        data["healAmount_PortName"] = "回血量"
        data["onHealed_PortName"] = "回血成功"
        return data
