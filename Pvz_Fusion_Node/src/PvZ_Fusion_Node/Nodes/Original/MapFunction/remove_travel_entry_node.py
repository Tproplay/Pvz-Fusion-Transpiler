from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RemoveTravelEntryNode(Node):
    node_type = "RemoveTravelEntryNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        kind: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="RemoveTravelEntryNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("kind", int(kind))

    @property
    def kind(self) -> int:
        return self.get_property("kind", 0)

    @kind.setter
    def kind(self, val: int) -> None:
        self.set_property("kind", int(val))
