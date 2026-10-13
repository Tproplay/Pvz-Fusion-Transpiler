from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetPlantAttributeCountdownNode(Node):
    # Status in Extensions: Implemented
    node_type = "SetPlantAttributeCountdownNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "倒计时": PortDef("倒计时", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Plant_input_plant : str = "植物"
    Countdown_input_float : str = "倒计时"
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
            node_type="SetPlantAttributeCountdownNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
