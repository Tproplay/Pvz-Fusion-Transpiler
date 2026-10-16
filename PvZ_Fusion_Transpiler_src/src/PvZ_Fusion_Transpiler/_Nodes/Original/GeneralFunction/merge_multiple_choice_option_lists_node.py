from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MergeMultipleChoiceOptionListsNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "MergeMultipleChoiceOptionListsNode"

    def __init__(self):
        super().__init__()
        self.port_input_choiceoptions_List1 : Port = self.create_port("列表1", PortDirection.Input, PortType.ChoiceOptions)
        self.port_input_choiceoptions_List2 : Port = self.create_port("列表2", PortDirection.Input, PortType.ChoiceOptions)
        self.port_output_choiceoptions_MergedList : Port = self.create_port("合并列表", PortDirection.Output, PortType.ChoiceOptions)


__all__ = ["MergeMultipleChoiceOptionListsNode"]
