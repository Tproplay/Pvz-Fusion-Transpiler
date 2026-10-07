from typing import Any, List, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MultiPlantTypeListNode(Node):
    node_type = "MultiPlantTypeListNode"
    _class_ports = {
        "植物类型列表": PortDef("植物类型列表", PortDirection.Output, PortType.PlantTypeList),
    }

    def __init__(
        self,
        plant_types: Optional[List[int]] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="MultiPlantTypeListNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("plantTypes", list(plant_types or []))

    @property
    def plant_types(self) -> List[int]:
        return self.get_property("plantTypes", [])

    @plant_types.setter
    def plant_types(self, val: List[int]) -> None:
        self.set_property("plantTypes", list(val))

    def dump_data(self):
        data = super().dump_data()
        data["plantTypeList_PortName"] = "植物类型列表"
        return data
