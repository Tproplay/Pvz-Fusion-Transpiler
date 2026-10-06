from typing import Optional
try:
    from ...Node import Node, PortDef, PortDirection, PortType
except (ImportError, ValueError):
    from ....Node import Node, PortDef, PortDirection, PortType


class GetListLengthNode(Node):
    node_type = "GetListLengthNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "长度": PortDef("长度", PortDirection.Output, PortType.Int),
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
            node_type="GetListLengthNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
