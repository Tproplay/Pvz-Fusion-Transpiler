from typing import Optional, Union
from ..Node import Node, PortDef, PortDirection, PortType
from ..Variables.List.list_storage_operation import ListStorageOperation

class PlantTypeListStorageNode(Node):
    # Status in Extensions: Implemented
    node_type = "PlantTypeListStorageNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.PlantTypeList),
        "植物类型": PortDef("植物类型", PortDirection.Input, PortType.PlantType),
        "当前列表": PortDef("当前列表", PortDirection.Output, PortType.PlantTypeList),
        "列表长度": PortDef("列表长度", PortDirection.Output, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_planttypelist : str = "列表"
    PlantType_input_planttype : str = "植物类型"
    CurrentList_output_planttypelist : str = "当前列表"
    ListLength_output_int : str = "列表长度"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        operation: Union[ListStorageOperation, int] = ListStorageOperation.Set,
        initialize_empty: bool = True,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="PlantTypeListStorageNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("operation", int(operation))
        self.set_property("initializeEmpty", bool(initialize_empty))

    @property
    def operation(self) -> ListStorageOperation:
        return ListStorageOperation(self.get_property("operation", 0))

    @operation.setter
    def operation(self, op: Union[ListStorageOperation, int]) -> None:
        self.set_property("operation", int(op))

    @property
    def initialize_empty(self) -> bool:
        return self.get_property("initializeEmpty", True)

    @initialize_empty.setter
    def initialize_empty(self, val: bool) -> None:
        self.set_property("initializeEmpty", bool(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["list_PortName"] = "列表"
        data["plantType_PortName"] = "植物类型"
        data["currentList_PortName"] = "当前列表"
        data["count_PortName"] = "列表长度"
        data["onComplete_PortName"] = "完成"
        return data
