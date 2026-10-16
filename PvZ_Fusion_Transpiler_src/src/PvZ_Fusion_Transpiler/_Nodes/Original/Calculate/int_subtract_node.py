from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntSubtractNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntSubtractNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Minuend : Port = self.create_port("被减数", PortDirection.Input, PortType.Int)
        self.port_input_int_Subtrahend : Port = self.create_port("减数", PortDirection.Input, PortType.Int)
        self.port_output_int_Diff : Port = self.create_port("差", PortDirection.Output, PortType.Int)


__all__ = ["IntSubtractNode"]
