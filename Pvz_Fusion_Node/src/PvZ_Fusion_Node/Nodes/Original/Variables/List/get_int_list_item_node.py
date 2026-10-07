from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType

class GetIntListItemNode(Node):
    node_type = "GetIntListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Int),
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
            node_type="GetIntListItemNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
