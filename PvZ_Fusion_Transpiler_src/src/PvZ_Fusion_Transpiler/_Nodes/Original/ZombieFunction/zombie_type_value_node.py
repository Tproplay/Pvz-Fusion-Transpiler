from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieTypeValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ZombieTypeValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Output, PortType.ZombieType)


__all__ = ["ZombieTypeValueNode"]
