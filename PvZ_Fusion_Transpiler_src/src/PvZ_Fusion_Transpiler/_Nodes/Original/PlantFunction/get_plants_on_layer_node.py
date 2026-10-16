from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetPlantsOnLayerNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetPlantsOnLayerNode"

    def __init__(self):
        super().__init__()
        self.port_output_plantlist_PlantList : Port = self.create_port("植物列表", PortDirection.Output, PortType.PlantList)


__all__ = ["GetPlantsOnLayerNode"]
