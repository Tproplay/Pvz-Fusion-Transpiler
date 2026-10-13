from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ToggleNode(Node):
    node_type = "ToggleNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "状态": PortDef("状态", PortDirection.Output, PortType.Bool),
        "状态改变时": PortDef("状态改变时", PortDirection.Output, PortType.Trigger),
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
            node_type="ToggleNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["state_PortName"] = "状态"
        data["onChanged_PortName"] = "状态改变时"
        return data
