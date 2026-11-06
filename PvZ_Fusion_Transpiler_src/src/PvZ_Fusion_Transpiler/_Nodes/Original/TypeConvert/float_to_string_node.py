from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatToStringNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "FloatToStringNode"

    def __init__(self):
        super().__init__()
        self.value_PortName: str = "Value"
        self.decimals_PortName: str = "Decimal Place"
        self.result_PortName: str = "String"
        self.port_input_float_Value : Port = self.create_port("Value", PortDirection.Input, PortType.Float)
        self.port_input_int_Decimals : Port = self.create_port("Decimal Place", PortDirection.Input, PortType.Int)
        self.port_output_string_String : Port = self.create_port("String", PortDirection.Output, PortType.String)


__all__ = ["FloatToStringNode"]
