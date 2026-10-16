from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreatePlantCardNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreatePlantCardNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_Col : Port = self.create_port("列", PortDirection.Input, PortType.Int)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_output_trigger_OnCreated : Port = self.create_port("创建成功", PortDirection.Output, PortType.Trigger)
        self.port_output_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Output, PortType.PlantType)


__all__ = ["CreatePlantCardNode"]
