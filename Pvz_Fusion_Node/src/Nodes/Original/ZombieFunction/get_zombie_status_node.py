from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetZombieStatusNode(Node):
    node_type = "GetZombieStatusNode"
    _class_ports = {
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "具有状态": PortDef("具有状态", PortDirection.Output, PortType.Bool),
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
            node_type="GetZombieStatusNode",
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
