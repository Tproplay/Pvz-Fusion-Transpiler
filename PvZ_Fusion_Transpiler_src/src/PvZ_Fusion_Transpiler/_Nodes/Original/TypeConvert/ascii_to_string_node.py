from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class AsciiToStringNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "AsciiToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_AsciiCode : Port = self.create_port("ASCII码", PortDirection.Input, PortType.Int)
        self.port_output_string_String : Port = self.create_port("字符串", PortDirection.Output, PortType.String)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["AsciiToStringNode"]
