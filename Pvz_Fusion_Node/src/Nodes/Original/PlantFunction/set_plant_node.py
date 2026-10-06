from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetPlantNode(Node):
    node_type = "SetPlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列": PortDef("列", PortDirection.Input, PortType.Int),
        "行": PortDef("行", PortDirection.Input, PortType.Int),
        "植物编号": PortDef("植物编号", PortDirection.Input, PortType.PlantType),
        "强制种植": PortDef("强制种植", PortDirection.Input, PortType.Bool),
        "创建成功": PortDef("创建成功", PortDirection.Output, PortType.Trigger),
        "创建失败": PortDef("创建失败", PortDirection.Output, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Output, PortType.Plant),
    }

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetPlantNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["column_PortName"] = "列"
        data["row_PortName"] = "行"
        data["plantType_PortName"] = "植物编号"
        data["forcePlant_PortName"] = "强制种植"
        data["onCreated_PortName"] = "创建成功"
        data["onCreateFailed_PortName"] = "创建失败"
        data["plant_PortName"] = "植物"
        return data
