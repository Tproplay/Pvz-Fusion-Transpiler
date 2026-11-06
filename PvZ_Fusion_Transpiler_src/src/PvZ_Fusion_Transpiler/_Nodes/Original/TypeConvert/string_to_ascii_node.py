from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToAsciiNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToAsciiNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("String", PortDirection.Input, PortType.String)
        self.port_input_int_Index : Port = self.create_port("Index", PortDirection.Input, PortType.Int)
        self.port_output_int_AsciiCode : Port = self.create_port("ASCII Code", PortDirection.Output, PortType.Int)
        self.port_output_bool_Valid : Port = self.create_port("Valid", PortDirection.Output, PortType.Bool)


__all__ = ["StringToAsciiNode"]
