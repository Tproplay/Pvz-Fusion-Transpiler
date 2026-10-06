from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ForEachPlantTypeNode(Node):
    node_type = "ForEachPlantTypeNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物类型列表": PortDef("植物类型列表", PortDirection.Input, PortType.PlantTypeList),
        "循环体": PortDef("循环体", PortDirection.Output, PortType.Trigger),
        "当前类型": PortDef("当前类型", PortDirection.Output, PortType.PlantType),
        "当前索引": PortDef("当前索引", PortDirection.Output, PortType.Int),
        "循环完成": PortDef("循环完成", PortDirection.Output, PortType.Trigger),
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
            node_type="ForEachPlantTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plantTypeList_PortName"] = "植物类型列表"
        data["loopBody_PortName"] = "循环体"
        data["currentPlantType_PortName"] = "当前类型"
        data["currentIndex_PortName"] = "当前索引"
        data["onCompleted_PortName"] = "循环完成"
        return data
