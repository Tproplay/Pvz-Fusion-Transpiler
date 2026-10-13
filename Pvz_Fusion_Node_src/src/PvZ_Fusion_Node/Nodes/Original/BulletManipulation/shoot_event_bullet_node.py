from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ShootEventBulletNode(Node):
    node_type = "ShootEventBulletNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "子弹类型": PortDef("子弹类型", PortDirection.Input, PortType.BulletType),
        "位置": PortDef("位置", PortDirection.Input, PortType.Vector3),
        "子弹": PortDef("子弹", PortDirection.Output, PortType.Bullet),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ShootEventBulletNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
