from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CreateDoomShroomEffectNode(Node):
    node_type = "CreateDoomShroomEffectNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "伤害值": PortDef("伤害值", PortDirection.Input, PortType.Float),
        "创建弹坑": PortDef("创建弹坑", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
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
            node_type="CreateDoomShroomEffectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["column_PortName"] = "列"
        data["row_PortName"] = "行"
        data["damage_PortName"] = "伤害值"
        data["setPit_PortName"] = "创建弹坑"
        return data
