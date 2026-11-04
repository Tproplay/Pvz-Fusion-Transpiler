from typing import Any
from ...._Data.EventZombieStatus import EventZombieStatus
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class GetZombieStatusNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetZombieStatusNode"

    def __init__(self, status: Any = EventZombieStatus.ChillSeconds, **kwargs: Any):
        super().__init__(**kwargs)
        s = kwargs.get("status", status)
        self.status: EventZombieStatus = validate_enum_field(s, EventZombieStatus, "status", default=EventZombieStatus.ChillSeconds)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_float_Value : Port = self.create_port("数值", PortDirection.Output, PortType.Float)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["GetZombieStatusNode"]
