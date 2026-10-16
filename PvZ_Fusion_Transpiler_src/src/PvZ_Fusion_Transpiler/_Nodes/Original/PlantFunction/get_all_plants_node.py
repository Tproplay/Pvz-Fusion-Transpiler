from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetAllPlantsNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetAllPlantsNode"

    def __init__(self):
        super().__init__()
        self.port_output_plantlist_AllPlants : Port = self.create_port("全部植物", PortDirection.Output, PortType.PlantList)


__all__ = ["GetAllPlantsNode"]
