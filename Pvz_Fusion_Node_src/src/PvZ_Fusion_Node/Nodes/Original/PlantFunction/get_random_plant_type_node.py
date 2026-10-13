from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetRandomPlantTypeNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetRandomPlantTypeNode"
    _class_ports = {
        "植物类型列表": PortDef("植物类型列表", PortDirection.Input, PortType.PlantTypeList),
        "随机植物类型": PortDef("随机植物类型", PortDirection.Output, PortType.PlantType),
    }

    # Port name constants
    PlantTypeList_input_planttypelist : str = "植物类型列表"
    RandomPlantType_output_planttype : str = "随机植物类型"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="GetRandomPlantTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["list_PortName"] = "植物类型列表"
        data["result_PortName"] = "随机植物类型"
        return data
