from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DamagePlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "DamagePlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_float_Damage : Port = self.create_port("伤害值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_DamageComplete : Port = self.create_port("伤害完成", PortDirection.Output, PortType.Trigger)


__all__ = ["DamagePlantNode"]
