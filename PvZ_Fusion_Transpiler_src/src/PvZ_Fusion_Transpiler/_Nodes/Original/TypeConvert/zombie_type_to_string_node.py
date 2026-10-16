from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieTypeToStringNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ZombieTypeToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombietype_Value : Port = self.create_port("值", PortDirection.Input, PortType.ZombieType)
        self.port_output_string_String : Port = self.create_port("字符串", PortDirection.Output, PortType.String)


__all__ = ["ZombieTypeToStringNode"]
