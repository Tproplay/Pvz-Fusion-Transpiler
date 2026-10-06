from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RemovePlantTypeNode(Node):
    node_type = "RemovePlantTypeNode"
    _class_ports = {
        "植物类型列表": PortDef("植物类型列表", PortDirection.Input, PortType.PlantTypeList),
        "要删除的类型": PortDef("要删除的类型", PortDirection.Input, PortType.PlantType),
        "结果列表": PortDef("结果列表", PortDirection.Output, PortType.PlantTypeList),
        "是否成功": PortDef("是否成功", PortDirection.Output, PortType.Bool),
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
            node_type="RemovePlantTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["list_PortName"] = "植物类型列表"
        data["plantType_PortName"] = "要删除的类型"
        data["resultList_PortName"] = "结果列表"
        data["success_PortName"] = "是否成功"
        return data
