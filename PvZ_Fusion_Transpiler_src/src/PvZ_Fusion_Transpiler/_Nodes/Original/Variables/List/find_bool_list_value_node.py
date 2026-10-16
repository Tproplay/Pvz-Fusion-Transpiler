from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FindBoolListValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "FindBoolListValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_bool_Value : Port = self.create_port("值", PortDirection.Input, PortType.Bool)
        self.port_output_int_Index : Port = self.create_port("索引", PortDirection.Output, PortType.Int)
        self.port_output_bool_Contains : Port = self.create_port("包含", PortDirection.Output, PortType.Bool)


__all__ = ["FindBoolListValueNode"]
