from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetZombieTypeListItemNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetZombieTypeListItemNode"

    def __init__(self):
        super().__init__()
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_int_Index : Port = self.create_port("索引", PortDirection.Input, PortType.Int)
        self.port_output_zombietype_Value : Port = self.create_port("值", PortDirection.Output, PortType.ZombieType)
        self.port_output_bool_Valid : Port = self.create_port("有效", PortDirection.Output, PortType.Bool)


__all__ = ["GetZombieTypeListItemNode"]
