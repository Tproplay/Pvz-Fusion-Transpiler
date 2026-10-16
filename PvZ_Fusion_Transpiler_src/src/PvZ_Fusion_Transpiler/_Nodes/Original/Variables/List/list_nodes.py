from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class AppendIntListNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "AppendIntListNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_int_Value : Port = self.create_port("值", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_listvariable_List : Port = self.create_port("列表", PortDirection.Output, PortType.ListVariable)


__all__ = ["AppendIntListNode"]
