from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MultiPlantTypeListNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MultiPlantTypeListNode"

    def __init__(self):
        super().__init__()
        self.port_output_planttypelist_PlantTypeList : Port = self.create_port("植物类型列表", PortDirection.Output, PortType.PlantTypeList)


__all__ = ["MultiPlantTypeListNode"]
