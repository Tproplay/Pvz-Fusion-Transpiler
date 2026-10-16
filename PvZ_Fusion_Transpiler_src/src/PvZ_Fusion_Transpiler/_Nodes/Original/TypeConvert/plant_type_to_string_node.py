from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeToStringNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "PlantTypeToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttype_Value : Port = self.create_port("值", PortDirection.Input, PortType.PlantType)
        self.port_output_string_String : Port = self.create_port("字符串", PortDirection.Output, PortType.String)


__all__ = ["PlantTypeToStringNode"]
