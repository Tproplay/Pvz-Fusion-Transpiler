from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ZombieToObjectNode(Node):
    # Status in Extensions: Implemented
    node_type = "ZombieToObjectNode"
    _class_ports = {
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "对象": PortDef("对象", PortDirection.Output, PortType.GameObject),
    }

    # Port name constants
    Zombie_input_zombie : str = "僵尸"
    GameObject_output_gameobject : str = "对象"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ZombieToObjectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
