from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ToggleNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ToggleNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_bool_State : Port = self.create_port("状态", PortDirection.Output, PortType.Bool)
        self.port_output_trigger_OnStateChanged : Port = self.create_port("状态改变时", PortDirection.Output, PortType.Trigger)


__all__ = ["ToggleNode"]
