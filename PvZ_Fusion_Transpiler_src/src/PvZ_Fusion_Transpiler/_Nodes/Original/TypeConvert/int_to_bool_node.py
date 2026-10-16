from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToBoolNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "IntToBoolNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Int)
        self.port_output_bool_Bool : Port = self.create_port("布尔值", PortDirection.Output, PortType.Bool)


__all__ = ["IntToBoolNode"]
