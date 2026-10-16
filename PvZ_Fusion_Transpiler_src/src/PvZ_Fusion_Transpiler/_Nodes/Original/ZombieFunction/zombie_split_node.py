from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieSplitNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ZombieSplitNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_int_Col : Port = self.create_port("列", PortDirection.Output, PortType.Int)
        self.port_output_int_Row : Port = self.create_port("行", PortDirection.Output, PortType.Int)
        self.port_output_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Output, PortType.ZombieType)
        self.port_output_bool_IsHypnotized : Port = self.create_port("是否被魅惑", PortDirection.Output, PortType.Bool)


__all__ = ["ZombieSplitNode"]
