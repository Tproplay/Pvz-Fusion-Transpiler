from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ToggleCycleNode(Node):
    node_type = "ToggleCycleNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "周期间隔": PortDef("周期间隔", PortDirection.Input, PortType.Float),
        "周期事件": PortDef("周期事件", PortDirection.Output, PortType.Trigger),
        "切换开始时": PortDef("切换开始时", PortDirection.Output, PortType.Trigger),
        "切换关闭时": PortDef("切换关闭时", PortDirection.Output, PortType.Trigger),
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
            node_type="ToggleCycleNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["interval_PortName"] = "周期间隔"
        data["cycle_PortName"] = "周期事件"
        data["onEnable_PortName"] = "切换开始时"
        data["onDisable_PortName"] = "切换关闭时"
        return data
