from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetPlantsInCellNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetPlantsInCellNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_output_plantlist_PlantList : Port = self.create_port("植物列表", PortDirection.Output, PortType.PlantList)


__all__ = ["GetPlantsInCellNode"]
