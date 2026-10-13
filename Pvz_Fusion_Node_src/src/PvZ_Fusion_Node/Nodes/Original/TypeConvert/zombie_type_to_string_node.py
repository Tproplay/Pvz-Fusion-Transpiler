from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ZombieTypeToStringNode(Node):
    node_type = "ZombieTypeToStringNode"
    _class_ports = {
        "僵尸类型": PortDef("僵尸类型", PortDirection.Input, PortType.ZombieType),
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
            node_type="ZombieTypeToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
