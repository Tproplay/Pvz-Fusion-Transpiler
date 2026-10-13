from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntToBoolNode(Node):
    node_type = "IntToBoolNode"
    _class_ports = {
        "整数": PortDef("整数", PortDirection.Input, PortType.Int),
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
            node_type="IntToBoolNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
