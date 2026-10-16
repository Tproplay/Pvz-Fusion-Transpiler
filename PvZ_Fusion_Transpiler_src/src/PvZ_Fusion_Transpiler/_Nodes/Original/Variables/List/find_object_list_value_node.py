from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class FindObjectListValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "FindObjectListValueNode"

    def __init__(self):
        super().__init__()
        self.port_input_listvariable_List : Port = self.create_port("列表", PortDirection.Input, PortType.ListVariable)
        self.port_input_gameobject_Value : Port = self.create_port("值", PortDirection.Input, PortType.GameObject)
        self.port_output_int_Index : Port = self.create_port("索引", PortDirection.Output, PortType.Int)
        self.port_output_bool_Contains : Port = self.create_port("包含", PortDirection.Output, PortType.Bool)


__all__ = ["FindObjectListValueNode"]
