from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class HealPlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "HealPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_float_HealAmount : Port = self.create_port("回血量", PortDirection.Input, PortType.Float)
        self.port_output_trigger_HealSuccess : Port = self.create_port("回血成功", PortDirection.Output, PortType.Trigger)


__all__ = ["HealPlantNode"]
