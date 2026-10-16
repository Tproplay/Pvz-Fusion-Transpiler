from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetZombieCardCooldownNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "SetZombieCardCooldownNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Input, PortType.ZombieType)
        self.port_input_float_TotalSeconds : Port = self.create_port("总秒数", PortDirection.Input, PortType.Float)
        self.port_input_float_RemainingSeconds : Port = self.create_port("剩余秒数", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_int_ModifiedCount : Port = self.create_port("修改数量", PortDirection.Output, PortType.Int)


__all__ = ["SetZombieCardCooldownNode"]
