from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CopyListValuesNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "CopyListValuesNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_listvariable_SourceList : Port = self.create_port("源列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_listvariable_TargetList : Port = self.create_port("目标列表", PortDirection.Input, PortType.ListVariable)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["CopyListValuesNode"]
