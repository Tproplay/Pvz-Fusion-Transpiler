from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToFloatNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToFloatNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("字符串", PortDirection.Input, PortType.String)
        self.port_output_float_Value : Port = self.create_port("值", PortDirection.Output, PortType.Float)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["StringToFloatNode"]
