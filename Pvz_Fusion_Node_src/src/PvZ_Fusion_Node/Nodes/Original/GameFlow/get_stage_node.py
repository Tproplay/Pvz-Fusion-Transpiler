from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetStageNode(Node):
    node_type = "GetStageNode"
    _class_ports = {
        "阶段名": PortDef("阶段名", PortDirection.Output, PortType.String),
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
            node_type="GetStageNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
