from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateIceBlockNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreateIceBlockNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_planttype_FrozenPlant : Port = self.create_port("冻住的植物", PortDirection.Input, PortType.PlantType)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["CreateIceBlockNode"]
