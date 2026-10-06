from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ZombieSplitNode(Node):
    node_type = "ZombieSplitNode"
    _class_ports = {
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "列": PortDef("列", PortDirection.Output, PortType.Int),
        "行": PortDef("行", PortDirection.Output, PortType.Int),
        "僵尸类型": PortDef("僵尸类型", PortDirection.Output, PortType.ZombieType),
        "是否被魅惑": PortDef("是否被魅惑", PortDirection.Output, PortType.Bool),
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
            node_type="ZombieSplitNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["zombie_PortName"] = "僵尸"
        data["column_PortName"] = "列"
        data["row_PortName"] = "行"
        data["zombieType_PortName"] = "僵尸类型"
        data["isHypnotized_PortName"] = "是否被魅惑"
        return data
