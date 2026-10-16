from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RemoveTravelEntryNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "RemoveTravelEntryNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_NameOrId : Port = self.create_port("名称或编号", PortDirection.Input, PortType.String)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_bool_Removed : Port = self.create_port("已移除", PortDirection.Output, PortType.Bool)


__all__ = ["RemoveTravelEntryNode"]
