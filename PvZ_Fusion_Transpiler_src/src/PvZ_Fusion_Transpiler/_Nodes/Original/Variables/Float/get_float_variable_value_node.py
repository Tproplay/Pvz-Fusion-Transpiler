from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetFloatVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetFloatVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.FloatVariable)
        self.port_output_float_Value : Port = self.create_port("值", PortDirection.Output, PortType.Float)


__all__ = ["GetFloatVariableValueNode"]
