from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GameOverNode(Node):
    node_type = "GameOverNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "失败原因": PortDef("失败原因", PortDirection.Input, PortType.String),
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
            node_type="GameOverNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["reason_PortName"] = "失败原因"
        return data
