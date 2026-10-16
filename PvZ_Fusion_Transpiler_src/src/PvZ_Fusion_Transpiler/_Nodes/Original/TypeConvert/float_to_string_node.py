from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatToStringNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "FloatToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_input_int_Decimals : Port = self.create_port("小数位数", PortDirection.Input, PortType.Int)
        self.port_output_string_String : Port = self.create_port("字符串", PortDirection.Output, PortType.String)


__all__ = ["FloatToStringNode"]
