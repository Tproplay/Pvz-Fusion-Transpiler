from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnPlantMixedNode(Node):
    # Status in Extensions: Implemented
    node_type = "OnPlantMixedNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
    }

    # Port name constants
    Trigger_output_trigger : str = "触发"
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
            node_type="OnPlantMixedNode",
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
        return data
