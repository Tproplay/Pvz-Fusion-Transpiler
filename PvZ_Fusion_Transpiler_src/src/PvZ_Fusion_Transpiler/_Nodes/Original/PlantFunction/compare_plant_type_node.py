from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ComparePlantTypeNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ComparePlantTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttype_PlantTypeA : Port = self.create_port("植物类型A", PortDirection.Input, PortType.PlantType)
        self.port_input_planttype_PlantTypeB : Port = self.create_port("植物类型B", PortDirection.Input, PortType.PlantType)
        self.port_output_bool_Same : Port = self.create_port("相同", PortDirection.Output, PortType.Bool)


__all__ = ["ComparePlantTypeNode"]
