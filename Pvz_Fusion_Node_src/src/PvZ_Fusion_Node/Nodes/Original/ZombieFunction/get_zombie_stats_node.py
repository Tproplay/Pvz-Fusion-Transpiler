from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetZombieStatsNode(Node):
    node_type = "GetZombieStatsNode"
    _class_ports = {
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "数值": PortDef("数值", PortDirection.Output, PortType.Float),
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
            node_type="GetZombieStatsNode",
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
