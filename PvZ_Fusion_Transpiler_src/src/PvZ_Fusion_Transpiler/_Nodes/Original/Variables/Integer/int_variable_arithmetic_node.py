from typing import Any
from ....._Data.EventArithmeticOperation import EventArithmeticOperation
from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class IntVariableArithmeticNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "IntVariableArithmeticNode"

    def __init__(self, operation: Any = EventArithmeticOperation.Add, **kwargs: Any):
        super().__init__(**kwargs)
        op = kwargs.get("operation", operation)
        self.operation: EventArithmeticOperation = validate_enum_field(
            op, EventArithmeticOperation, "operation", default=EventArithmeticOperation.Add
        )
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_intvariable_Variable : Port = self.create_port("变量", PortDirection.Input, PortType.IntVariable)
        self.port_input_int_Operand : Port = self.create_port("操作数", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_intvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.IntVariable)
        self.port_output_int_Result : Port = self.create_port("结果", PortDirection.Output, PortType.Int)


__all__ = ["IntVariableArithmeticNode"]
