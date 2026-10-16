from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class NotNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "NotNode"

    def __init__(self):
        super().__init__()
        self.port_input_bool_Input : Port = self.create_port("输入", PortDirection.Input, PortType.Bool)
        self.port_output_bool_Output : Port = self.create_port("输出", PortDirection.Output, PortType.Bool)


__all__ = ["NotNode"]
