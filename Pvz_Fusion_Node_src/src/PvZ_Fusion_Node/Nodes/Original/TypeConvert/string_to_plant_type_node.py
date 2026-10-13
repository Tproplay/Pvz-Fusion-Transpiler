from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringToPlantTypeNode(Node):
    node_type = "StringToPlantTypeNode"
    _class_ports = {
        "字符串": PortDef("字符串", PortDirection.Input, PortType.String),
        "植物类型": PortDef("植物类型", PortDirection.Output, PortType.PlantType),
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
            node_type="StringToPlantTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
