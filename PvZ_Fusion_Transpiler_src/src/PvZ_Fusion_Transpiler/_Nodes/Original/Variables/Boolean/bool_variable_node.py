from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BoolVariableNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "BoolVariableNode"

    def __init__(self):
        super().__init__()
        self.port_output_boolvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.BoolVariable)


__all__ = ["BoolVariableNode"]
