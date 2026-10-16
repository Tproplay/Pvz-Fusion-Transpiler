from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnZombieDieNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OnZombieDieNode"

    def __init__(self):
        super().__init__()
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)


__all__ = ["OnZombieDieNode"]
