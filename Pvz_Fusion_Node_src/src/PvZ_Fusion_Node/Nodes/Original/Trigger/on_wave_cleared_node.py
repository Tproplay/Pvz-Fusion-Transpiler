from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnWaveClearedNode(Node):
    # Status in Extensions: Implemented
    node_type = "OnWaveClearedNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "波次": PortDef("波次", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    Trigger_output_trigger : str = "触发"
    Wave_output_int : str = "波次"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="OnWaveClearedNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["wave_PortName"] = "波次"
        return data
