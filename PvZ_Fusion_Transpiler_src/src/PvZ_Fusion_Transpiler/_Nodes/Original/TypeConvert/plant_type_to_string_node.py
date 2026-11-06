from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeToStringNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "PlantTypeToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_planttype_Value : Port = self.create_port("Value", PortDirection.Input, PortType.PlantType)
        self.port_output_string_String : Port = self.create_port("String", PortDirection.Output, PortType.String)


__all__ = ["PlantTypeToStringNode"]
