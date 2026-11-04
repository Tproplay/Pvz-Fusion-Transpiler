from typing import Any
from ...._Data.BulletType import BulletType
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class BulletTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "BulletTypeValueNode"

    def __init__(self, value: Any = None, bullet_type: Any = None, bulletType: Any = None, **kwargs: Any):
        super().__init__(**kwargs)
        bt = bulletType if bulletType is not None else (bullet_type if bullet_type is not None else value)
        validated = validate_enum_field(bt, BulletType, "bullet_type", default=BulletType.Bullet_pea)
        self.bulletType: BulletType = validated
        self.value: int = int(validated.value)
        self.port_output_bullettype_BulletType : Port = self.create_port("子弹类型", PortDirection.Output, PortType.BulletType)


__all__ = ["BulletTypeValueNode"]
