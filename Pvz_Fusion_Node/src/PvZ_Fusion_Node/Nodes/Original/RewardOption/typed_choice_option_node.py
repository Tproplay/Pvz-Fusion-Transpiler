from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class TypedChoiceOptionNode(Node):
    node_type = "TypedChoiceOptionNode"
    _class_ports = {
        "选项列表": PortDef("选项列表", PortDirection.Output, PortType.ChoiceOptions),
        "标题": PortDef("标题", PortDirection.Input, PortType.String),
        "描述": PortDef("描述", PortDirection.Input, PortType.String),
        "植物类型": PortDef("植物类型", PortDirection.Input, PortType.PlantType),
        "僵尸类型": PortDef("僵尸类型", PortDirection.Input, PortType.ZombieType),
        "选项被点击": PortDef("选项被点击", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        title: str = "选项",
        description: str = "选项描述",
        plant_type: int = 254,
        zombie_type: int = -1,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="TypedChoiceOptionNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("title", str(title))
        self.set_property("description", str(description))
        self.set_property("plantType", int(plant_type))
        self.set_property("zombieType", int(zombie_type))

    @property
    def title(self) -> str:
        return self.get_property("title", "选项")

    @title.setter
    def title(self, val: str) -> None:
        self.set_property("title", str(val))

    @property
    def description(self) -> str:
        return self.get_property("description", "选项描述")

    @description.setter
    def description(self, val: str) -> None:
        self.set_property("description", str(val))

    @property
    def plant_type(self) -> int:
        return self.get_property("plantType", 254)

    @plant_type.setter
    def plant_type(self, val: int) -> None:
        self.set_property("plantType", int(val))

    @property
    def zombie_type(self) -> int:
        return self.get_property("zombieType", -1)

    @zombie_type.setter
    def zombie_type(self, val: int) -> None:
        self.set_property("zombieType", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["list_PortName"] = "选项列表"
        data["title_PortName"] = "标题"
        data["description_PortName"] = "描述"
        data["plantType_PortName"] = "植物类型"
        data["zombieType_PortName"] = "僵尸类型"
        data["optionSelected_PortName"] = "选项被点击"
        return data
