from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FeedGoldenBeanNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "FeedGoldenBeanNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_bool_Effective : Port = self.create_port("已生效", PortDirection.Output, PortType.Bool)


__all__ = ["FeedGoldenBeanNode"]
