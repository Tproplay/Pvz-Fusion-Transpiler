from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ForEachZombieNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ForEachZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombielist_ZombieList : Port = self.create_port("僵尸列表", PortDirection.Input, PortType.ZombieList)
        self.port_output_trigger_Loop : Port = self.create_port("每次循环", PortDirection.Output, PortType.Trigger)
        self.port_output_zombie_CurrentZombie : Port = self.create_port("当前僵尸", PortDirection.Output, PortType.Zombie)
        self.port_output_int_Index : Port = self.create_port("索引", PortDirection.Output, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["ForEachZombieNode"]
