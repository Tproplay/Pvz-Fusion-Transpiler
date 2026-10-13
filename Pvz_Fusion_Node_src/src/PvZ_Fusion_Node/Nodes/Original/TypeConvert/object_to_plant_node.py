from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ObjectToPlantNode(Node):
    # Status in Extensions: Implemented
    node_type = "ObjectToPlantNode"
    _class_ports = {
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
    }

    # Port name constants
    GameObject_input_gameobject : str = "对象"
    Plant_output_plant : str = "植物"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ObjectToPlantNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
