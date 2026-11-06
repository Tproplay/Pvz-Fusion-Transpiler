from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatToIntNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "FloatToIntNode"

    def __init__(self):
        super().__init__()
        self.float_PortName: str = "Float"
        self.int_PortName: str = "Integer"
        self.port_input_float_Float : Port = self.create_port("Float", PortDirection.Input, PortType.Float)
        self.port_output_int_Int : Port = self.create_port("Integer", PortDirection.Output, PortType.Int)


__all__ = ["FloatToIntNode"]
