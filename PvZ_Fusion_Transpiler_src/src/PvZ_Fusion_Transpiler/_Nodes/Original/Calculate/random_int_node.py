from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RandomIntNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "RandomIntNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Min : Port = self.create_port("最小值", PortDirection.Input, PortType.Int)
        self.port_input_int_Max : Port = self.create_port("最大值", PortDirection.Input, PortType.Int)
        self.port_output_int_RandomInt : Port = self.create_port("随机整数", PortDirection.Output, PortType.Int)


__all__ = ["RandomIntNode"]
