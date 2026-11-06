from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ObjectToZombieNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ObjectToZombieNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("Object", PortDirection.Input, PortType.GameObject)
        self.port_output_zombie_Zombie : Port = self.create_port("Zombie", PortDirection.Output, PortType.Zombie)
        self.port_output_bool_Exists : Port = self.create_port("Exists", PortDirection.Output, PortType.Bool)


__all__ = ["ObjectToZombieNode"]
