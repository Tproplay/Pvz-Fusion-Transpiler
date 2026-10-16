from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetIntVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "SetIntVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_intvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.IntVariable)
        self.port_input_int_NewValue : Port = self.create_port("新值", PortDirection.Input, PortType.Int)
        self.port_output_intvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.IntVariable)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["SetIntVariableValueNode"]
