from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntMultiplyNode(Node):
    # Status in Extensions: Implemented
    node_type = "IntMultiplyNode"
    _class_ports = {
        "A": PortDef("A", PortDirection.Input, PortType.Int),
        "B": PortDef("B", PortDirection.Input, PortType.Int),
        "积": PortDef("积", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    A_input_int : str = "A"
    B_input_int : str = "B"
    Product_output_int : str = "积"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="IntMultiplyNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
