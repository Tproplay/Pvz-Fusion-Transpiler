from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PowerNode(Node):
    node_type = "PowerNode"
    _class_ports = {
        "底数": PortDef("底数", PortDirection.Input, PortType.Float),
        "指数": PortDef("指数", PortDirection.Input, PortType.Float),
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
            node_type="PowerNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
