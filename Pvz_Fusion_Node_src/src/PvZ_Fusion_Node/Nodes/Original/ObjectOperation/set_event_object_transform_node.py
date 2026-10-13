from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetEventObjectTransformNode(Node):
    # Status in Extensions: Implemented
    node_type = "SetEventObjectTransformNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "对象": PortDef("对象", PortDirection.Input, PortType.GameObject),
        "位置": PortDef("位置", PortDirection.Input, PortType.Vector3),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    GameObject_input_gameobject : str = "对象"
    Position_input_vector3 : str = "位置"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetEventObjectTransformNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
