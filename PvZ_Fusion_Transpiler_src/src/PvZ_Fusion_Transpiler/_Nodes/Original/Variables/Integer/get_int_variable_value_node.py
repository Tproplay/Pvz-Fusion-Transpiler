from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetIntVariableValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetIntVariableValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_intvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.IntVariable)
        self.port_output_int_Value : Port = self.create_port("值", PortDirection.Output, PortType.Int)


__all__ = ["GetIntVariableValueNode"]
