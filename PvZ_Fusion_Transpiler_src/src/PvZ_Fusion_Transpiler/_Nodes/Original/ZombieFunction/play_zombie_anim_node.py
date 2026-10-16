from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlayZombieAnimNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "PlayZombieAnimNode"

    def __init__(self, animationName: str = "idle", **kwargs: Any):
        super().__init__(**kwargs)
        self.animationName: str = kwargs.get("animation_name", animationName)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)

    @property
    def animation_name(self) -> str:
        return self.animationName

    @animation_name.setter
    def animation_name(self, value: str) -> None:
        self.animationName = value


__all__ = ["PlayZombieAnimNode"]
