from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetSunAmountNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetSunAmountNode"

    def __init__(self):
        super().__init__()
        self.port_output_int_SunAmount : Port = self.create_port("阳光数量", PortDirection.Output, PortType.Int)


__all__ = ["GetSunAmountNode"]
