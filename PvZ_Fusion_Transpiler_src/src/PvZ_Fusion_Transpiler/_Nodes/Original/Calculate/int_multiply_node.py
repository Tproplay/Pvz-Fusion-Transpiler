from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntMultiplyNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntMultiplyNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_A : Port = self.create_port("A", PortDirection.Input, PortType.Int)
        self.port_input_int_B : Port = self.create_port("B", PortDirection.Input, PortType.Int)
        self.port_output_int_Product : Port = self.create_port("积", PortDirection.Output, PortType.Int)


__all__ = ["IntMultiplyNode"]
