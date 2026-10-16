from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CounterNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CounterNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bool_IsReset : Port = self.create_port("是否重置", PortDirection.Input, PortType.Bool)
        self.port_output_int_Count : Port = self.create_port("计数", PortDirection.Output, PortType.Int)
        self.port_output_trigger_CountComplete : Port = self.create_port("计数完成", PortDirection.Output, PortType.Trigger)


__all__ = ["CounterNode"]
