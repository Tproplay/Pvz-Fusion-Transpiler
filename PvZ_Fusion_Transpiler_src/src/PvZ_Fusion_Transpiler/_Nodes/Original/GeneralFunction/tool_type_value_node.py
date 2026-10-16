from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ToolTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ToolTypeValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Output, PortType.ToolType)


__all__ = ["ToolTypeValueNode"]
