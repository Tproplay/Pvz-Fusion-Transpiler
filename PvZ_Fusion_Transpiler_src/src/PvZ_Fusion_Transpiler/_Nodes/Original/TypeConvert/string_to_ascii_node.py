from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToAsciiNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToAsciiNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("字符串", PortDirection.Input, PortType.String)
        self.port_input_int_Index : Port = self.create_port("索引", PortDirection.Input, PortType.Int)
        self.port_output_int_AsciiCode : Port = self.create_port("ASCII码", PortDirection.Output, PortType.Int)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["StringToAsciiNode"]
