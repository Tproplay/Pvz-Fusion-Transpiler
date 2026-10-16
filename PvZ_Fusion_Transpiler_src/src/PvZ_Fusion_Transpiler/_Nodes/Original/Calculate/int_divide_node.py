from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntDivideNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntDivideNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Dividend : Port = self.create_port("被除数", PortDirection.Input, PortType.Int)
        self.port_input_int_Divisor : Port = self.create_port("除数", PortDirection.Input, PortType.Int)
        self.port_output_int_Quotient : Port = self.create_port("商", PortDirection.Output, PortType.Int)


__all__ = ["IntDivideNode"]
