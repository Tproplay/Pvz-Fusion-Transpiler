from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetMouseWorldPositionNode(Node):
    node_type = "GetMouseWorldPositionNode"
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
            node_type="GetMouseWorldPositionNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
