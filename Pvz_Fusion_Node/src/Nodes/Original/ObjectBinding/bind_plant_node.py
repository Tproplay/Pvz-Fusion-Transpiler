from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BindPlantNode(Node):
    node_type = "BindPlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        binding_name: str = "守护目标",
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="BindPlantNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("bindingName", str(binding_name))

    @property
    def binding_name(self) -> str:
        return self.get_property("bindingName", "守护目标")

    @binding_name.setter
    def binding_name(self, name: str) -> None:
        self.set_property("bindingName", str(name))
