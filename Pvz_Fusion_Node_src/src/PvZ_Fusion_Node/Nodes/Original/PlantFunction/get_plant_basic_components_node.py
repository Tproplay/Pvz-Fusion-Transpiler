from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetPlantBasicComponentsNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetPlantBasicComponentsNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "组件": PortDef("组件", PortDirection.Output, PortType.GameObject),
    }

    # Port name constants
    Plant_input_plant : str = "植物"
    Component_output_gameobject : str = "组件"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="GetPlantBasicComponentsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
