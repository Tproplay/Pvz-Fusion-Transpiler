from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetZombieStatsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetZombieStatsNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_float_Value : Port = self.create_port("数值", PortDirection.Output, PortType.Float)


__all__ = ["GetZombieStatsNode"]
