from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnWaveClearedNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OnWaveClearedNode"

    def __init__(self):
        super().__init__()
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)
        self.port_output_int_Wave : Port = self.create_port("波次", PortDirection.Output, PortType.Int)


__all__ = ["OnWaveClearedNode"]
