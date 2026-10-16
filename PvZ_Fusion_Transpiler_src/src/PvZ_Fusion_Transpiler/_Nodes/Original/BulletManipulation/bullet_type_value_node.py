from enum import Enum
from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BulletTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "BulletTypeValueNode"

    def __init__(self, value: Any = None, bullet_type: Any = None, bulletType: Any = None, **kwargs):
        super().__init__(**kwargs)
        bt = bulletType if bulletType is not None else (bullet_type if bullet_type is not None else value)
        if isinstance(bt, (int, float)) and not isinstance(bt, Enum):
            raise TypeError("BulletType must be handled through the BulletType enum, direct int input is not allowed.")
        if bt is not None:
            self.bulletType: int = int(getattr(bt, "value", bt))
        else:
            self.bulletType = 0
        self.value: int = self.bulletType
        self.port_output_bullettype_BulletType : Port = self.create_port("子弹类型", PortDirection.Output, PortType.BulletType)


__all__ = ["BulletTypeValueNode"]
