from typing import Any
from ...._Data.BuffType import BuffType
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class GetTravelEntryNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetTravelEntryNode"

    def __init__(self, buff_type: Any = BuffType.UnlockPlant, entry_index: int = 0, **kwargs: Any):
        super().__init__(**kwargs)
        bt = kwargs.get("buffType", kwargs.get("buff_type", buff_type))
        self.buffType: BuffType = validate_enum_field(bt, BuffType, "buffType", default=BuffType.UnlockPlant)
        self.entryIndex: int = int(kwargs.get("entryIndex", kwargs.get("entry_index", entry_index)))
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["GetTravelEntryNode"]
