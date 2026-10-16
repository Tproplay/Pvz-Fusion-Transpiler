from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToPlantTypeNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToPlantTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("字符串", PortDirection.Input, PortType.String)
        self.port_output_planttype_Value : Port = self.create_port("值", PortDirection.Output, PortType.PlantType)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["StringToPlantTypeNode"]
