from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "StringValueNode"

    def __init__(self, value: str = "默认文本", **kwargs: Any):
        super().__init__(**kwargs)
        self.value: str = str(value)
        self.port_output_string_Value : Port = self.create_port("值", PortDirection.Output, PortType.String)


__all__ = ["StringValueNode"]
