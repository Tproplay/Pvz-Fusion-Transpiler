from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ModifyZombieHealthNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ModifyZombieHealthNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_input_float_HealthMultiplier : Port = self.create_port("血量倍率", PortDirection.Input, PortType.Float)
        self.port_output_trigger_ModifySuccess : Port = self.create_port("修改成功", PortDirection.Output, PortType.Trigger)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["ModifyZombieHealthNode"]
