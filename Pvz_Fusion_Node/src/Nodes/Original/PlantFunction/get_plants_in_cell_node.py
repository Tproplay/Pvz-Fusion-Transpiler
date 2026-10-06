from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetPlantsInCellNode(Node):
    node_type = "GetPlantsInCellNode"
    _class_ports = {
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
        "植物列表": PortDef("植物列表", PortDirection.Output, PortType.PlantList),
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
            node_type="GetPlantsInCellNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["row_PortName"] = "行"
        data["column_PortName"] = "列"
        data["plants_PortName"] = "植物列表"
        return data
