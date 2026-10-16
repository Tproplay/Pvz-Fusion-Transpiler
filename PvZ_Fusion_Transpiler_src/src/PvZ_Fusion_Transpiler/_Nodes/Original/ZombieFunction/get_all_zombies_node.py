from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetAllZombiesNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetAllZombiesNode"

    def __init__(self):
        super().__init__()
        self.port_output_zombielist_ZombieList : Port = self.create_port("僵尸列表", PortDirection.Output, PortType.ZombieList)


__all__ = ["GetAllZombiesNode"]
