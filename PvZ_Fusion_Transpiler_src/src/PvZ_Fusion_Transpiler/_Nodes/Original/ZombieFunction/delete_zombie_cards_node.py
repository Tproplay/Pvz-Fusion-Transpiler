from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DeleteZombieCardsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "DeleteZombieCardsNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Input, PortType.ZombieType)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_int_DeletedCount : Port = self.create_port("删除数量", PortDirection.Output, PortType.Int)


__all__ = ["DeleteZombieCardsNode"]
