from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatToBoolNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "FloatToBoolNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Value : Port = self.create_port("Value", PortDirection.Input, PortType.Float)
        self.port_output_bool_Bool : Port = self.create_port("Boolean", PortDirection.Output, PortType.Bool)


__all__ = ["FloatToBoolNode"]
