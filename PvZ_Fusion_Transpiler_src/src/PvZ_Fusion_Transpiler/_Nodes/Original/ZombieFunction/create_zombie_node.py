from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateZombieNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreateZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Input, PortType.ZombieType)
        self.port_input_bool_IsHypnotized : Port = self.create_port("是否魅惑", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_OnCreated : Port = self.create_port("创建成功", PortDirection.Output, PortType.Trigger)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["CreateZombieNode"]
