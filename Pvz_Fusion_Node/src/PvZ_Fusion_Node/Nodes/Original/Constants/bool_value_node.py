from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BoolValueNode(Node):
    node_type = "BoolValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.Bool),
    }

    def __init__(
        self,
        value: bool = False,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="BoolValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("value", bool(value))

    @property
    def value(self) -> bool:
        return self.get_property("value", False)

    @value.setter
    def value(self, val: bool) -> None:
        self.set_property("value", bool(val))
