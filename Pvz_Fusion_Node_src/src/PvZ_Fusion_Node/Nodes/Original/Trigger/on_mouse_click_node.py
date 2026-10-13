from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnMouseClickNode(Node):
    # Status in Extensions: Implemented
    node_type = "OnMouseClickNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
        "行": PortDef("行", PortDirection.Output, PortType.Int),
        "列": PortDef("列", PortDirection.Output, PortType.Int),
        "手上的物品": PortDef("手上的物品", PortDirection.Output, PortType.ToolType),
        "是左键": PortDef("是左键", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    Trigger_output_trigger : str = "触发"
    Row_output_int : str = "行"
    Col_output_int : str = "列"
    HeldItem_output_tooltype : str = "手上的物品"
    IsLeftButton_output_bool : str = "是左键"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="OnMouseClickNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["row_PortName"] = "行"
        data["column_PortName"] = "列"
        data["item_PortName"] = "手上的物品"
        data["isLeftButton_PortName"] = "是左键"
        return data
