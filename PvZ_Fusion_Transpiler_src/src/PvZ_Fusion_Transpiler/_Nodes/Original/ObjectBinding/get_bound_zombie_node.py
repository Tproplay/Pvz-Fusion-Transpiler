from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetBoundZombieNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "GetBoundZombieNode"

    def __init__(self):
        super().__init__()
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["GetBoundZombieNode"]
