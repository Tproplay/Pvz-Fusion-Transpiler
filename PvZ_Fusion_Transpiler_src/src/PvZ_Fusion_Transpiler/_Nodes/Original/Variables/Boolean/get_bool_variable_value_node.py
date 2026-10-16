from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetBoolVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetBoolVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_boolvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.BoolVariable)
        self.port_output_bool_Value : Port = self.create_port("值", PortDirection.Output, PortType.Bool)


__all__ = ["GetBoolVariableValueNode"]
