from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetObjectTransformNode(Node):
    node_type = "GetObjectTransformNode"
    _class_ports = {
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "位置": PortDef("位置", PortDirection.Output, PortType.Vector3),
        "旋转": PortDef("旋转", PortDirection.Output, PortType.Vector3),
        "缩放": PortDef("缩放", PortDirection.Output, PortType.Vector3),
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
            node_type="GetObjectTransformNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
