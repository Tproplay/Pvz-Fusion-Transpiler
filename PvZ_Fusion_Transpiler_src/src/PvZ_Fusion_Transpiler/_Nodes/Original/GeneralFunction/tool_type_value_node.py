from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ToolTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ToolTypeValueNode"

    def __init__(self, value: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.value: int = int(value)
        self.port_output_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Output, PortType.ToolType)


__all__ = ["ToolTypeValueNode"]
