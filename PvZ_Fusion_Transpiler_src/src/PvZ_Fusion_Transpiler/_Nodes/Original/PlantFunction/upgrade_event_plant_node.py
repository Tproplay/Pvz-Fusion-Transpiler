from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class UpgradeEventPlantNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "UpgradeEventPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_int_TargetLevel : Port = self.create_port("目标等级", PortDirection.Input, PortType.Int)
        self.port_input_bool_Star : Port = self.create_port("星辉", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["UpgradeEventPlantNode"]
