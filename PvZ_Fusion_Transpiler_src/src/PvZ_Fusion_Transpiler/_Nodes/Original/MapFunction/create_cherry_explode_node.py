from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateCherryExplodeNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreateCherryExplodeNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_float_Damage : Port = self.create_port("伤害值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["CreateCherryExplodeNode"]
