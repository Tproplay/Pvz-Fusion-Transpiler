from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetToolCooldownNode(Node):
    node_type = "GetToolCooldownNode"
    _class_ports = {
        "工具类型": PortDef("工具类型", PortDirection.Input, PortType.ToolType),
        "冷却时间": PortDef("冷却时间", PortDirection.Output, PortType.Float),
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
            node_type="GetToolCooldownNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
