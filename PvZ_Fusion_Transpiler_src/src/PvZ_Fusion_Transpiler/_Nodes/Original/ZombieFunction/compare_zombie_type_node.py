from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CompareZombieTypeNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "CompareZombieTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombietype_ZombieTypeA : Port = self.create_port("僵尸类型A", PortDirection.Input, PortType.ZombieType)
        self.port_input_zombietype_ZombieTypeB : Port = self.create_port("僵尸类型B", PortDirection.Input, PortType.ZombieType)
        self.port_output_bool_Same : Port = self.create_port("相同", PortDirection.Output, PortType.Bool)


__all__ = ["CompareZombieTypeNode"]
