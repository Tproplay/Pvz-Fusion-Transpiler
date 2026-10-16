from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetFloatVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "SetFloatVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.FloatVariable)
        self.port_input_float_NewValue : Port = self.create_port("新值", PortDirection.Input, PortType.Float)
        self.port_output_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.FloatVariable)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["SetFloatVariableValueNode"]
