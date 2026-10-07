from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntDivideNode(Node):
    node_type = "IntDivideNode"
    _class_ports = {
        "被除数": PortDef("被除数", PortDirection.Input, PortType.Int),
        "除数": PortDef("除数", PortDirection.Input, PortType.Int),
        "商": PortDef("商", PortDirection.Output, PortType.Int),
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
            node_type="IntDivideNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
