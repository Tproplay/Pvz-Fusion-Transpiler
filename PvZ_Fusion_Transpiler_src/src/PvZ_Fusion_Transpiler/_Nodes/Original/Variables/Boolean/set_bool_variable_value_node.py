from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetBoolVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "SetBoolVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_boolvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.BoolVariable)
        self.port_input_bool_NewValue : Port = self.create_port("新值", PortDirection.Input, PortType.Bool)
        self.port_output_boolvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.BoolVariable)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["SetBoolVariableValueNode"]
