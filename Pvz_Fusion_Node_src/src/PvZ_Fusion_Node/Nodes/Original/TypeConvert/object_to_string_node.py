from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ObjectToStringNode(Node):
    node_type = "ObjectToStringNode"
    _class_ports = {
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "字符串": PortDef("字符串", PortDirection.Output, PortType.String),
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
            node_type="ObjectToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
