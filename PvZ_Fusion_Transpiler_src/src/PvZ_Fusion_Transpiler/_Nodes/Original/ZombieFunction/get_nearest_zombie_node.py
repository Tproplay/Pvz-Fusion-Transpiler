from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetNearestZombieNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetNearestZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["GetNearestZombieNode"]
