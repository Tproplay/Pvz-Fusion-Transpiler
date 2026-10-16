from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OrNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OrNode"

    def __init__(self):
        super().__init__()
        self.port_input_bool_ConditionA : Port = self.create_port("条件A", PortDirection.Input, PortType.Bool)
        self.port_input_bool_ConditionB : Port = self.create_port("条件B", PortDirection.Input, PortType.Bool)
        self.port_output_bool_Result : Port = self.create_port("结果", PortDirection.Output, PortType.Bool)


__all__ = ["OrNode"]
