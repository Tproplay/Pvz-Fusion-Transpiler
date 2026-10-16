from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ShowTextNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ShowTextNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_Text : Port = self.create_port("文本", PortDirection.Input, PortType.String)
        self.port_input_float_Duration : Port = self.create_port("持续时间", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["ShowTextNode"]
