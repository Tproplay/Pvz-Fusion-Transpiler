from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MergePlantTypeListsNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MergePlantTypeListsNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttypelist_ListA : Port = self.create_port("列表A", PortDirection.Input, PortType.PlantTypeList)
        self.port_input_planttypelist_ListB : Port = self.create_port("列表B", PortDirection.Input, PortType.PlantTypeList)
        self.port_output_planttypelist_MergedList : Port = self.create_port("合并列表", PortDirection.Output, PortType.PlantTypeList)
        self.port_output_int_ListLength : Port = self.create_port("列表长度", PortDirection.Output, PortType.Int)


__all__ = ["MergePlantTypeListsNode"]
