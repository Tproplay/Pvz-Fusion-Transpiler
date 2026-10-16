from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DivideNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "DivideNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Dividend : Port = self.create_port("被除数", PortDirection.Input, PortType.Float)
        self.port_input_float_Divisor : Port = self.create_port("除数", PortDirection.Input, PortType.Float)
        self.port_output_float_Quotient : Port = self.create_port("商", PortDirection.Output, PortType.Float)


__all__ = ["DivideNode"]
