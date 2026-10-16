from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToFloatNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntToFloatNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Int : Port = self.create_port("整数", PortDirection.Input, PortType.Int)
        self.port_output_float_Float : Port = self.create_port("浮点数", PortDirection.Output, PortType.Float)


__all__ = ["IntToFloatNode"]
