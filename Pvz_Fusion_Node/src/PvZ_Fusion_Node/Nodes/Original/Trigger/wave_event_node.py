from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class WaveEventNode(Node):
    node_type = "WaveEventNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "波次": PortDef("波次", PortDirection.Output, PortType.Int),
    }

    def __init__(
        self,
        wave_value: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="WaveEventNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("waveValue", int(wave_value))

    @property
    def wave_value(self) -> int:
        return self.get_property("waveValue", 0)

    @wave_value.setter
    def wave_value(self, val: int) -> None:
        self.set_property("waveValue", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["wave_PortName"] = "波次"
        return data
