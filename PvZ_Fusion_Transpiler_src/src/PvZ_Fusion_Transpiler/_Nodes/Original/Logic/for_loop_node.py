from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ForLoopNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ForLoopNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_LoopCount : Port = self.create_port("循环次数", PortDirection.Input, PortType.Int)
        self.port_output_trigger_LoopBody : Port = self.create_port("循环体", PortDirection.Output, PortType.Trigger)
        self.port_output_int_Index : Port = self.create_port("当前索引", PortDirection.Output, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["ForLoopNode"]
