from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetPlantsOnLayerNode(Node):
    node_type = "GetPlantsOnLayerNode"
    _class_ports = {
        "植物列表": PortDef("植物列表", PortDirection.Output, PortType.PlantList),
    }

    def __init__(
        self,
        layer: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="GetPlantsOnLayerNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("layer", int(layer))

    @property
    def layer(self) -> int:
        return self.get_property("layer", 0)

    @layer.setter
    def layer(self, val: int) -> None:
        self.set_property("layer", int(val))
