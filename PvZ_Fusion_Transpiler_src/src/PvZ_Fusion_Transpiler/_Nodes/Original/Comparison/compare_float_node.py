from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CompareFloatNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CompareFloatNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_ValueA : Port = self.create_port("值A", PortDirection.Input, PortType.Float)
        self.port_input_float_ValueB : Port = self.create_port("值B", PortDirection.Input, PortType.Float)
        self.port_output_bool_Greater : Port = self.create_port("大于", PortDirection.Output, PortType.Bool)
        self.port_output_bool_Less : Port = self.create_port("小于", PortDirection.Output, PortType.Bool)
        self.port_output_bool_Equal : Port = self.create_port("等于", PortDirection.Output, PortType.Bool)


__all__ = ["CompareFloatNode"]
