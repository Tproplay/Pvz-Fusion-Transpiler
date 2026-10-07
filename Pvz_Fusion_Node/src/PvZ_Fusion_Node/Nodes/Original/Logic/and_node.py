from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class AndNode(Node):
    node_type = "AndNode"
    _class_ports = {
        "条件A": PortDef("条件A", PortDirection.Input, PortType.Bool),
        "条件B": PortDef("条件B", PortDirection.Input, PortType.Bool),
        "结果": PortDef("结果", PortDirection.Output, PortType.Bool),
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
            node_type="AndNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["a_PortName"] = "条件A"
        data["b_PortName"] = "条件B"
        data["output_PortName"] = "结果"
        return data
