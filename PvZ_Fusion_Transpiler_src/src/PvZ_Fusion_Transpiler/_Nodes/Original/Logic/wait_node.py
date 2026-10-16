from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class WaitNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "WaitNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_float_Duration : Port = self.create_port("等待时间", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)


__all__ = ["WaitNode"]
