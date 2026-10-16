from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ShowMultipleChoiceMenuNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ShowMultipleChoiceMenuNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_choiceoptions_OptionList : Port = self.create_port("选项列表", PortDirection.Input, PortType.ChoiceOptions)
        self.port_input_bool_CanRefresh : Port = self.create_port("可刷新", PortDirection.Input, PortType.Bool)
        self.port_input_int_RefreshCount : Port = self.create_port("刷新次数", PortDirection.Input, PortType.Int)
        self.port_input_bool_CanCancel : Port = self.create_port("可取消", PortDirection.Input, PortType.Bool)
        self.port_input_int_WindowCount : Port = self.create_port("窗口数量", PortDirection.Input, PortType.Int)
        self.port_output_trigger_OnExit : Port = self.create_port("退出时触发", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_OnRefresh : Port = self.create_port("刷新时触发", PortDirection.Output, PortType.Trigger)


__all__ = ["ShowMultipleChoiceMenuNode"]
