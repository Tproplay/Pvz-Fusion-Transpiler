from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetSunNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetSunNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_SunAmount : Port = self.create_port("阳光数量", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["GetSunNode"]
