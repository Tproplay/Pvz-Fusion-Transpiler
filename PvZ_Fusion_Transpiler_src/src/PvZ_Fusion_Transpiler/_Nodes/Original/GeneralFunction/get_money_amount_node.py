from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetMoneyAmountNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetMoneyAmountNode"

    def __init__(self):
        super().__init__()
        self.port_output_int_MoneyAmount : Port = self.create_port("金币", PortDirection.Output, PortType.Int)


__all__ = ["GetMoneyAmountNode"]
