from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ForEachPlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ForEachPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plantlist_PlantList : Port = self.create_port("植物列表", PortDirection.Input, PortType.PlantList)
        self.port_output_trigger_LoopBody : Port = self.create_port("循环体", PortDirection.Output, PortType.Trigger)
        self.port_output_plant_CurrentPlant : Port = self.create_port("当前植物", PortDirection.Output, PortType.Plant)
        self.port_output_int_Index : Port = self.create_port("当前索引", PortDirection.Output, PortType.Int)
        self.port_output_trigger_LoopComplete : Port = self.create_port("循环完成", PortDirection.Output, PortType.Trigger)


__all__ = ["ForEachPlantNode"]
