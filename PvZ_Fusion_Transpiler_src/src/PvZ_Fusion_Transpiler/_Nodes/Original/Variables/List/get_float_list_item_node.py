from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetFloatListItemNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetFloatListItemNode"

    def __init__(self):
        super().__init__()
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_int_Index : Port = self.create_port("索引", PortDirection.Input, PortType.Int)
        self.port_output_float_Value : Port = self.create_port("值", PortDirection.Output, PortType.Float)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["GetFloatListItemNode"]
