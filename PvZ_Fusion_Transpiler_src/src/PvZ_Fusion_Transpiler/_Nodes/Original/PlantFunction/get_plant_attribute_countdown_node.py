from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetPlantAttributeCountdownNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetPlantAttributeCountdownNode"

    def __init__(self):
        super().__init__()
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_output_float_RemainingSeconds : Port = self.create_port("剩余秒数", PortDirection.Output, PortType.Float)
        self.port_output_float_MaxSeconds : Port = self.create_port("最大秒数", PortDirection.Output, PortType.Float)


__all__ = ["GetPlantAttributeCountdownNode"]
