from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ChangeStageNode(Node):
    node_type = "ChangeStageNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        stage_name: str = "战斗",
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ChangeStageNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("stageName", str(stage_name))

    @property
    def stage_name(self) -> str:
        return self.get_property("stageName", "战斗")

    @stage_name.setter
    def stage_name(self, name: str) -> None:
        self.set_property("stageName", str(name))
