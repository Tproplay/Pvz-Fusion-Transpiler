from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnWorldPlantEffectNode(Node):
    node_type = "OnWorldPlantEffectNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
    }

    def __init__(
        self,
        effect: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="OnWorldPlantEffectNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("effect", int(effect))

    @property
    def effect(self) -> int:
        return self.get_property("effect", 0)

    @effect.setter
    def effect(self, val: int) -> None:
        self.set_property("effect", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plant_PortName"] = "植物"
        return data
