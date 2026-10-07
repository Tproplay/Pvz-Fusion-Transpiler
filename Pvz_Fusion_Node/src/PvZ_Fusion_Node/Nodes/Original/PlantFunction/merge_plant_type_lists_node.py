from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MergePlantTypeListsNode(Node):
    node_type = "MergePlantTypeListsNode"
    _class_ports = {
        "列表A": PortDef("列表A", PortDirection.Input, PortType.PlantTypeList),
        "列表B": PortDef("列表B", PortDirection.Input, PortType.PlantTypeList),
        "合并列表": PortDef("合并列表", PortDirection.Output, PortType.PlantTypeList),
        "列表长度": PortDef("列表长度", PortDirection.Output, PortType.Int),
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
            node_type="MergePlantTypeListsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["listA_PortName"] = "列表A"
        data["listB_PortName"] = "列表B"
        data["mergedList_PortName"] = "合并列表"
        data["count_PortName"] = "列表长度"
        return data
