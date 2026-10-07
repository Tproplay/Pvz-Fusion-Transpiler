from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnPlantDeathCompleteNode(Node):
    node_type = "OnPlantDeathCompleteNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
        "死亡原因": PortDef("死亡原因", PortDirection.Output, PortType.Int),
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
            node_type="OnPlantDeathCompleteNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plant_PortName"] = "植物"
        data["dieReason_PortName"] = "死亡原因"
        return data
