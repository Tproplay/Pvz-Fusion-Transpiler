from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetZombieStatusNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetZombieStatusNode"

    def __init__(self):
        super().__init__()
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_float_Value : Port = self.create_port("数值", PortDirection.Output, PortType.Float)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["GetZombieStatusNode"]
