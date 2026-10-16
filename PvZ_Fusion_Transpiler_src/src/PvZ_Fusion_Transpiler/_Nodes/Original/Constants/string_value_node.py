from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "StringValueNode"

    def __init__(self, value: str = "Default text", **kwargs):
        super().__init__(**kwargs)
        self.value: str = str(value)
        self.port_output_string_Value : Port = self.create_port("值", PortDirection.Output, PortType.String)


__all__ = ["StringValueNode"]
