from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatToStringNode(Node):
    # Status in Extensions: Implemented
    node_type = "FloatToStringNode"
    _class_ports = {
        "数值": PortDef("数值", PortDirection.Input, PortType.Float),
        "小数位数": PortDef("小数位数", PortDirection.Input, PortType.Int),
        "字符串": PortDef("字符串", PortDirection.Output, PortType.String),
    }

    # Port name constants
    Value_input_float : str = "数值"
    Decimals_input_int : str = "小数位数"
    String_output_string : str = "字符串"

    def __init__(
        self,
        float_val: Optional[Any] = None,
        decimals: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        f_val = float_val if float_val is not None else kwargs.pop("float_val", kwargs.pop("float", kwargs.pop("value", kwargs.pop("val", None))))
        dec = decimals if decimals is not None else kwargs.pop("decimals", kwargs.pop("decimal", None))
        if f_val is not None:
            kwargs["value"] = f_val
        if dec is not None:
            kwargs["decimals"] = dec

        super().__init__(
            node_type="FloatToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["value_PortName"] = "数值"
        data["decimals_PortName"] = "小数位数"
        data["result_PortName"] = "字符串"
        return data
