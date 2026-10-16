from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateInfoCardNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreateInfoCardNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_BigTitle : Port = self.create_port("大标题", PortDirection.Input, PortType.String)
        self.port_input_string_SmallTitle : Port = self.create_port("小标题", PortDirection.Input, PortType.String)
        self.port_output_trigger_OnCardClicked : Port = self.create_port("点击卡牌时触发", PortDirection.Output, PortType.Trigger)


__all__ = ["CreateInfoCardNode"]
