from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DoOnceNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "DoOnceNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_trigger_Reset : Port = self.create_port("重置", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)


__all__ = ["DoOnceNode"]
