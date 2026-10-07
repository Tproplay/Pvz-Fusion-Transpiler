from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RandomFloatNode(Node):
    node_type = "RandomFloatNode"
    _class_ports = {
        "最小值": PortDef("最小值", PortDirection.Input, PortType.Float),
        "最大值": PortDef("最大值", PortDirection.Input, PortType.Float),
        "随机浮点数": PortDef("随机浮点数", PortDirection.Output, PortType.Float),
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
            node_type="RandomFloatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
