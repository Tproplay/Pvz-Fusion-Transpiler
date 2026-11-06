from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToStringNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "IntToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Value : Port = self.create_port("Value", PortDirection.Input, PortType.Int)
        self.port_output_string_String : Port = self.create_port("String", PortDirection.Output, PortType.String)


__all__ = ["IntToStringNode"]
