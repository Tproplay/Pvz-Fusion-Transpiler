from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ChangeStageNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "ChangeStageNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["ChangeStageNode"]
