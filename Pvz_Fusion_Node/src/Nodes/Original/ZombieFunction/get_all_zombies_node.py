from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetAllZombiesNode(Node):
    node_type = "GetAllZombiesNode"
    _class_ports = {
        "全部僵尸": PortDef("全部僵尸", PortDirection.Output, PortType.ZombieList),
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
            node_type="GetAllZombiesNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
