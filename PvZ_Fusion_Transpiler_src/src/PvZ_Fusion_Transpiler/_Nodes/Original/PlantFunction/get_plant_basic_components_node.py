from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetPlantBasicComponentsNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetPlantBasicComponentsNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_output_planttypelist_PlantTypeList : Port = self.create_port("植物类型列表", PortDirection.Output, PortType.PlantTypeList)


__all__ = ["GetPlantBasicComponentsNode"]
