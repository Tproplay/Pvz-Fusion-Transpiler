from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class TypedChoiceOptionNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "TypedChoiceOptionNode"

    def __init__(self, title: str = "选项", description: str = "选项描述", **kwargs: Any):
        super().__init__(**kwargs)
        self.title: str = title
        self.description: str = description
        self.port_output_choiceoptions_OptionList : Port = self.create_port("选项列表", PortDirection.Output, PortType.ChoiceOptions)
        self.port_input_string_Title : Port = self.create_port("标题", PortDirection.Input, PortType.String)
        self.port_input_string_Description : Port = self.create_port("描述", PortDirection.Input, PortType.String)
        self.port_input_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Input, PortType.PlantType)
        self.port_input_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Input, PortType.ZombieType)
        self.port_output_trigger_OnOptionClicked : Port = self.create_port("选项被点击", PortDirection.Output, PortType.Trigger)


__all__ = ["TypedChoiceOptionNode"]
