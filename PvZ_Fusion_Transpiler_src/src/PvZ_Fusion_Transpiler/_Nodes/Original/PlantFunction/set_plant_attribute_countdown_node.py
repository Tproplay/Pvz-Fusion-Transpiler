from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetPlantAttributeCountdownNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "SetPlantAttributeCountdownNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_float_RemainingSeconds : Port = self.create_port("剩余秒数", PortDirection.Input, PortType.Float)
        self.port_input_float_MaxSeconds : Port = self.create_port("最大秒数", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["SetPlantAttributeCountdownNode"]
