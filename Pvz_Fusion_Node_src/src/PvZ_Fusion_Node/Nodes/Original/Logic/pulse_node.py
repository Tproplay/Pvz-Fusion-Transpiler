from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class PulseNode(Node):
    # Status in Extensions: Implemented
    node_type = "PulseNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "状态": PortDef("状态", PortDirection.Input, PortType.Bool),
        "脉冲触发时": PortDef("脉冲触发时", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    State_input_bool : str = "状态"
    OnPulse_output_trigger : str = "脉冲触发时"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="PulseNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["state_PortName"] = "状态"
        data["onPulse_PortName"] = "脉冲触发时"
        return data
