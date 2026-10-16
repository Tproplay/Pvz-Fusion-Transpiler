from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateIceShroomEffectNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CreateIceShroomEffectNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_float_FreezeTime : Port = self.create_port("冻结时间", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["CreateIceShroomEffectNode"]
