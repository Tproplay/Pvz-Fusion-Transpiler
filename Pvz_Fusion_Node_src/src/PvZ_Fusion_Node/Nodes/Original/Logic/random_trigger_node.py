from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RandomTriggerNode(Node):
    node_type = "RandomTriggerNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "触发数量": PortDef("触发数量", PortDirection.Input, PortType.Int),
        "重复触发": PortDef("重复触发", PortDirection.Input, PortType.Bool),
        "输出": PortDef("触发", PortDirection.Output, PortType.Trigger),
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
            node_type="RandomTriggerNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["count_PortName"] = "触发数量"
        data["allowRepeat_PortName"] = "重复触发"
        data["output_PortName"] = "触发"
        return data
