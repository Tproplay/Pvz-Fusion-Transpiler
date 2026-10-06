from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class TypedChoiceMenuNode(Node):
    node_type = "TypedChoiceMenuNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "选项列表": PortDef("选项列表", PortDirection.Input, PortType.ChoiceOptions),
        "可刷新": PortDef("可刷新", PortDirection.Input, PortType.Bool),
        "刷新次数": PortDef("刷新次数", PortDirection.Input, PortType.Int),
        "可取消": PortDef("可取消", PortDirection.Input, PortType.Bool),
        "窗口数量": PortDef("窗口数量", PortDirection.Input, PortType.Int),
        "退出时触发": PortDef("退出时触发", PortDirection.Output, PortType.Trigger),
        "刷新时触发": PortDef("刷新时触发", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        refreshable: bool = False,
        refresh_count: int = 3,
        cancelable: bool = True,
        window_count: int = 3,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="TypedChoiceMenuNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("refreshable", bool(refreshable))
        self.set_property("refreshCount", int(refresh_count))
        self.set_property("cancelable", bool(cancelable))
        self.set_property("windowCount", int(window_count))

    @property
    def refreshable(self) -> bool:
        return self.get_property("refreshable", False)

    @refreshable.setter
    def refreshable(self, val: bool) -> None:
        self.set_property("refreshable", bool(val))

    @property
    def refresh_count(self) -> int:
        return self.get_property("refreshCount", 3)

    @refresh_count.setter
    def refresh_count(self, val: int) -> None:
        self.set_property("refreshCount", int(val))

    @property
    def cancelable(self) -> bool:
        return self.get_property("cancelable", True)

    @cancelable.setter
    def cancelable(self, val: bool) -> None:
        self.set_property("cancelable", bool(val))

    @property
    def window_count(self) -> int:
        return self.get_property("windowCount", 3)

    @window_count.setter
    def window_count(self, val: int) -> None:
        self.set_property("windowCount", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["options_PortName"] = "选项列表"
        data["refreshable_PortName"] = "可刷新"
        data["refreshCount_PortName"] = "刷新次数"
        data["cancelable_PortName"] = "可取消"
        data["windowCount_PortName"] = "窗口数量"
        data["actionOnExit_PortName"] = "退出时触发"
        data["actionOnRefresh_PortName"] = "刷新时触发"
        return data
