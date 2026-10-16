from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class IntAddNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "IntAddNode"

    def __init__(self):
        super().__init__()
        self.port_input_int_A : Port = self.create_port("A", PortDirection.Input, PortType.Int)
        self.port_input_int_B : Port = self.create_port("B", PortDirection.Input, PortType.Int)
        self.port_output_int_Sum : Port = self.create_port("和", PortDirection.Output, PortType.Int)


__all__ = ["IntAddNode"]
