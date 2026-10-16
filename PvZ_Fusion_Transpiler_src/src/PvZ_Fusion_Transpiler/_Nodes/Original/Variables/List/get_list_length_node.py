from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetListLengthNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetListLengthNode"

    def __init__(self):
        super().__init__()
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_output_int_Length : Port = self.create_port("长度", PortDirection.Output, PortType.Int)


__all__ = ["GetListLengthNode"]
