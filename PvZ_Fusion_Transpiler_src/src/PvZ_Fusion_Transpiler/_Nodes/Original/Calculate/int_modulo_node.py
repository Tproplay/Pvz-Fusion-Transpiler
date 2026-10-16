from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntModuloNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntModuloNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Dividend : Port = self.create_port("被除数", PortDirection.Input, PortType.Int)
        self.port_input_int_Divisor : Port = self.create_port("除数", PortDirection.Input, PortType.Int)
        self.port_output_int_Remainder : Port = self.create_port("余数", PortDirection.Output, PortType.Int)


__all__ = ["IntModuloNode"]
