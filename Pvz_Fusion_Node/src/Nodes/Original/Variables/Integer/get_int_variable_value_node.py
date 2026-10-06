from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


class GetIntVariableValueNode(Node):
    node_type = "GetIntVariableValueNode"
    _class_ports = {
        "变量": PortDef("变量", PortDirection.Input, PortType.IntVariable),
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
            node_type="GetIntVariableValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
