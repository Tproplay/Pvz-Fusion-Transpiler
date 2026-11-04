from typing import Any
from ...._Data.EventZombieStat import EventZombieStat
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class SetZombieStatsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "SetZombieStatsNode"

    def __init__(self, stat: Any = EventZombieStat.AttackPower, **kwargs: Any):
        super().__init__(**kwargs)
        s = kwargs.get("stat", stat)
        self.stat: EventZombieStat = validate_enum_field(s, EventZombieStat, "stat", default=EventZombieStat.AttackPower)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["SetZombieStatsNode"]
