from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatValueNode(Node):
    node_type = "FloatValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.Float),
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
            node_type="FloatValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        v = val if val is not None else (value if value is not None else 3.0)
        self.set_property("value", float(v))

    @property
    def const_value(self) -> float:
        return float(self.get_property("value", 3.0))

    @const_value.setter
    def const_value(self, val: float) -> None:
        self.set_property("value", float(val))

    def dump_data(self):
        data = super().dump_data()
        data["value"] = float(self.get_property("value", 3.0))
        data["value_PortName"] = "值"
        return data
