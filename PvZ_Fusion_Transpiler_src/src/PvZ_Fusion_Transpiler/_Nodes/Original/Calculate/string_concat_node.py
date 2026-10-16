from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringConcatNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "StringConcatNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_A : Port = self.create_port("A", PortDirection.Input, PortType.String)
        self.port_input_string_B : Port = self.create_port("B", PortDirection.Input, PortType.String)
        self.port_output_string_Result : Port = self.create_port("结果", PortDirection.Output, PortType.String)


__all__ = ["StringConcatNode"]
