from typing import Any
from ...._Data.EventZombieStat import EventZombieStat
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class GetZombieStatsNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetZombieStatsNode"

    def __init__(self, stat: Any = EventZombieStat.AttackPower, **kwargs: Any):
        super().__init__(**kwargs)
        s = kwargs.get("stat", stat)
        self.stat: EventZombieStat = validate_enum_field(s, EventZombieStat, "stat", default=EventZombieStat.AttackPower)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_float_Value : Port = self.create_port("数值", PortDirection.Output, PortType.Float)


__all__ = ["GetZombieStatsNode"]
