from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ModifyEventBulletNode(Node):
    node_type = "ModifyEventBulletNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "子弹": PortDef("子弹", PortDirection.Input, PortType.Bullet),
        "数值": PortDef("数值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        property_id: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ModifyEventBulletNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("property", int(property_id))

    @property
    def property(self) -> int:
        return self.get_property("property", 0)

    @property.setter
    def property(self, val: int) -> None:
        self.set_property("property", int(val))
