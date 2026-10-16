from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ToggleCycleNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ToggleCycleNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_float_CycleInterval : Port = self.create_port("周期间隔", PortDirection.Input, PortType.Float)
        self.port_output_trigger_OnCycle : Port = self.create_port("周期事件", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_OnEnable : Port = self.create_port("切换开始时", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_OnDisable : Port = self.create_port("切换关闭时", PortDirection.Output, PortType.Trigger)


__all__ = ["ToggleCycleNode"]
