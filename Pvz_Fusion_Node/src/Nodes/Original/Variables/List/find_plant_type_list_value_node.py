from typing import Optional
try:
    from ...Node import Node, PortDef, PortDirection, PortType
except (ImportError, ValueError):
    from ....Node import Node, PortDef, PortDirection, PortType


class FindPlantTypeListValueNode(Node):
    node_type = "FindPlantTypeListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
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
            node_type="FindPlantTypeListValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
