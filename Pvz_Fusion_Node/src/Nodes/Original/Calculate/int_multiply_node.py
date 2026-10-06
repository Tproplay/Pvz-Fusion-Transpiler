from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntMultiplyNode(Node):
    node_type = "IntMultiplyNode"
    _class_ports = {
        "A": PortDef("A", PortDirection.Input, PortType.Int),
        "B": PortDef("B", PortDirection.Input, PortType.Int),
        "积": PortDef("积", PortDirection.Output, PortType.Int),
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
            node_type="IntMultiplyNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
