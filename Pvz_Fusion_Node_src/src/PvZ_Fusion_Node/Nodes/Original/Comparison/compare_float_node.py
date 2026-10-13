from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CompareFloatNode(Node):
    node_type = "CompareFloatNode"
    _class_ports = {
        "值A": PortDef("值A", PortDirection.Input, PortType.Float),
        "值B": PortDef("值B", PortDirection.Input, PortType.Float),
        "大于": PortDef("大于", PortDirection.Output, PortType.Bool),
        "小于": PortDef("小于", PortDirection.Output, PortType.Bool),
        "等于": PortDef("等于", PortDirection.Output, PortType.Bool),
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
            node_type="CompareFloatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["valueA_PortName"] = "值A"
        data["valueB_PortName"] = "值B"
        data["greater_PortName"] = "大于"
        data["less_PortName"] = "小于"
        data["equal_PortName"] = "等于"
        return data
