from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DamageZombieNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "DamageZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_input_float_Damage : Port = self.create_port("伤害值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["DamageZombieNode"]
