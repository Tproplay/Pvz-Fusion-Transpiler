from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ObjectToStringNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ObjectToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("Object", PortDirection.Input, PortType.GameObject)
        self.port_output_string_String : Port = self.create_port("Text", PortDirection.Output, PortType.String)


__all__ = ["ObjectToStringNode"]
