from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetZombieStatusNode(Node):
    node_type = "SetZombieStatusNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        status: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetZombieStatusNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("status", int(status))

    @property
    def status(self) -> int:
        return self.get_property("status", 0)

    @status.setter
    def status(self, val: int) -> None:
        self.set_property("status", int(val))
