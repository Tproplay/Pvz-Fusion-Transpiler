from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ComparePlantTypeNode(Node):
    # Status in Extensions: Implemented
    node_type = "ComparePlantTypeNode"
    _class_ports = {
        "植物类型A": PortDef("植物类型A", PortDirection.Input, PortType.PlantType),
        "植物类型B": PortDef("植物类型B", PortDirection.Input, PortType.PlantType),
        "相同": PortDef("相同", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    PlantTypeA_input_planttype : str = "植物类型A"
    PlantTypeB_input_planttype : str = "植物类型B"
    Same_output_bool : str = "相同"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ComparePlantTypeNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["plantTypeA_PortName"] = "植物类型A"
        data["plantTypeB_PortName"] = "植物类型B"
        data["equal_PortName"] = "相同"
        return data
