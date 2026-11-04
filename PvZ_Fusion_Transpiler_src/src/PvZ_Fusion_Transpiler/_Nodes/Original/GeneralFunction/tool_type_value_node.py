from typing import Any
from ...._Data.ToolType import ToolType
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class ToolTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ToolTypeValueNode"

    def __init__(self, tool_type: Any = ToolType.Shovel, value: Any = None, toolType: Any = None, **kwargs: Any):
        super().__init__(**kwargs)
        tt = toolType if toolType is not None else (tool_type if value is None else value)
        validated = validate_enum_field(tt, ToolType, "tool_type", default=ToolType.Shovel)
        self.toolType: ToolType = validated
        self.value: int = int(validated.value)
        self.port_output_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Output, PortType.ToolType)


__all__ = ["ToolTypeValueNode"]
