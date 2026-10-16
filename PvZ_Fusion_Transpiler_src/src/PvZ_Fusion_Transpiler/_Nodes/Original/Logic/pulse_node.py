from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PulseNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PulseNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bool_State : Port = self.create_port("状态", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_OnPulse : Port = self.create_port("脉冲触发时", PortDirection.Output, PortType.Trigger)


__all__ = ["PulseNode"]
