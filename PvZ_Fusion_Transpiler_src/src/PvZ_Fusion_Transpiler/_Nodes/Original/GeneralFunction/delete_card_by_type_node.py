from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class DeleteCardByTypeNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "DeleteCardByTypeNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["DeleteCardByTypeNode"]
