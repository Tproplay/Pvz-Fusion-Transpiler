from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetMoneyAmountNode(Node):
    node_type = "GetMoneyAmountNode"
    _class_ports = {
        "金钱数量": PortDef("金钱数量", PortDirection.Output, PortType.Int),
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
            node_type="GetMoneyAmountNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
