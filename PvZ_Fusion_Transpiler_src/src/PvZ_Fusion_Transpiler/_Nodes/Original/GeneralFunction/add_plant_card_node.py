from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class AddPlantCardNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "AddPlantCardNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_input_float_Cooldown : Port = self.create_port("冷却时间", PortDirection.Input, PortType.Float)
        self.port_input_int_Price : Port = self.create_port("价格", PortDirection.Input, PortType.Int)
        self.port_input_bool_UseDefaultData : Port = self.create_port("使用默认数据", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_AddSuccess : Port = self.create_port("添加成功", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_AddFailed : Port = self.create_port("添加失败", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_OnPlant : Port = self.create_port("种植时触发", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_PlantedPlant : Port = self.create_port("种植的植物", PortDirection.Output, PortType.Plant)


__all__ = ["AddPlantCardNode"]
