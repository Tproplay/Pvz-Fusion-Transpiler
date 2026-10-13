from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType

class FindBoolListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindBoolListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_bool : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="FindBoolListValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
