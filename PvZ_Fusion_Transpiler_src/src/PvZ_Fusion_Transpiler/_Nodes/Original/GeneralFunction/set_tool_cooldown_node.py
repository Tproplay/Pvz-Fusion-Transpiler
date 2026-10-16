from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetToolCooldownNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "SetToolCooldownNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Input, PortType.ToolType)
        self.port_input_float_TotalSeconds : Port = self.create_port("总秒数", PortDirection.Input, PortType.Float)
        self.port_input_float_RemainingSeconds : Port = self.create_port("剩余秒数", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["SetToolCooldownNode"]
