from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetPlantAttackSpeedNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetPlantAttackSpeedNode"

    def __init__(self):
        super().__init__()
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_output_float_Multiplier : Port = self.create_port("倍率", PortDirection.Output, PortType.Float)
        self.port_output_float_AttackInterval : Port = self.create_port("攻击间隔", PortDirection.Output, PortType.Float)


__all__ = ["GetPlantAttackSpeedNode"]
