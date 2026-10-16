from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ObjectToStringNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ObjectToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Input, PortType.GameObject)
        self.port_output_string_String : Port = self.create_port("文本", PortDirection.Output, PortType.String)


__all__ = ["ObjectToStringNode"]
