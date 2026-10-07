from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BranchNode(Node):
    node_type = "BranchNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "条件": PortDef("条件", PortDirection.Input, PortType.Bool),
        "真（触发）": PortDef("真（触发）", PortDirection.Output, PortType.Trigger),
        "假（停止）": PortDef("假（停止）", PortDirection.Output, PortType.Trigger),
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
            node_type="BranchNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["condition_PortName"] = "条件"
        data["then_PortName"] = "真（触发）"
        data["else_PortName"] = "假（停止）"
        return data
