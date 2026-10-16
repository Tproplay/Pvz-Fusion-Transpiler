from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class LogarithmNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "LogarithmNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_input_float_Base : Port = self.create_port("底数", PortDirection.Input, PortType.Float)
        self.port_output_float_Result : Port = self.create_port("结果", PortDirection.Output, PortType.Float)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["LogarithmNode"]
