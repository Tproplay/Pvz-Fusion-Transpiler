from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


class InsertFloatListNode(Node):
    node_type = "InsertFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
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
            node_type="InsertFloatListNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
