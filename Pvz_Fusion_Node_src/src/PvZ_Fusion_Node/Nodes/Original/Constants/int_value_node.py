from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "IntValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    Value_output_int : str = "值"

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
            node_type="IntValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        v = val if val is not None else (value if value is not None else 1)
        self.set_property("value", int(v))

    @property
    def const_value(self) -> int:
        return int(self.get_property("value", 1))

    @const_value.setter
    def const_value(self, val: int) -> None:
        self.set_property("value", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["value"] = int(self.get_property("value", 1))
        data["value_PortName"] = "值"
        return data
