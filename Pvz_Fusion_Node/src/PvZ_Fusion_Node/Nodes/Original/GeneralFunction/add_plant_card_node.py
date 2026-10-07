from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class AddPlantCardNode(Node):
    node_type = "AddPlantCardNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "植物类型": PortDef("植物类型", PortDirection.Input, PortType.PlantType),
        "冷却时间": PortDef("冷却时间", PortDirection.Input, PortType.Float),
        "价格": PortDef("价格", PortDirection.Input, PortType.Int),
        "使用默认数据": PortDef("使用默认数据", PortDirection.Input, PortType.Bool),
        "添加成功": PortDef("添加成功", PortDirection.Output, PortType.Trigger),
        "添加失败": PortDef("添加失败", PortDirection.Output, PortType.Trigger),
        "种植时触发": PortDef("种植时触发", PortDirection.Output, PortType.Trigger),
        "种植的植物": PortDef("种植的植物", PortDirection.Output, PortType.Plant),
    }

    def __init__(
        self,
        plant_type: int = 0,
        cooldown: float = 7.5,
        cost: int = 100,
        use_default_data: bool = True,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="AddPlantCardNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("plantType", int(plant_type))
        self.set_property("cooldown", float(cooldown))
        self.set_property("cost", int(cost))
        self.set_property("useDefaultData", bool(use_default_data))

    @property
    def plant_type(self) -> int:
        return self.get_property("plantType", 0)

    @plant_type.setter
    def plant_type(self, val: int) -> None:
        self.set_property("plantType", int(val))

    @property
    def cooldown(self) -> float:
        return self.get_property("cooldown", 7.5)

    @cooldown.setter
    def cooldown(self, val: float) -> None:
        self.set_property("cooldown", float(val))

    @property
    def cost(self) -> int:
        return self.get_property("cost", 100)

    @cost.setter
    def cost(self, val: int) -> None:
        self.set_property("cost", int(val))

    @property
    def use_default_data(self) -> bool:
        return self.get_property("useDefaultData", True)

    @use_default_data.setter
    def use_default_data(self, val: bool) -> None:
        self.set_property("useDefaultData", bool(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["plantType_PortName"] = "植物类型"
        data["cooldown_PortName"] = "冷却时间"
        data["cost_PortName"] = "价格"
        data["useDefaultData_PortName"] = "使用默认数据"
        data["success_PortName"] = "添加成功"
        data["failed_PortName"] = "添加失败"
        data["onPlant_PortName"] = "种植时触发"
        data["plantedPlant_PortName"] = "种植的植物"
        return data
