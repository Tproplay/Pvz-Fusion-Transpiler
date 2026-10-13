from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DeleteCardByTypeNode(Node):
    # Status in Extensions: Implemented
    node_type = "DeleteCardByTypeNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物类型": PortDef("植物类型", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    PlantType_input_planttype : str = "植物类型"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        plant_type: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="DeleteCardByTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("plantType", int(plant_type))

    @property
    def plant_type(self) -> int:
        return self.get_property("plantType", 0)

    @plant_type.setter
    def plant_type(self, val: int) -> None:
        self.set_property("plantType", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plantType_PortName"] = "植物类型"
        data["completed_PortName"] = "完成"
        return data
