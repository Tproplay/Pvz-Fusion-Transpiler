from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringToZombieTypeNode(Node):
    # Status in Extensions: Implemented
    node_type = "StringToZombieTypeNode"
    _class_ports = {
        "字符串": PortDef("字符串", PortDirection.Input, PortType.String),
        "僵尸类型": PortDef("僵尸类型", PortDirection.Output, PortType.ZombieType),
    }

    # Port name constants
    String_input_string : str = "字符串"
    ZombieType_output_zombietype : str = "僵尸类型"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="StringToZombieTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
