from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BoolValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "BoolValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_bool_Value : Port = self.create_port("值", PortDirection.Output, PortType.Bool)


__all__ = ["BoolValueNode"]
