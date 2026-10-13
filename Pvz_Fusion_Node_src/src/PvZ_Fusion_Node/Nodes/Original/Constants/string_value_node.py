from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringValueNode(Node):
    node_type = "StringValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.String),
    }

    def __init__(
        self,
        value: Optional[Any] = None,
        val: Optional[Any] = None,
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
        v = val if val is not None else (value if value is not None else "默认文本")
        self.set_property("value", str(v))

    @property
    def const_value(self) -> str:
        return str(self.get_property("value", "默认文本"))

    @const_value.setter
    def const_value(self, val: str) -> None:
        self.set_property("value", str(val))

    def dump_data(self):
        data = super().dump_data()
        data["value"] = str(self.get_property("value", "默认文本"))
        data["value_PortName"] = "值"
        return data
