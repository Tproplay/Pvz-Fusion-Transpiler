from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RandomFloatNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "RandomFloatNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Min : Port = self.create_port("最小值", PortDirection.Input, PortType.Float)
        self.port_input_float_Max : Port = self.create_port("最大值", PortDirection.Input, PortType.Float)
        self.port_output_float_RandomFloat : Port = self.create_port("随机浮点数", PortDirection.Output, PortType.Float)


__all__ = ["RandomFloatNode"]
