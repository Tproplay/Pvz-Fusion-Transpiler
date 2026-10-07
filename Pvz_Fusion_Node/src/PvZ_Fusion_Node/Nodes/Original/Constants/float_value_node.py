from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatValueNode(Node):
    node_type = "FloatValueNode"
    _class_ports = {
        "值": PortDef("值", PortDirection.Output, PortType.Float),
    }

    def __init__(
        self,
        value: float = 3.0,
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
        self.set_property("value", float(value))

    @property
    def value(self) -> float:
        return self.get_property("value", 3.0)

    @value.setter
    def value(self, val: float) -> None:
        self.set_property("value", float(val))
