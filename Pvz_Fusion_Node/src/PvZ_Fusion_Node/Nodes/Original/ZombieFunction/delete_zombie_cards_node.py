from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DeleteZombieCardsNode(Node):
    node_type = "DeleteZombieCardsNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸类型": PortDef("僵尸类型", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
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
            node_type="DeleteZombieCardsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
