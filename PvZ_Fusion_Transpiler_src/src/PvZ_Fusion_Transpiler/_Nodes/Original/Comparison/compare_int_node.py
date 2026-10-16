from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CompareIntNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "CompareIntNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_ValueA : Port = self.create_port("值A", PortDirection.Input, PortType.Int)
        self.port_input_int_ValueB : Port = self.create_port("值B", PortDirection.Input, PortType.Int)
        self.port_output_bool_Greater : Port = self.create_port("大于", PortDirection.Output, PortType.Bool)
        self.port_output_bool_Less : Port = self.create_port("小于", PortDirection.Output, PortType.Bool)
        self.port_output_bool_Equal : Port = self.create_port("等于", PortDirection.Output, PortType.Bool)


__all__ = ["CompareIntNode"]
