from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieToObjectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ZombieToObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Output, PortType.GameObject)


__all__ = ["ZombieToObjectNode"]
