from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ObjectToZombieNode(Node):
    node_type = "ObjectToZombieNode"
    _class_ports = {
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "僵尸": PortDef("僵尸", PortDirection.Output, PortType.Zombie),
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
            node_type="ObjectToZombieNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
