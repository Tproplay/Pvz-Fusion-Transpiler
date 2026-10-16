from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetRandomPlantTypeNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetRandomPlantTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttypelist_PlantTypeList : Port = self.create_port("植物类型列表", PortDirection.Input, PortType.PlantTypeList)
        self.port_output_planttype_RandomPlantType : Port = self.create_port("随机植物类型", PortDirection.Output, PortType.PlantType)


__all__ = ["GetRandomPlantTypeNode"]
