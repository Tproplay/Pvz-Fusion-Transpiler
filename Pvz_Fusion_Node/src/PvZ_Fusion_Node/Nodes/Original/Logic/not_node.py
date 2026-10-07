from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class NotNode(Node):
    node_type = "NotNode"
    _class_ports = {
        "输入": PortDef("输入", PortDirection.Input, PortType.Bool),
        "输出": PortDef("输出", PortDirection.Output, PortType.Bool),
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
            node_type="NotNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["input_PortName"] = "输入"
        data["output_PortName"] = "输出"
        return data
