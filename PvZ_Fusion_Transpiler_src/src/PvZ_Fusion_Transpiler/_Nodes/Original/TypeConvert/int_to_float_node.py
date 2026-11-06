from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntToFloatNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "IntToFloatNode"

    def __init__(self):
        super().__init__()
        self.int_PortName: str = "Integer"
        self.float_PortName: str = "Float"
        self.port_input_int_Int : Port = self.create_port("Integer", PortDirection.Input, PortType.Int)
        self.port_output_float_Float : Port = self.create_port("Float", PortDirection.Output, PortType.Float)


__all__ = ["IntToFloatNode"]
