from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FloatValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "FloatValueNode"

    def __init__(self, value: float = 3.0, **kwargs):
        super().__init__(**kwargs)
        self.value: float = float(value)
        self.port_output_float_Value : Port = self.create_port("值", PortDirection.Output, PortType.Float)


__all__ = ["FloatValueNode"]
