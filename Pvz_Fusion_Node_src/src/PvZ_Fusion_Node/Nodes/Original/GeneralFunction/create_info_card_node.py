from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CreateInfoCardNode(Node):
    node_type = "CreateInfoCardNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "大标题": PortDef("大标题", PortDirection.Input, PortType.String),
        "小标题": PortDef("小标题", PortDirection.Input, PortType.String),
        "点击卡牌时触发": PortDef("点击卡牌时触发", PortDirection.Output, PortType.Trigger),
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
            node_type="CreateInfoCardNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["bigTitle_PortName"] = "大标题"
        data["smallTitle_PortName"] = "小标题"
        data["onCardClicked_PortName"] = "点击卡牌时触发"
        return data
