from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnPlantDeathCompleteNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OnPlantDeathCompleteNode"

    def __init__(self):
        super().__init__()
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)
        self.port_output_int_DeathReason : Port = self.create_port("死亡原因", PortDirection.Output, PortType.Int)


__all__ = ["OnPlantDeathCompleteNode"]
