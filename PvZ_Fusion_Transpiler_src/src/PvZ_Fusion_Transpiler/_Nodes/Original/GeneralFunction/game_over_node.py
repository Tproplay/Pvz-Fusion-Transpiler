from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GameOverNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GameOverNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_FailureReason : Port = self.create_port("失败原因", PortDirection.Input, PortType.String)


__all__ = ["GameOverNode"]
