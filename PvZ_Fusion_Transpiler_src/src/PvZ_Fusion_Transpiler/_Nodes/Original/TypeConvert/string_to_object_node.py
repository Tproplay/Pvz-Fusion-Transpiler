from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringToObjectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "StringToObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_string_String : Port = self.create_port("文本", PortDirection.Input, PortType.String)
        self.port_output_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Output, PortType.GameObject)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["StringToObjectNode"]
