from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CompareGameObjectNode(Node):
    node_type = "CompareGameObjectNode"
    _class_ports = {
        "对象A": PortDef("对象A", PortDirection.Input, PortType.GameObject),
        "对象B": PortDef("对象B", PortDirection.Input, PortType.GameObject),
        "相同": PortDef("相同", PortDirection.Output, PortType.Bool),
    }

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="CompareGameObjectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["gameObjectA_PortName"] = "对象A"
        data["gameObjectB_PortName"] = "对象B"
        data["equal_PortName"] = "相同"
        return data
