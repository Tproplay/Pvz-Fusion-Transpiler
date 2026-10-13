from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DiePlantNode(Node):
    # Status in Extensions: Implemented
    node_type = "DiePlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "死亡完成": PortDef("死亡完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Plant_input_plant : str = "植物"
    DeathComplete_output_trigger : str = "死亡完成"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="DiePlantNode",
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
        data["onCompleted_PortName"] = "死亡完成"
        return data
