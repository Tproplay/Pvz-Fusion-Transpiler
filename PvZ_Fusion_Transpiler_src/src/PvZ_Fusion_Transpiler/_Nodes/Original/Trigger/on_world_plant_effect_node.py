from typing import Any
from ...._Data.EventWorldEffect import EventWorldEffect
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class OnWorldPlantEffectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "OnWorldPlantEffectNode"

    def __init__(self, effect: Any = EventWorldEffect.IceShroom, **kwargs: Any):
        super().__init__(**kwargs)
        e = kwargs.get("effect", effect)
        self.effect: EventWorldEffect = validate_enum_field(
            e, EventWorldEffect, "effect", default=EventWorldEffect.IceShroom
        )
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)
        self.port_output_int_Row : Port = self.create_port("行", PortDirection.Output, PortType.Int)


__all__ = ["OnWorldPlantEffectNode"]
