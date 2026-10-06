from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class AsciiToStringNode(Node):
    node_type = "AsciiToStringNode"
    _class_ports = {
        "ASCII": PortDef("ASCII", PortDirection.Input, PortType.Int),
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
            node_type="AsciiToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
