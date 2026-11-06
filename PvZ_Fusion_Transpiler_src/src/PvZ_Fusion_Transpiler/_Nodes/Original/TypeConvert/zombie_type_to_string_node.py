from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieTypeToStringNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ZombieTypeToStringNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombietype_Value : Port = self.create_port("Value", PortDirection.Input, PortType.ZombieType)
        self.port_output_string_String : Port = self.create_port("String", PortDirection.Output, PortType.String)


__all__ = ["ZombieTypeToStringNode"]
