from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatVariableArithmeticNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "FloatVariableArithmeticNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.FloatVariable)
        self.port_input_float_Operand : Port = self.create_port("操作数", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.FloatVariable)
        self.port_output_float_Result : Port = self.create_port("结果", PortDirection.Output, PortType.Float)


__all__ = ["FloatVariableArithmeticNode"]
