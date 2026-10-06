from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringToObjectNode(Node):
    node_type = "StringToObjectNode"
    _class_ports = {
        "字符串": PortDef("字符串", PortDirection.Input, PortType.String),
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
            node_type="StringToObjectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
