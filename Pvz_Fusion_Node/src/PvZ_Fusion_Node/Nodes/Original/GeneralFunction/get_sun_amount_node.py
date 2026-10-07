from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetSunAmountNode(Node):
    node_type = "GetSunAmountNode"
    _class_ports = {
        "阳光数量": PortDef("阳光数量", PortDirection.Output, PortType.Int),
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
            node_type="GetSunAmountNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["sunAmount_PortName"] = "阳光数量"
        return data
