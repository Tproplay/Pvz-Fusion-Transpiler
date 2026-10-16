from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class RepeatUntilNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "RepeatUntilNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bool_Condition : Port = self.create_port("条件", PortDirection.Input, PortType.Bool)
        self.port_input_float_IntervalSeconds : Port = self.create_port("间隔秒数", PortDirection.Input, PortType.Float)
        self.port_input_int_MaxChecks : Port = self.create_port("最多检查次数", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Timeout : Port = self.create_port("超时", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Loop : Port = self.create_port("每次循环", PortDirection.Output, PortType.Trigger)


__all__ = ["RepeatUntilNode"]
