from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class UseMoneyNode(Node):
    node_type = "UseMoneyNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "金币数量": PortDef("金币数量", PortDirection.Input, PortType.Int),
        "消耗成功": PortDef("消耗成功", PortDirection.Output, PortType.Trigger),
        "金币不足": PortDef("金币不足", PortDirection.Output, PortType.Trigger),
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
            node_type="UseMoneyNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["moneyAmount_PortName"] = "金币数量"
        data["onSuccess_PortName"] = "消耗成功"
        data["onFailed_PortName"] = "金币不足"
        return data
