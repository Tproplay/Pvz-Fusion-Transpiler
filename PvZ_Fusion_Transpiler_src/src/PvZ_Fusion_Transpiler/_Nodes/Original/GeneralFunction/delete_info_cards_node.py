from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DeleteInfoCardsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "DeleteInfoCardsNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_gameobject_CardObject : Port = self.create_port("卡牌对象", PortDirection.Input, PortType.GameObject)
        self.port_input_bool_All : Port = self.create_port("全部", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_int_DeletedCount : Port = self.create_port("删除数量", PortDirection.Output, PortType.Int)


__all__ = ["DeleteInfoCardsNode"]
