from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DivideNode(Node):
    # Status in Extensions: Implemented
    node_type = "DivideNode"
    _class_ports = {
        "被除数": PortDef("被除数", PortDirection.Input, PortType.Float),
        "除数": PortDef("除数", PortDirection.Input, PortType.Float),
        "商": PortDef("商", PortDirection.Output, PortType.Float),
    }

    # Port name constants
    Dividend_input_float : str = "被除数"
    Divisor_input_float : str = "除数"
    Quotient_output_float : str = "商"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="DivideNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
