from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class LogarithmNode(Node):
    node_type = "LogarithmNode"
    _class_ports = {
        "真数": PortDef("真数", PortDirection.Input, PortType.Float),
        "底数": PortDef("底数", PortDirection.Input, PortType.Float),
        "结果": PortDef("结果", PortDirection.Output, PortType.Float),
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
            node_type="LogarithmNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
