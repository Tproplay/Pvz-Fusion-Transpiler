from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class SetToolCooldownNode(Node):
    # Status in Extensions: Implemented
    node_type = "SetToolCooldownNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "工具类型": PortDef("工具类型", PortDirection.Input, PortType.ToolType),
        "冷却时间": PortDef("冷却时间", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    ToolType_input_tooltype : str = "工具类型"
    Cooldown_input_float : str = "冷却时间"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetToolCooldownNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
