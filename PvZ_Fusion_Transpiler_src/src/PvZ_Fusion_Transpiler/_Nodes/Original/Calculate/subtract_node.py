from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SubtractNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "SubtractNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Minuend : Port = self.create_port("被减数", PortDirection.Input, PortType.Float)
        self.port_input_float_Subtrahend : Port = self.create_port("减数", PortDirection.Input, PortType.Float)
        self.port_output_float_Diff : Port = self.create_port("差", PortDirection.Output, PortType.Float)


__all__ = ["SubtractNode"]
