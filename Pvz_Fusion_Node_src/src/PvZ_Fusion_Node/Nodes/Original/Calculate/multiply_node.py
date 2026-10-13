from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MultiplyNode(Node):
    node_type = "MultiplyNode"
    _class_ports = {
        "A": PortDef("A", PortDirection.Input, PortType.Float),
        "B": PortDef("B", PortDirection.Input, PortType.Float),
        "积": PortDef("积", PortDirection.Output, PortType.Float),
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
            node_type="MultiplyNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
