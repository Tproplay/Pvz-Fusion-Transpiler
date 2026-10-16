from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GameWinNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GameWinNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)


__all__ = ["GameWinNode"]
