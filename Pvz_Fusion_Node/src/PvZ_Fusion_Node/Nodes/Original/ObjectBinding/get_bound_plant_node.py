from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetBoundPlantNode(Node):
    node_type = "GetBoundPlantNode"
    _class_ports = {
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
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
            node_type="GetBoundPlantNode",
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
