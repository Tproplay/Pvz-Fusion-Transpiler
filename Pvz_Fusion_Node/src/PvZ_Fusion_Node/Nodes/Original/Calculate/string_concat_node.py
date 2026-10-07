from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringConcatNode(Node):
    node_type = "StringConcatNode"
    _class_ports = {
        "A": PortDef("A", PortDirection.Input, PortType.String),
        "B": PortDef("B", PortDirection.Input, PortType.String),
        "结果": PortDef("结果", PortDirection.Output, PortType.String),
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
            node_type="StringConcatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
