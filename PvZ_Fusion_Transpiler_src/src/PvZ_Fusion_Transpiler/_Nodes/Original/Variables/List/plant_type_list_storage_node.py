from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeListStorageNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlantTypeListStorageNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_planttypelist_List : Port = self.create_port("列表", PortDirection.Input, PortType.PlantTypeList)
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_output_planttypelist_CurrentList : Port = self.create_port("当前列表", PortDirection.Output, PortType.PlantTypeList)
        self.port_output_int_ListLength : Port = self.create_port("列表长度", PortDirection.Output, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["PlantTypeListStorageNode"]
