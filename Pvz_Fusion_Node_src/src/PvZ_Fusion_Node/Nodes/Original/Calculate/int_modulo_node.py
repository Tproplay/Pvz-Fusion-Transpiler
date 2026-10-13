from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntModuloNode(Node):
    # Status in Extensions: Implemented
    node_type = "IntModuloNode"
    _class_ports = {
        "被除数": PortDef("被除数", PortDirection.Input, PortType.Int),
        "除数": PortDef("除数", PortDirection.Input, PortType.Int),
        "余数": PortDef("余数", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    Dividend_input_int : str = "被除数"
    Divisor_input_int : str = "除数"
    Remainder_output_int : str = "余数"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="IntModuloNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
