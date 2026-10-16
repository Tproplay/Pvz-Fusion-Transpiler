from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DeleteGridItemsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "DeleteGridItemsNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_int_DeletedCount : Port = self.create_port("删除数量", PortDirection.Output, PortType.Int)


__all__ = ["DeleteGridItemsNode"]
