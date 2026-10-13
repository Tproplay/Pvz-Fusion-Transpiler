from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringToFloatNode(Node):
    # Status in Extensions: Implemented
    node_type = "StringToFloatNode"
    _class_ports = {
        "字符串": PortDef("字符串", PortDirection.Input, PortType.String),
        "浮点数": PortDef("浮点数", PortDirection.Output, PortType.Float),
    }

    # Port name constants
    String_input_string : str = "字符串"
    Float_output_float : str = "浮点数"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="StringToFloatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
