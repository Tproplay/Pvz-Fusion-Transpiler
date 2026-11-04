from typing import Any
from ...._Data.EventZombieStatus import EventZombieStatus
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class SetZombieStatusNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "SetZombieStatusNode"

    def __init__(self, status: Any = EventZombieStatus.ChillSeconds, **kwargs: Any):
        super().__init__(**kwargs)
        s = kwargs.get("status", status)
        self.status: EventZombieStatus = validate_enum_field(s, EventZombieStatus, "status", default=EventZombieStatus.ChillSeconds)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["SetZombieStatusNode"]
