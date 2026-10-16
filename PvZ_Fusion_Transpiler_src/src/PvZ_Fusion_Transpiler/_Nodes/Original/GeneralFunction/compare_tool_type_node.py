from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CompareToolTypeNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "CompareToolTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_tooltype_A : Port = self.create_port("A", PortDirection.Input, PortType.ToolType)
        self.port_input_tooltype_B : Port = self.create_port("B", PortDirection.Input, PortType.ToolType)
        self.port_output_bool_Equal : Port = self.create_port("相等", PortDirection.Output, PortType.Bool)


__all__ = ["CompareToolTypeNode"]
