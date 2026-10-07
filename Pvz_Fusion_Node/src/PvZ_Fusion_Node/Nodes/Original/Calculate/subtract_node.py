from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SubtractNode(Node):
    node_type = "SubtractNode"
    _class_ports = {
        "被减数": PortDef("被减数", PortDirection.Input, PortType.Float),
        "减数": PortDef("减数", PortDirection.Input, PortType.Float),
        "差": PortDef("差", PortDirection.Output, PortType.Float),
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
            node_type="SubtractNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
