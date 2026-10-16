from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CursePlantNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "CursePlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_input_float_CurseValue : Port = self.create_port("诅咒值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["CursePlantNode"]
