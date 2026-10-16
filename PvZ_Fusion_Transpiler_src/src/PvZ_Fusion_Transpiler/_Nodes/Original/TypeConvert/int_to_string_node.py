from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToStringNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "IntToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Value : Port = self.create_port("值", PortDirection.Input, PortType.Int)
        self.port_output_string_String : Port = self.create_port("字符串", PortDirection.Output, PortType.String)


__all__ = ["IntToStringNode"]
