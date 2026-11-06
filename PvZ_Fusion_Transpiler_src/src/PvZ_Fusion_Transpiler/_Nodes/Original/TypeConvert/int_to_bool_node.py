from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToBoolNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "IntToBoolNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Value : Port = self.create_port("Value", PortDirection.Input, PortType.Int)
        self.port_output_bool_Bool : Port = self.create_port("Boolean", PortDirection.Output, PortType.Bool)


__all__ = ["IntToBoolNode"]
