from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringValueNode(Node):
    node_type = "StringValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.String),
    }

    def __init__(
        self,
        value: str = "默认文本",
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="StringValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("value", str(value))

    @property
    def value(self) -> str:
        return self.get_property("value", "默认文本")

    @value.setter
    def value(self, val: str) -> None:
        self.set_property("value", str(val))
