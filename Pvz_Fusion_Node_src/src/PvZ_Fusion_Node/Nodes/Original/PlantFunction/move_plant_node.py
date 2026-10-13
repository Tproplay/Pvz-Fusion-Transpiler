from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MovePlantNode(Node):
    # Status in Extensions: Implemented
    node_type = "MovePlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "强制": PortDef("强制", PortDirection.Input, PortType.Bool),
        "移动成功": PortDef("移动成功", PortDirection.Output, PortType.Trigger),
        "植物Out": PortDef("植物", PortDirection.Output, PortType.Plant),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Plant_input_plant : str = "植物"
    Col_input_int : str = "列"
    Row_input_int : str = "行"
    Force_input_bool : str = "强制"
    MoveSuccess_output_trigger : str = "移动成功"
    Out_output_plant : str = "植物Out"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="MovePlantNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plant_PortName"] = "植物"
        data["column_PortName"] = "列"
        data["row_PortName"] = "行"
        data["force_PortName"] = "强制"
        data["onMoved_PortName"] = "移动成功"
        data["movedPlant_PortName"] = "植物"
        return data
