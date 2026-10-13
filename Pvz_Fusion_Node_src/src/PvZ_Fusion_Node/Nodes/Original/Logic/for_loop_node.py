from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ForLoopNode(Node):
    node_type = "ForLoopNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "循环次数": PortDef("循环次数", PortDirection.Input, PortType.Int),
        "循环体": PortDef("循环体", PortDirection.Output, PortType.Trigger),
        "当前索引": PortDef("当前索引", PortDirection.Output, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
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
            node_type="ForLoopNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["count_PortName"] = "循环次数"
        data["output_PortName"] = "循环体"
        data["index_PortName"] = "当前索引"
        return data
