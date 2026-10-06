from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlantSplitNode(Node):
    node_type = "PlantSplitNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "列": PortDef("列", PortDirection.Output, PortType.Int),
        "行": PortDef("行", PortDirection.Output, PortType.Int),
        "植物类型": PortDef("植物类型", PortDirection.Output, PortType.PlantType),
        "植物血量": PortDef("植物血量", PortDirection.Output, PortType.Float),
        "属性倒计时": PortDef("属性倒计时", PortDirection.Output, PortType.Float),
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
            node_type="PlantSplitNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["plant_PortName"] = "植物"
        data["column_PortName"] = "列"
        data["row_PortName"] = "行"
        data["plantType_PortName"] = "植物类型"
        data["health_PortName"] = "植物血量"
        data["attributeCountdown_PortName"] = "属性倒计时"
        return data
