from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ForEachAllZombiesNode(Node):
    node_type = "ForEachAllZombiesNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "循环体": PortDef("循环体", PortDirection.Output, PortType.Trigger),
        "当前僵尸": PortDef("当前僵尸", PortDirection.Output, PortType.Zombie),
        "当前索引": PortDef("当前索引", PortDirection.Output, PortType.Int),
        "循环完成": PortDef("循环完成", PortDirection.Output, PortType.Trigger),
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
            node_type="ForEachAllZombiesNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
