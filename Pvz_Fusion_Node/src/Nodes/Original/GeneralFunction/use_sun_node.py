from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class UseSunNode(Node):
    node_type = "UseSunNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "阳光数量": PortDef("阳光数量", PortDirection.Input, PortType.Int),
        "消耗成功": PortDef("消耗成功", PortDirection.Output, PortType.Trigger),
        "阳光不足": PortDef("阳光不足", PortDirection.Output, PortType.Trigger),
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
            node_type="UseSunNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["sunAmount_PortName"] = "阳光数量"
        data["onSuccess_PortName"] = "消耗成功"
        data["onFailed_PortName"] = "阳光不足"
        return data
