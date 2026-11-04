from typing import Any
from ...._Data.EventBulletProperty import EventBulletProperty
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class ModifyEventBulletNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ModifyEventBulletNode"

    def __init__(self, prop: Any = EventBulletProperty.ScaleMultiplier, **kwargs: Any):
        super().__init__(**kwargs)
        p = kwargs.get("property", prop)
        self.property: EventBulletProperty = validate_enum_field(
            p, EventBulletProperty, "property", default=EventBulletProperty.ScaleMultiplier
        )
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bullet_Bullet : Port = self.create_port("子弹", PortDirection.Input, PortType.Bullet)
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["ModifyEventBulletNode"]
