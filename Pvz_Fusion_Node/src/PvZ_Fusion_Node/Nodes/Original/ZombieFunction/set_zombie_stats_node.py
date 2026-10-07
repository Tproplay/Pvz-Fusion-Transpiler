from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetZombieStatsNode(Node):
    node_type = "SetZombieStatsNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "数值": PortDef("数值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        stat: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetZombieStatsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("stat", int(stat))

    @property
    def stat(self) -> int:
        return self.get_property("stat", 0)

    @stat.setter
    def stat(self, val: int) -> None:
        self.set_property("stat", int(val))
