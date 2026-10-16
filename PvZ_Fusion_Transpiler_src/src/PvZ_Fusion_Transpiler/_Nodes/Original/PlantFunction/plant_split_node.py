from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantSplitNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlantSplitNode"

    def __init__(self):
        super().__init__()
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_output_int_Col : Port = self.create_port("列", PortDirection.Output, PortType.Int)
        self.port_output_int_Row : Port = self.create_port("行", PortDirection.Output, PortType.Int)
        self.port_output_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Output, PortType.PlantType)
        self.port_output_float_PlantHealth : Port = self.create_port("植物血量", PortDirection.Output, PortType.Float)
        self.port_output_float_PropertyCountdown : Port = self.create_port("属性倒计时", PortDirection.Output, PortType.Float)


__all__ = ["PlantSplitNode"]
