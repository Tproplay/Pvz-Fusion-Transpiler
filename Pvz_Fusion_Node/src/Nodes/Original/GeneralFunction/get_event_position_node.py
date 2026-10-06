from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetEventPositionNode(Node):
    node_type = "GetEventPositionNode"
    _class_ports = {
        "位置": PortDef("位置", PortDirection.Output, PortType.Vector3),
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
            node_type="GetEventPositionNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
