from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RandomIntNode(Node):
    # Status in Extensions: Implemented
    node_type = "RandomIntNode"
    _class_ports = {
        "最小值": PortDef("最小值", PortDirection.Input, PortType.Int),
        "最大值": PortDef("最大值", PortDirection.Input, PortType.Int),
        "随机整数": PortDef("随机整数", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    Min_input_int : str = "最小值"
    Max_input_int : str = "最大值"
    RandomInt_output_int : str = "随机整数"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="RandomIntNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
