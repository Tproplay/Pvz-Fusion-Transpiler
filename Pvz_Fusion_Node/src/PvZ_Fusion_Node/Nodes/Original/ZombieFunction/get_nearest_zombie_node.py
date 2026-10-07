from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetNearestZombieNode(Node):
    node_type = "GetNearestZombieNode"
    _class_ports = {
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
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
            node_type="GetNearestZombieNode",
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
        data["zombie_PortName"] = "僵尸"
        return data
