from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntVariableNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntVariableNode"

    def __init__(self):
        super().__init__()
        self.port_output_intvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.IntVariable)


__all__ = ["IntVariableNode"]
