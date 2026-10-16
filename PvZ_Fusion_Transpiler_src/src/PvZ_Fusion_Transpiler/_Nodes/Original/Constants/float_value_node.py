from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "FloatValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_float_Value : Port = self.create_port("值", PortDirection.Output, PortType.Float)


__all__ = ["FloatValueNode"]
