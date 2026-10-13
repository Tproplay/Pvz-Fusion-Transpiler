from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetPlantAttributeCountdownNode(Node):
    node_type = "GetPlantAttributeCountdownNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "倒计时": PortDef("倒计时", PortDirection.Output, PortType.Float),
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
            node_type="GetPlantAttributeCountdownNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
