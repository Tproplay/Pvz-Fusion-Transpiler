from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CompareToolTypeNode(Node):
    node_type = "CompareToolTypeNode"
    _class_ports = {
        "工具类型A": PortDef("工具类型A", PortDirection.Input, PortType.ToolType),
        "工具类型B": PortDef("工具类型B", PortDirection.Input, PortType.ToolType),
        "相同": PortDef("相同", PortDirection.Output, PortType.Bool),
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
            node_type="CompareToolTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
