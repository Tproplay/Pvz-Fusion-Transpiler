from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetStringVariableValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetStringVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_stringvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.StringVariable)
        self.port_output_string_Value : Port = self.create_port("值", PortDirection.Output, PortType.String)


__all__ = ["GetStringVariableValueNode"]
