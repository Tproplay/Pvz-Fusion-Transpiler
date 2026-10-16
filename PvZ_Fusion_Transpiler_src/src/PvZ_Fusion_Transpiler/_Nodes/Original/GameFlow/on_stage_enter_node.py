from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnStageEnterNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "OnStageEnterNode"

    def __init__(self, stageName: str = "战斗", **kwargs: Any):
        super().__init__(**kwargs)
        self.stageName: str = kwargs.get("stage_name", stageName)
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)

    @property
    def stage_name(self) -> str:
        return self.stageName

    @stage_name.setter
    def stage_name(self, value: str) -> None:
        self.stageName = value


__all__ = ["OnStageEnterNode"]
