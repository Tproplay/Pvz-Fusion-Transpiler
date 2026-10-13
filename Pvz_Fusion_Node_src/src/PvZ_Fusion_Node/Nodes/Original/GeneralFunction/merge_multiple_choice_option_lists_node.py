from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class MergeMultipleChoiceOptionListsNode(Node):
    node_type = "MergeMultipleChoiceOptionListsNode"
    _class_ports = {
        "列表1": PortDef("列表1", PortDirection.Input, PortType.ChoiceOptions),
        "列表2": PortDef("列表2", PortDirection.Input, PortType.ChoiceOptions),
        "合并列表": PortDef("合并列表", PortDirection.Output, PortType.ChoiceOptions),
    }

    def __init__(
        self,
        cancel_merge: bool = False,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="MergeMultipleChoiceOptionListsNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("cancelMerge", bool(cancel_merge))

    @property
    def cancel_merge(self) -> bool:
        return self.get_property("cancelMerge", False)

    @cancel_merge.setter
    def cancel_merge(self, val: bool) -> None:
        self.set_property("cancelMerge", bool(val))

    def dump_data(self):
        data = super().dump_data()
        data["list1_PortName"] = "列表1"
        data["list2_PortName"] = "列表2"
        return data
