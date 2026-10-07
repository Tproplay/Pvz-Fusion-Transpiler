from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MakeVector3Node(Node):
    node_type = "MakeVector3Node"
    _class_ports = {
        "X": PortDef("X", PortDirection.Input, PortType.Float),
        "Y": PortDef("Y", PortDirection.Input, PortType.Float),
        "Z": PortDef("Z", PortDirection.Input, PortType.Float),
        "向量": PortDef("向量", PortDirection.Output, PortType.Vector3),
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
            node_type="MakeVector3Node",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
