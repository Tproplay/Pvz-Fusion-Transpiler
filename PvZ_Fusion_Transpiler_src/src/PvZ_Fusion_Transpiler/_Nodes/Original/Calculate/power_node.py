from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PowerNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "PowerNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_input_float_Exponent : Port = self.create_port("指数", PortDirection.Input, PortType.Float)
        self.port_output_float_Result : Port = self.create_port("结果", PortDirection.Output, PortType.Float)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["PowerNode"]
