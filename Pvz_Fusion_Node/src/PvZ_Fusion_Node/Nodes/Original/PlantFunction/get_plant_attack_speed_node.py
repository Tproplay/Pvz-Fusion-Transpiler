from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetPlantAttackSpeedNode(Node):
    node_type = "GetPlantAttackSpeedNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "攻速": PortDef("攻速", PortDirection.Output, PortType.Float),
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
            node_type="GetPlantAttackSpeedNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
