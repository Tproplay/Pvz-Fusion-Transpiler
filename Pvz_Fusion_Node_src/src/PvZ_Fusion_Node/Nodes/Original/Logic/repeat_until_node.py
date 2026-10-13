from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class RepeatUntilNode(Node):
    # Status in Extensions: Implemented
    node_type = "RepeatUntilNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "条件": PortDef("条件", PortDirection.Input, PortType.Bool),
        "循环体": PortDef("循环体", PortDirection.Output, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Condition_input_bool : str = "条件"
    LoopBody_output_trigger : str = "循环体"
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
            node_type="RepeatUntilNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
