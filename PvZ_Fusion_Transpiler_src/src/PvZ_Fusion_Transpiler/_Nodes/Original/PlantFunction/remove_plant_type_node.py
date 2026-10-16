from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RemovePlantTypeNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "RemovePlantTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttypelist_PlantTypeList : Port = self.create_port("植物类型列表", PortDirection.Input, PortType.PlantTypeList)
        self.port_input_planttype_TypeToRemove : Port = self.create_port("要删除的类型", PortDirection.Input, PortType.PlantType)
        self.port_output_planttypelist_ResultList : Port = self.create_port("结果列表", PortDirection.Output, PortType.PlantTypeList)
        self.port_output_bool_IsSuccess : Port = self.create_port("是否成功", PortDirection.Output, PortType.Bool)


__all__ = ["RemovePlantTypeNode"]
