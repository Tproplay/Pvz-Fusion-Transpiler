from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetAllPlantsNode(Node):
    node_type = "GetAllPlantsNode"
    _class_ports = {
        "全部植物": PortDef("全部植物", PortDirection.Output, PortType.PlantList),
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
            node_type="GetAllPlantsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["plants_PortName"] = "全部植物"
        return data
