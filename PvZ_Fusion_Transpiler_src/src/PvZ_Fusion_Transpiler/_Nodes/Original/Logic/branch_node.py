from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BranchNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "BranchNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bool_Condition : Port = self.create_port("条件", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Then : Port = self.create_port("真（触发）", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Else : Port = self.create_port("假（停止）", PortDirection.Output, PortType.Trigger)


__all__ = ["BranchNode"]
