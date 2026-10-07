from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CompareZombieTypeNode(Node):
    node_type = "CompareZombieTypeNode"
    _class_ports = {
        "僵尸类型A": PortDef("僵尸类型A", PortDirection.Input, PortType.ZombieType),
        "僵尸类型B": PortDef("僵尸类型B", PortDirection.Input, PortType.ZombieType),
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
            node_type="CompareZombieTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["zombieTypeA_PortName"] = "僵尸类型A"
        data["zombieTypeB_PortName"] = "僵尸类型B"
        data["equal_PortName"] = "相同"
        return data
