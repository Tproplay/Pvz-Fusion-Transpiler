from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class StringVariableNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "StringVariableNode"

    def __init__(self):
        super().__init__()
        self.port_output_stringvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.StringVariable)


__all__ = ["StringVariableNode"]
