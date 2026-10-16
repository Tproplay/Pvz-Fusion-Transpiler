from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatToBoolNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "FloatToBoolNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_output_bool_Bool : Port = self.create_port("布尔值", PortDirection.Output, PortType.Bool)


__all__ = ["FloatToBoolNode"]
