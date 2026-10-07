from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ZombieTypeValueNode(Node):
    node_type = "ZombieTypeValueNode"
    _class_ports = {
        "僵尸类型": PortDef("僵尸类型", PortDirection.Output, PortType.ZombieType),
    }

    def __init__(
        self,
        value: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ZombieTypeValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("value", int(value))

    @property
    def value(self) -> int:
        return self.get_property("value", 0)

    @value.setter
    def value(self, val: int) -> None:
        self.set_property("value", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["value_PortName"] = "僵尸类型"
        return data
