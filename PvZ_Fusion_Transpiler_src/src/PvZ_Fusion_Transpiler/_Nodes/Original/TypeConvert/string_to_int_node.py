from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToIntNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToIntNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("String", PortDirection.Input, PortType.String)
        self.port_output_int_Value : Port = self.create_port("Value", PortDirection.Output, PortType.Int)
        self.port_output_bool_Valid : Port = self.create_port("Valid", PortDirection.Output, PortType.Bool)


__all__ = ["StringToIntNode"]
