from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntSubtractNode(Node):
    node_type = "IntSubtractNode"
    _class_ports = {
        "被减数": PortDef("被减数", PortDirection.Input, PortType.Int),
        "减数": PortDef("减数", PortDirection.Input, PortType.Int),
        "差": PortDef("差", PortDirection.Output, PortType.Int),
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
            node_type="IntSubtractNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
