# pyright: reportIncompatibleMethodOverride=none
from __future__ import annotations
from enum import IntEnum
from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Any

if TYPE_CHECKING:
    from .._Nodes.Original.node import Node


class PortDirection(IntEnum):
    Input = 0
    Output = 1
class PortType(IntEnum):
    Trigger = 0
    Int = 1
    IntVariable = 2
    Float = 3
    FloatVariable = 4
    String = 5
    Bool = 6
    BoolVariable = 7
    Vector3 = 8
    PlantType = 9
    ZombieType = 10
    Plant = 11
    Zombie = 12
    GameObject = 13
    PlantList = 14
    ZombieList = 15
    PlantTypeList = 16
    ZombieTypeList = 17
    ChoiceOptions = 18
    StringVariable = 19
    ListVariable = 20
    Bullet = 21
    ToolType = 22
    BulletType = 23
    
    @property
    def is_trigger(self) -> bool:
        return self == PortType.Trigger

class Port:
    def __init__(self, node : Node, name : str, direction : PortDirection, port_type : PortType):
        self.node : Node = node
        self.name : str = name
        self.direction : PortDirection = direction
        self.port_type : PortType = port_type

    def connect(self, other_port : Port):
        if self.direction == other_port.direction:
            raise ValueError("Cannot connect ports with the same direction.")
        if self.port_type != other_port.port_type:
            out_p = self if self.direction == PortDirection.Output else other_port
            in_p = other_port if self.direction == PortDirection.Output else self
            int_enum_pairs = {
                (PortType.ListVariable, PortType.ZombieTypeList),
                (PortType.ZombieTypeList, PortType.ListVariable),
                (PortType.ListVariable, PortType.PlantTypeList),
                (PortType.PlantTypeList, PortType.ListVariable),
            }
            if (out_p.port_type, in_p.port_type) in int_enum_pairs:
                pass
            elif out_p.port_type == PortType.Int and in_p.port_type == PortType.Float:
                from .._Nodes.Original.TypeConvert.int_to_float_node import IntToFloatNode
                conv = IntToFloatNode()
                out_p.connect(conv.port_input_int_Int)
                conv.port_output_float_Float.connect(in_p)
                return
            elif out_p.port_type == PortType.Float and in_p.port_type == PortType.Int:
                from .._Nodes.Original.TypeConvert.float_to_int_node import FloatToIntNode
                conv = FloatToIntNode()
                out_p.connect(conv.port_input_float_Float)
                conv.port_output_int_Int.connect(in_p)
                return
            else:
                raise ValueError(f"Cannot connect ports with different types: {self.port_type.name} and {other_port.port_type.name}.")
        if self.direction == PortDirection.Output:
            ConnectionManager.add_connection(self.node, self, other_port.node, other_port)
        else:
            ConnectionManager.add_connection(other_port.node, other_port, self.node, self)

    def get_connections(self):
        return [conn for conn in ConnectionManager.get_connections() 
                if (conn.source_node is self.node and conn.source_port is self) or 
                   (conn.target_node is self.node and conn.target_port is self)]

    def _is_float_port(self) -> bool:
        return self.port_type in (PortType.Float, PortType.FloatVariable)

    def _ensure_float(self, port: Port) -> Port:
        if port._is_float_port():
            return port
        from .._Nodes.Original.TypeConvert.int_to_float_node import IntToFloatNode
        conv = IntToFloatNode()
        port.connect(conv.get_input("IntValue"))
        return conv.get_output("FloatValue")

    def _ensure_int(self, port: Port) -> Port:
        if not port._is_float_port():
            return port
        from .._Nodes.Original.TypeConvert.float_to_int_node import FloatToIntNode
        conv = FloatToIntNode()
        port.connect(conv.get_input("FloatValue"))
        return conv.get_output("IntValue")

    def __add__(self, other: Any) -> Port:
        from ..typing import to_port
        other_p = to_port(other)
        if self.port_type == PortType.String or other_p.port_type == PortType.String:
            from .._Nodes.Original.Calculate.string_concat_node import StringConcatNode
            node = StringConcatNode()
            self.connect(node.get_input("A"))
            other_p.connect(node.get_input("B"))
            return node.get_output("结果")
        return self._execute_op(other_p, "add")

    def __radd__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other).__add__(self)

    def __sub__(self, other: Any) -> Port:
        from ..typing import to_port
        return self._execute_op(to_port(other), "sub")

    def __rsub__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other)._execute_op(self, "sub")

    def __mul__(self, other: Any) -> Port:
        from ..typing import to_port
        return self._execute_op(to_port(other), "mul")

    def __rmul__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other)._execute_op(self, "mul")

    def __truediv__(self, other: Any) -> Port:
        from ..typing import to_port
        return self._execute_op(to_port(other), "div")

    def __rtruediv__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other)._execute_op(self, "div")

    def __floordiv__(self, other: Any) -> Port:
        from ..typing import to_port
        return self._execute_op(to_port(other), "floordiv")

    def __rfloordiv__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other)._execute_op(self, "floordiv")

    def __mod__(self, other: Any) -> Port:
        from ..typing import to_port
        return self._execute_op(to_port(other), "mod")

    def __rmod__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other)._execute_op(self, "mod")

    def __pow__(self, other: Any) -> Port:
        from ..typing import to_port
        from .._Nodes.Original.Calculate.power_node import PowerNode
        other_port = to_port(other)
        f_a = self._ensure_float(self)
        f_b = self._ensure_float(other_port)
        node = PowerNode()
        f_a.connect(node.get_input("底数"))
        f_b.connect(node.get_input("指数"))
        return node.get_output("结果")

    def __rpow__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other).__pow__(self)

    def __neg__(self) -> Port:
        from ..typing import to_port
        zero = 0.0 if self._is_float_port() else 0
        return to_port(zero) - self

    def _execute_op(self, other_port: Port, op_type: str) -> Port:
        is_float = self._is_float_port() or other_port._is_float_port()
        if op_type == "floordiv":
            i_a = self._ensure_int(self)
            i_b = self._ensure_int(other_port)
            from .._Nodes.Original.Calculate.int_divide_node import IntDivideNode
            n = IntDivideNode()
            i_a.connect(n.get_input("被除数"))
            i_b.connect(n.get_input("除数"))
            return n.get_output("商")

        if is_float and op_type != "mod":
            f_a = self._ensure_float(self)
            f_b = self._ensure_float(other_port)
            if op_type == "add":
                from .._Nodes.Original.Calculate.add_node import AddNode
                node = AddNode()
                f_a.connect(node.get_input("A"))
                f_b.connect(node.get_input("B"))
                return node.get_output("结果")
            elif op_type == "sub":
                from .._Nodes.Original.Calculate.subtract_node import SubtractNode
                node = SubtractNode()
                f_a.connect(node.get_input("被减数"))
                f_b.connect(node.get_input("减数"))
                return node.get_output("差")
            elif op_type == "mul":
                from .._Nodes.Original.Calculate.multiply_node import MultiplyNode
                node = MultiplyNode()
                f_a.connect(node.get_input("A"))
                f_b.connect(node.get_input("B"))
                return node.get_output("积")
            elif op_type == "div":
                from .._Nodes.Original.Calculate.divide_node import DivideNode
                node = DivideNode()
                f_a.connect(node.get_input("被除数"))
                f_b.connect(node.get_input("除数"))
                return node.get_output("商")
        else:
            i_a = self._ensure_int(self)
            i_b = self._ensure_int(other_port)
            if op_type == "add":
                from .._Nodes.Original.Calculate.int_add_node import IntAddNode
                node = IntAddNode()
                i_a.connect(node.get_input("A"))
                i_b.connect(node.get_input("B"))
                return node.get_output("和")
            elif op_type == "sub":
                from .._Nodes.Original.Calculate.int_subtract_node import IntSubtractNode
                node = IntSubtractNode()
                i_a.connect(node.get_input("被减数"))
                i_b.connect(node.get_input("减数"))
                return node.get_output("差")
            elif op_type == "mul":
                from .._Nodes.Original.Calculate.int_multiply_node import IntMultiplyNode
                node = IntMultiplyNode()
                i_a.connect(node.get_input("A"))
                i_b.connect(node.get_input("B"))
                return node.get_output("积")
            elif op_type == "div":
                from .._Nodes.Original.Calculate.int_divide_node import IntDivideNode
                node = IntDivideNode()
                i_a.connect(node.get_input("被除数"))
                i_b.connect(node.get_input("除数"))
                return node.get_output("商")
            elif op_type == "mod":
                from .._Nodes.Original.Calculate.int_modulo_node import IntModuloNode
                node = IntModuloNode()
                i_a.connect(node.get_input("被除数"))
                i_b.connect(node.get_input("除数"))
                return node.get_output("余数")

        raise ValueError(f"Unsupported operation {op_type}")

    def __eq__(self, other: Any) -> Port:
        from enum import Enum
        from ..typing import to_port
        if self.port_type == PortType.PlantType or (isinstance(other, Enum) and other.__class__.__name__ == "PlantType"):
            from .._Nodes.Original.PlantFunction.compare_plant_type_node import ComparePlantTypeNode
            cmp = ComparePlantTypeNode()
            self.connect(cmp.get_input("植物类型A"))
            to_port(other).connect(cmp.get_input("植物类型B"))
            return cmp.get_output("相同")
        if self.port_type == PortType.ZombieType or (isinstance(other, Enum) and other.__class__.__name__ == "ZombieType"):
            from .._Nodes.Original.ZombieFunction.compare_zombie_type_node import CompareZombieTypeNode
            cmp = CompareZombieTypeNode()
            self.connect(cmp.get_input("僵尸类型A"))
            to_port(other).connect(cmp.get_input("僵尸类型B"))
            return cmp.get_output("相同")

        other_port = to_port(other)
        is_float = self._is_float_port() or other_port._is_float_port()
        if is_float:
            from .._Nodes.Original.Comparison.compare_float_node import CompareFloatNode
            cmp = CompareFloatNode()
            self._ensure_float(self).connect(cmp.get_input("值A"))
            self._ensure_float(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("等于")
        else:
            from .._Nodes.Original.Comparison.compare_int_node import CompareIntNode
            cmp = CompareIntNode()
            self._ensure_int(self).connect(cmp.get_input("值A"))
            self._ensure_int(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("等于")

    def __ne__(self, other: Any) -> Port:
        eq_port = self.__eq__(other)
        from .._Nodes.Original.Logic.not_node import NotNode
        not_n = NotNode()
        eq_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def __gt__(self, other: Any) -> Port:
        return self._compare_order(other, "gt")

    def __lt__(self, other: Any) -> Port:
        return self._compare_order(other, "lt")

    def __ge__(self, other: Any) -> Port:
        lt_port = self._compare_order(other, "lt")
        from .._Nodes.Original.Logic.not_node import NotNode
        not_n = NotNode()
        lt_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def __le__(self, other: Any) -> Port:
        gt_port = self._compare_order(other, "gt")
        from .._Nodes.Original.Logic.not_node import NotNode
        not_n = NotNode()
        gt_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def _compare_order(self, other: Any, mode: str) -> Port:
        from ..typing import to_port
        other_port = to_port(other)
        is_float = self._is_float_port() or other_port._is_float_port()
        if is_float:
            from .._Nodes.Original.Comparison.compare_float_node import CompareFloatNode
            cmp = CompareFloatNode()
            self._ensure_float(self).connect(cmp.get_input("值A"))
            self._ensure_float(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("大于" if mode == "gt" else "小于")
        else:
            from .._Nodes.Original.Comparison.compare_int_node import CompareIntNode
            cmp = CompareIntNode()
            self._ensure_int(self).connect(cmp.get_input("值A"))
            self._ensure_int(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("大于" if mode == "gt" else "小于")

    def __and__(self, other: Any) -> Port:
        from ..typing import to_port
        from .._Nodes.Original.Logic.and_node import AndNode
        other_port = to_port(other)
        node = AndNode()
        self.connect(node.get_input("A"))
        other_port.connect(node.get_input("B"))
        return node.get_output("结果")

    def __rand__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other).__and__(self)

    def __or__(self, other: Any) -> Port:
        from ..typing import to_port
        from .._Nodes.Original.Logic.or_node import OrNode
        other_port = to_port(other)
        node = OrNode()
        self.connect(node.get_input("A"))
        other_port.connect(node.get_input("B"))
        return node.get_output("结果")

    def __ror__(self, other: Any) -> Port:
        from ..typing import to_port
        return to_port(other).__or__(self)

    def __invert__(self) -> Port:
        from .._Nodes.Original.Logic.not_node import NotNode
        not_n = NotNode()
        self.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def __rshift__(self, target: Any) -> Any:
        self.connect(target)
        return target

    def __repr__(self) -> str:
        node_name = getattr(self.node, "node_type", self.node.__class__.__name__)
        return f"<Port {node_name}.{self.name} dir={self.direction.name} type={self.port_type.name}>"

@dataclass
class Connection:
    source_node : Node
    source_port : Port
    target_node : Node
    target_port : Port

    def to_dict(self) -> dict[str, str]:
        return {
            "sourceNodeId": getattr(self.source_node, "id", str(self.source_node)),
            "sourcePortName": getattr(self.source_port, "name", str(self.source_port)),
            "targetNodeId": getattr(self.target_node, "id", str(self.target_node)),
            "targetPortName": getattr(self.target_port, "name", str(self.target_port)),
        }

    def __repr__(self) -> str:
        src_name = getattr(self.source_node, "node_type", self.source_node.__class__.__name__)
        tgt_name = getattr(self.target_node, "node_type", self.target_node.__class__.__name__)
        return f"<Connection {src_name}.{self.source_port.name} -> {tgt_name}.{self.target_port.name}>"

class ConnectionManager:
    """Manages connections between nodes and their ports."""
    
    connections : List[Connection] = []
    
    @classmethod
    def add_connection(cls, source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> Connection:
        if getattr(source_port, "direction", None) == PortDirection.Input and getattr(target_port, "direction", None) == PortDirection.Output:
            source_node, source_port, target_node, target_port = target_node, target_port, source_node, source_port

        connection = Connection(source_node, source_port, target_node, target_port)
        for conn in cls.connections:
            if (conn.source_node is source_node and
                conn.source_port is source_port and
                conn.target_node is target_node and
                conn.target_port is target_port):
                return conn
        cls.connections.append(connection)
        return connection

    @classmethod
    def remove_connection(cls, source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> None:
        for conn in list(cls.connections):
            if (conn.source_node is source_node and
                conn.source_port is source_port and
                conn.target_node is target_node and
                conn.target_port is target_port):
                cls.connections.remove(conn)

    @classmethod
    def get_connections(cls) -> List[Connection]:
        return cls.connections

    @classmethod
    def clear(cls) -> None:
        cls.connections.clear()


