from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PlantTypeValueNode(Node):
    node_type = "PlantTypeValueNode"
    _class_ports = {
        "植物类型": PortDef("植物类型", PortDirection.Output, PortType.PlantType),
    }

    def __init__(
        self,
        value: int = -1,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="PlantTypeValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("value", int(value))

    @property
    def value(self) -> int:
        return self.get_property("value", -1)

    @value.setter
    def value(self, val: int) -> None:
        self.set_property("value", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["value_PortName"] = "植物类型"
        return data
