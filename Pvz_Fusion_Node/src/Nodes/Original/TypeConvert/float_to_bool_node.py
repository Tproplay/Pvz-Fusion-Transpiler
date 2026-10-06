from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatToBoolNode(Node):
    node_type = "FloatToBoolNode"
    _class_ports = {
        "浮点数": PortDef("浮点数", PortDirection.Input, PortType.Float),
        "布尔": PortDef("布尔", PortDirection.Output, PortType.Bool),
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
            node_type="FloatToBoolNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
