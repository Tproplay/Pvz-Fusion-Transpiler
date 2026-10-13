from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ToolTypeValueNode(Node):
    node_type = "ToolTypeValueNode"
    _class_ports = {
        "工具类型": PortDef("工具类型", PortDirection.Output, PortType.ToolType),
    }

    def __init__(
        self,
        tool_type: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ToolTypeValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("toolType", int(tool_type))

    @property
    def tool_type(self) -> int:
        return self.get_property("toolType", 0)

    @tool_type.setter
    def tool_type(self, val: int) -> None:
        self.set_property("toolType", int(val))
