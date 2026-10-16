from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MultiplyNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MultiplyNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_A : Port = self.create_port("A", PortDirection.Input, PortType.Float)
        self.port_input_float_B : Port = self.create_port("B", PortDirection.Input, PortType.Float)
        self.port_output_float_Product : Port = self.create_port("积", PortDirection.Output, PortType.Float)


__all__ = ["MultiplyNode"]
