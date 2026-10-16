from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ModifyPlantHealthNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ModifyPlantHealthNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_float_HealthBonus : Port = self.create_port("血量加成x100%", PortDirection.Input, PortType.Float)
        self.port_output_trigger_ModifySuccess : Port = self.create_port("修改成功", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)


__all__ = ["ModifyPlantHealthNode"]
