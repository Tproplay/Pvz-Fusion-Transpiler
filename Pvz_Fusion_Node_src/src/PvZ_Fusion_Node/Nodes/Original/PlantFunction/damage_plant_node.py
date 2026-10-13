from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class DamagePlantNode(Node):
    # Status in Extensions: Implemented
    node_type = "DamagePlantNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物": PortDef("植物", PortDirection.Input, PortType.Plant),
        "伤害值": PortDef("伤害值", PortDirection.Input, PortType.Float),
        "伤害完成": PortDef("伤害完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Plant_input_plant : str = "植物"
    Damage_input_float : str = "伤害值"
    DamageComplete_output_trigger : str = "伤害完成"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="DamagePlantNode",
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
        data["damage_PortName"] = "伤害值"
        data["onCompleted_PortName"] = "伤害完成"
        return data
