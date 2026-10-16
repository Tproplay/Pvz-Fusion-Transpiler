from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnGameStartNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OnGameStartNode"

    def __init__(self):
        super().__init__()
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)


__all__ = ["OnGameStartNode"]
