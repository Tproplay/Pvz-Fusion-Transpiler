from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BulletTypeValueNode(Node):
    node_type = "BulletTypeValueNode"
    _class_ports = {
        "子弹类型": PortDef("子弹类型", PortDirection.Output, PortType.BulletType),
    }

    def __init__(
        self,
        bullet_type: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="BulletTypeValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("bulletType", int(bullet_type))

    @property
    def bullet_type(self) -> int:
        return self.get_property("bulletType", 0)

    @bullet_type.setter
    def bullet_type(self, val: int) -> None:
        self.set_property("bulletType", int(val))
