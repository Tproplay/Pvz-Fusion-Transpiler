from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RandomTriggerNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "RandomTriggerNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_TriggerCount : Port = self.create_port("触发数量", PortDirection.Input, PortType.Int)
        self.port_input_bool_RepeatTrigger : Port = self.create_port("重复触发", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)


__all__ = ["RandomTriggerNode"]
