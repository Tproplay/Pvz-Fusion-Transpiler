from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_int_Value : Port = self.create_port("值", PortDirection.Output, PortType.Int)


__all__ = ["IntValueNode"]
