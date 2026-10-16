from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MoveZombieNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MoveZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_input_int_TargetCol : Port = self.create_port("目标列", PortDirection.Input, PortType.Int)
        self.port_input_int_TargetRow : Port = self.create_port("目标行", PortDirection.Input, PortType.Int)
        self.port_output_trigger_MoveSuccess : Port = self.create_port("移动成功", PortDirection.Output, PortType.Trigger)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["MoveZombieNode"]
