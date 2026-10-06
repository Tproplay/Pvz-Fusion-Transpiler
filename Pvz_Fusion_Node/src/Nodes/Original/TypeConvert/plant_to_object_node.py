from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlantToObjectNode(Node):
    node_type = "PlantToObjectNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "对象": PortDef("对象", PortDirection.Output, PortType.GameObject),
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
            node_type="PlantToObjectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
