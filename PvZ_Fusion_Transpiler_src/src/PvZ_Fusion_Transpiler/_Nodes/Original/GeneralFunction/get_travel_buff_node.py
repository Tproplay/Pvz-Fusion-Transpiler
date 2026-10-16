from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetTravelBuffNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetTravelBuffNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Success : Port = self.create_port("成功", PortDirection.Output, PortType.Trigger)


__all__ = ["GetTravelBuffNode"]
