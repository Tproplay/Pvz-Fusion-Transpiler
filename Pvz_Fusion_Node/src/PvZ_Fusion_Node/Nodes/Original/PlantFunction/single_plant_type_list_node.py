from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SinglePlantTypeListNode(Node):
    node_type = "SinglePlantTypeListNode"
    _class_ports = {
        "植物类型列表": PortDef("植物类型列表", PortDirection.Output, PortType.PlantTypeList),
    }

    def __init__(
        self,
        plant_type: int = -1,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SinglePlantTypeListNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("plantType", int(plant_type))

    @property
    def plant_type(self) -> int:
        return self.get_property("plantType", -1)

    @plant_type.setter
    def plant_type(self, val: int) -> None:
        self.set_property("plantType", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["plantTypeList_PortName"] = "植物类型列表"
        return data
