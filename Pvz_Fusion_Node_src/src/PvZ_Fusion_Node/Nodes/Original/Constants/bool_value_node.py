from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BoolValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "BoolValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    Value_output_bool : str = "值"

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
            node_type="BoolValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        v = val if val is not None else (value if value is not None else False)
        self.set_property("value", bool(v))

    @property
    def const_value(self) -> bool:
        return bool(self.get_property("value", False))

    @const_value.setter
    def const_value(self, val: bool) -> None:
        self.set_property("value", bool(val))

    def dump_data(self):
        data = super().dump_data()
        data["value"] = bool(self.get_property("value", False))
        data["value_PortName"] = "值"
        return data
