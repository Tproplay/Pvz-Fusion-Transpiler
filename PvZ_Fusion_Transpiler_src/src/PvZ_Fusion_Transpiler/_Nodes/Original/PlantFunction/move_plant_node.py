from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MovePlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MovePlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_bool_Force : Port = self.create_port("强制", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_MoveSuccess : Port = self.create_port("移动成功", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)


__all__ = ["MovePlantNode"]
