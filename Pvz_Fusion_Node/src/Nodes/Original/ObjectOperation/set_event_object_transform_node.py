from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetEventObjectTransformNode(Node):
    node_type = "SetEventObjectTransformNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "位置": PortDef("位置", PortDirection.Input, PortType.Vector3),
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
            node_type="SetEventObjectTransformNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
