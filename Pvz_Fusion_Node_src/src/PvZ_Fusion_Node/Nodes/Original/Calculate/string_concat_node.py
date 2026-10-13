from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class StringConcatNode(Node):
    # Status in Extensions: Implemented
    node_type = "StringConcatNode"
    _class_ports = {
        "A": PortDef("A", PortDirection.Input, PortType.String),
        "B": PortDef("B", PortDirection.Input, PortType.String),
        "结果": PortDef("结果", PortDirection.Output, PortType.String),
    }

    # Port name constants
    A_input_string : str = "A"
    B_input_string : str = "B"
    Result_output_string : str = "结果"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="StringConcatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
