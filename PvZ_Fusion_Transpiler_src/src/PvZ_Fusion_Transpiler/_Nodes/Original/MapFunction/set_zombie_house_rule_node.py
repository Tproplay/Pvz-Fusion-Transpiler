from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class SetZombieHouseRuleNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "SetZombieHouseRuleNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bool_HouseEntryDefeat : Port = self.create_port("进家失败", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["SetZombieHouseRuleNode"]
