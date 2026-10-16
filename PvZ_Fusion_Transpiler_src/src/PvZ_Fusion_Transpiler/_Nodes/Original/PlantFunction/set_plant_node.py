from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetPlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "SetPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_planttype_PlantType : Port = self.create_port("植物编号", PortDirection.Input, PortType.PlantType)
        self.port_input_bool_ForcePlant : Port = self.create_port("强制种植", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_OnCreated : Port = self.create_port("创建成功", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_OnFailed : Port = self.create_port("创建失败", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)


__all__ = ["SetPlantNode"]
