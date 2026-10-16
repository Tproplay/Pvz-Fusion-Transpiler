from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ChangeEventMapNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ChangeEventMapNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_string_FailureReason : Port = self.create_port("失败原因", PortDirection.Output, PortType.String)


__all__ = ["ChangeEventMapNode"]
