from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlantTypeToStringNode(Node):
    node_type = "PlantTypeToStringNode"
    _class_ports = {
        "植物类型": PortDef("植物类型", PortDirection.Input, PortType.PlantType),
        "字符串": PortDef("字符串", PortDirection.Output, PortType.String),
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
            node_type="PlantTypeToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
