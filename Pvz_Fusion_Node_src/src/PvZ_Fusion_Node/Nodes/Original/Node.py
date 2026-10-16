"""Low-Level Node Architecture for Pvz Fusion (PvzRH) Visual Node Transpiler.

Provides strictly typed, flyweight-compatible schema definitions and serialization logic.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum
from typing import Any, Mapping, Optional, Union
import uuid


class PortDirection(IntEnum):
    """Port direction matching Unity IL2CPP GameLevel.EventNodes.PortDirection."""
    Input = 0
    Output = 1


class PortType(IntEnum):
    """Port data types matching Unity IL2CPP GameLevel.EventNodes.PortType."""
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

    # =========================================================================
    # TYPE METADATA HELPERS
    # =========================================================================

    @property
    def is_trigger(self) -> bool:
        """True if this port represents an execution flow wire."""
        return self == PortType.Trigger

    @property
    def is_variable(self) -> bool:
        """True if this port references a persistent canvas variable asset."""
        return self in (
            PortType.IntVariable,
            PortType.FloatVariable,
            PortType.BoolVariable,
            PortType.StringVariable,
            PortType.ListVariable,
        )

    @property
    def is_numeric(self) -> bool:
        """True if this port represents a standard numeric primitive."""
        return self in (PortType.Int, PortType.Float)

    @property
    def is_list(self) -> bool:
        """True if this port holds a sequence or collection."""
        return self in (
            PortType.PlantList,
            PortType.ZombieList,
            PortType.PlantTypeList,
            PortType.ZombieTypeList,
            PortType.ChoiceOptions,
        )

    @property
    def is_entity(self) -> bool:
        """True if this port references a runtime GameObject/Entity."""
        return self in (
            PortType.Plant,
            PortType.Zombie,
            PortType.GameObject,
            PortType.Bullet,
        )


@dataclass(frozen=True)
class PortDef:
    """Immutable Flyweight schema descriptor for a port.
    Shared across all node instances of the same type.
    """
    name: str
    direction: PortDirection
    port_type: PortType
    description: str = ""

    @property
    def is_input(self) -> bool:
        return self.direction == PortDirection.Input

    @property
    def is_output(self) -> bool:
        return self.direction == PortDirection.Output

    @property
    def is_trigger(self) -> bool:
        return self.port_type.is_trigger


@dataclass
class Port:
    """A port instance bound to a specific Node on the canvas."""
    node: Node
    definition: PortDef

    @property
    def name(self) -> str:
        return self.definition.name

    @property
    def port_name(self) -> str:
        return self.definition.name

    @property
    def direction(self) -> PortDirection:
        return self.definition.direction

    @property
    def port_type(self) -> PortType:
        return self.definition.port_type

    @property
    def is_input(self) -> bool:
        return self.definition.is_input

    @property
    def is_output(self) -> bool:
        return self.definition.is_output

    @property
    def is_trigger(self) -> bool:
        return self.definition.is_trigger

    def is_compatible_with(self, target: Port) -> bool:
        """Checks structural compatibility between this port and a target pin."""
        if self.direction == target.direction:
            return False  # Cannot wire Input -> Input or Output -> Output

        if self.port_type == target.port_type:
            return True

        # Unity numeric conversion
        if (self.port_type == PortType.Int and target.port_type == PortType.Float) or (
            self.port_type == PortType.Float and target.port_type == PortType.Int
        ):
            return True

        # Unity Object conversions (e.g. Vector3 can be converted via ObjectToStringNode)
        if (self.port_type == PortType.Vector3 and target.port_type == PortType.GameObject) or (
            self.port_type == PortType.GameObject and target.port_type == PortType.Vector3
        ):
            return True

        return False

    def __bool__(self) -> bool:
        return True

    def _is_float_port(self) -> bool:
        if self.port_type == PortType.Float:
            return True
        t = getattr(self.node, "node_type", "")
        float_nodes = {
            "FloatValueNode", "RandomFloatNode", "IntToFloatNode",
            "AddNode", "SubtractNode", "MultiplyNode", "DivideNode",
            "GetFloatVariableValueNode", "FloatVariableNode",
        }
        int_nodes = {
            "IntValueNode", "RandomIntNode", "FloatToIntNode",
            "IntAddNode", "IntSubtractNode", "IntMultiplyNode",
            "IntDivideNode", "IntModuloNode", "CounterNode", "GetSunAmountNode",
            "GetIntVariableValueNode", "IntVariableNode",
        }
        if t in float_nodes:
            return True
        if t in int_nodes:
            return False
        if "Float" in t and "ToInt" not in t and "ToString" not in t:
            return True
        return False

    def _ensure_float(self, val: Any) -> Port:
        if isinstance(val, (int, float)):
            from .Constants.float_value_node import FloatValueNode
            return FloatValueNode(val=float(val)).get_output("值")
        p = to_port(val)
        if p._is_float_port():
            return p
        from .TypeConvert.int_to_float_node import IntToFloatNode
        conv = IntToFloatNode()
        p.connect(conv.get_input("整数"))
        return conv.get_output("浮点数")

    def _ensure_int(self, val: Any) -> Port:
        if isinstance(val, (int, float)):
            from .Constants.int_value_node import IntValueNode
            return IntValueNode(val=int(val)).get_output("值")
        p = to_port(val)
        if not p._is_float_port():
            return p
        from .TypeConvert.float_to_int_node import FloatToIntNode
        conv = FloatToIntNode()
        p.connect(conv.get_input("浮点数"))
        return conv.get_output("整数")

    @staticmethod
    def _float_modulo(val: Any, mod_val: Any) -> Port:
        from .TypeConvert.float_to_int_node import FloatToIntNode
        from .TypeConvert.int_to_float_node import IntToFloatNode

        v_port = to_port(val)
        m_port = to_port(mod_val)
        div = v_port / m_port

        f2i = FloatToIntNode()
        div.connect(f2i.get_input("浮点数"))

        i2f = IntToFloatNode()
        f2i.get_output("整数").connect(i2f.get_input("整数"))

        mult = i2f.get_output("浮点数") * m_port
        return v_port - mult

    def _to_string_port(self) -> Port:
        if self.port_type == PortType.String:
            return self
        t = getattr(self.node, "node_type", "")
        if "String" in t or "Concat" in t:
            return self

        if self._is_float_port():
            from .TypeConvert.float_to_string_node import FloatToStringNode
            from .Constants.int_value_node import IntValueNode
            f2s = FloatToStringNode()
            self.connect(f2s.get_input("数值"))
            IntValueNode(val=2).get_output("值").connect(f2s.get_input("小数位数"))
            return f2s.get_output("字符串")
        elif self.port_type == PortType.PlantType:
            from .TypeConvert.plant_type_to_string_node import PlantTypeToStringNode
            p2s = PlantTypeToStringNode()
            self.connect(p2s.get_input("植物类型"))
            return p2s.get_output("字符串")
        elif self.port_type == PortType.ZombieType:
            from .TypeConvert.zombie_type_to_string_node import ZombieTypeToStringNode
            z2s = ZombieTypeToStringNode()
            self.connect(z2s.get_input("僵尸类型"))
            return z2s.get_output("字符串")
        elif self.port_type == PortType.GameObject:
            from .TypeConvert.object_to_string_node import ObjectToStringNode
            o2s = ObjectToStringNode()
            self.connect(o2s.get_input("对象"))
            return o2s.get_output("字符串")
        elif self.port_type == PortType.Plant:
            from .TypeConvert.plant_to_object_node import PlantToObjectNode
            from .TypeConvert.object_to_string_node import ObjectToStringNode
            p2o = PlantToObjectNode()
            self.connect(p2o.get_input("植物"))
            o2s = ObjectToStringNode()
            p2o.get_output("对象").connect(o2s.get_input("对象"))
            return o2s.get_output("字符串")
        elif self.port_type == PortType.Zombie:
            from .TypeConvert.zombie_to_object_node import ZombieToObjectNode
            from .TypeConvert.object_to_string_node import ObjectToStringNode
            z2o = ZombieToObjectNode()
            self.connect(z2o.get_input("僵尸"))
            o2s = ObjectToStringNode()
            z2o.get_output("对象").connect(o2s.get_input("对象"))
            return o2s.get_output("字符串")
        elif self.port_type == PortType.Vector3:
            from .TypeConvert.object_to_string_node import ObjectToStringNode
            o2s = ObjectToStringNode()
            self.connect(o2s.get_input("对象"))
            return o2s.get_output("字符串")
        else:
            from .TypeConvert.int_to_string_node import IntToStringNode
            i2s = IntToStringNode()
            self.connect(i2s.get_input("整数"))
            return i2s.get_output("字符串")

    # =========================================================================
    # ARITHMETIC OPERATORS
    # =========================================================================

    def __add__(self, other: Any) -> Port:
        if isinstance(other, str) or self.port_type == PortType.String or (isinstance(other, Port) and other.port_type == PortType.String):
            from .Calculate.string_concat_node import StringConcatNode
            s_self = self._to_string_port()
            s_other = other._to_string_port() if isinstance(other, Port) else to_port(str(other))
            cat = StringConcatNode()
            s_self.connect(cat.get_input("A"))
            s_other.connect(cat.get_input("B"))
            return cat.get_output("结果")
        return self._execute_op(other, "add")

    def __radd__(self, other: Any) -> Port:
        if isinstance(other, str):
            from .Calculate.string_concat_node import StringConcatNode
            s_self = self._to_string_port()
            s_other = to_port(str(other))
            cat = StringConcatNode()
            s_other.connect(cat.get_input("A"))
            s_self.connect(cat.get_input("B"))
            return cat.get_output("结果")
        return to_port(other).__add__(self)

    def __sub__(self, other: Any) -> Port:
        return self._execute_op(other, "sub")

    def __rsub__(self, other: Any) -> Port:
        return to_port(other)._execute_op(self, "sub")

    def __mul__(self, other: Any) -> Port:
        return self._execute_op(other, "mul")

    def __rmul__(self, other: Any) -> Port:
        return to_port(other)._execute_op(self, "mul")

    def __truediv__(self, other: Any) -> Port:
        return self._execute_op(other, "div")

    def __rtruediv__(self, other: Any) -> Port:
        return to_port(other)._execute_op(self, "div")

    def __floordiv__(self, other: Any) -> Port:
        return self._execute_op(other, "floordiv")

    def __rfloordiv__(self, other: Any) -> Port:
        return to_port(other)._execute_op(self, "floordiv")

    def __mod__(self, other: Any) -> Port:
        return self._execute_op(other, "mod")

    def __rmod__(self, other: Any) -> Port:
        return to_port(other)._execute_op(self, "mod")

    def __pow__(self, other: Any) -> Port:
        from .Calculate.power_node import PowerNode
        other_port = to_port(other)
        f_a = self._ensure_float(self)
        f_b = self._ensure_float(other_port)
        node = PowerNode()
        f_a.connect(node.get_input("底数"))
        f_b.connect(node.get_input("指数"))
        return node.get_output("结果")

    def __rpow__(self, other: Any) -> Port:
        return to_port(other).__pow__(self)

    def _execute_op(self, other: Any, op_type: str) -> Port:
        other_port = to_port(other)
        is_float = self._is_float_port() or other_port._is_float_port() or isinstance(other, float)
        if op_type == "floordiv":
            i_a = self._ensure_int(self)
            i_b = self._ensure_int(other_port)
            from .Calculate.int_divide_node import IntDivideNode
            n = IntDivideNode()
            i_a.connect(n.get_input("被除数"))
            i_b.connect(n.get_input("除数"))
            return n.get_output("商")

        if is_float and op_type != "mod":
            f_a = self._ensure_float(self)
            f_b = self._ensure_float(other_port)
            if op_type == "add":
                from .Calculate.add_node import AddNode
                node = AddNode()
                f_a.connect(node.get_input("A"))
                f_b.connect(node.get_input("B"))
                return node.get_output("结果")
            elif op_type == "sub":
                from .Calculate.subtract_node import SubtractNode
                node = SubtractNode()
                f_a.connect(node.get_input("被减数"))
                f_b.connect(node.get_input("减数"))
                return node.get_output("差")
            elif op_type == "mul":
                from .Calculate.multiply_node import MultiplyNode
                node = MultiplyNode()
                f_a.connect(node.get_input("A"))
                f_b.connect(node.get_input("B"))
                return node.get_output("积")
            elif op_type == "div":
                from .Calculate.divide_node import DivideNode
                node = DivideNode()
                f_a.connect(node.get_input("被除数"))
                f_b.connect(node.get_input("除数"))
                return node.get_output("商")
        else:
            i_a = self._ensure_int(self)
            i_b = self._ensure_int(other_port)
            if op_type == "add":
                from .Calculate.int_add_node import IntAddNode
                node = IntAddNode()
                i_a.connect(node.get_input("A"))
                i_b.connect(node.get_input("B"))
                return node.get_output("和")
            elif op_type == "sub":
                from .Calculate.int_subtract_node import IntSubtractNode
                node = IntSubtractNode()
                i_a.connect(node.get_input("被减数"))
                i_b.connect(node.get_input("减数"))
                return node.get_output("差")
            elif op_type == "mul":
                from .Calculate.int_multiply_node import IntMultiplyNode
                node = IntMultiplyNode()
                i_a.connect(node.get_input("A"))
                i_b.connect(node.get_input("B"))
                return node.get_output("积")
            elif op_type == "div":
                from .Calculate.int_divide_node import IntDivideNode
                node = IntDivideNode()
                i_a.connect(node.get_input("被除数"))
                i_b.connect(node.get_input("除数"))
                return node.get_output("商")
            elif op_type == "mod":
                from .Calculate.int_modulo_node import IntModuloNode
                node = IntModuloNode()
                i_a.connect(node.get_input("被除数"))
                i_b.connect(node.get_input("除数"))
                return node.get_output("余数")

        raise ValueError(f"Unsupported operation {op_type}")

    # =========================================================================
    # COMPARISON OPERATORS
    # =========================================================================

    def __eq__(self, other: Any) -> Port:
        from enum import Enum
        if self.port_type == PortType.PlantType or (isinstance(other, Enum) and other.__class__.__name__ == "PlantType"):
            from .Comparison.compare_plant_type_node import ComparePlantTypeNode
            cmp = ComparePlantTypeNode()
            self.connect(cmp.get_input("植物类型A"))
            to_port(other).connect(cmp.get_input("植物类型B"))
            return cmp.get_output("相同")
        if self.port_type == PortType.ZombieType or (isinstance(other, Enum) and other.__class__.__name__ == "ZombieType"):
            from .Comparison.compare_zombie_type_node import CompareZombieTypeNode
            cmp = CompareZombieTypeNode()
            self.connect(cmp.get_input("僵尸类型A"))
            to_port(other).connect(cmp.get_input("僵尸类型B"))
            return cmp.get_output("相同")

        other_port = to_port(other)
        is_float = self._is_float_port() or other_port._is_float_port() or isinstance(other, float)
        if is_float:
            from .Comparison.compare_float_node import CompareFloatNode
            cmp = CompareFloatNode()
            self._ensure_float(self).connect(cmp.get_input("值A"))
            self._ensure_float(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("等于")
        else:
            from .Comparison.compare_int_node import CompareIntNode
            cmp = CompareIntNode()
            self._ensure_int(self).connect(cmp.get_input("值A"))
            self._ensure_int(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("等于")

    def __ne__(self, other: Any) -> Port:
        eq_port = self.__eq__(other)
        from .Logic.not_node import NotNode
        not_n = NotNode()
        eq_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def __gt__(self, other: Any) -> Port:
        return self._compare_order(other, "gt")

    def __lt__(self, other: Any) -> Port:
        return self._compare_order(other, "lt")

    def __ge__(self, other: Any) -> Port:
        lt_port = self._compare_order(other, "lt")
        from .Logic.not_node import NotNode
        not_n = NotNode()
        lt_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def __le__(self, other: Any) -> Port:
        gt_port = self._compare_order(other, "gt")
        from .Logic.not_node import NotNode
        not_n = NotNode()
        gt_port.connect(not_n.get_input("输入"))
        return not_n.get_output("输出")

    def _compare_order(self, other: Any, mode: str) -> Port:
        other_port = to_port(other)
        is_float = self._is_float_port() or other_port._is_float_port() or isinstance(other, float)
        if is_float:
            from .Comparison.compare_float_node import CompareFloatNode
            cmp = CompareFloatNode()
            self._ensure_float(self).connect(cmp.get_input("值A"))
            self._ensure_float(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("大于" if mode == "gt" else "小于")
        else:
            from .Comparison.compare_int_node import CompareIntNode
            cmp = CompareIntNode()
            self._ensure_int(self).connect(cmp.get_input("值A"))
            self._ensure_int(other_port).connect(cmp.get_input("值B"))
            return cmp.get_output("大于" if mode == "gt" else "小于")

    # =========================================================================
    # LOGICAL OPERATORS
    # =========================================================================

    def __and__(self, other: Any) -> Port:
        other_port = to_port(other)
        from .Logic.and_node import AndNode
        n = AndNode()
        self.connect(n.get_input("条件A"))
        other_port.connect(n.get_input("条件B"))
        return n.get_output("结果")

    def __or__(self, other: Any) -> Port:
        other_port = to_port(other)
        from .Logic.or_node import OrNode
        n = OrNode()
        self.connect(n.get_input("条件A"))
        other_port.connect(n.get_input("条件B"))
        return n.get_output("结果")

    def __invert__(self) -> Port:
        from .Logic.not_node import NotNode
        n = NotNode()
        self.connect(n.get_input("输入"))
        return n.get_output("输出")

    def connect(self, target: Union[Port, Node, Any]) -> dict[str, str]:
        """Connects this port to a target port or node."""
        target_port: Optional[Port] = None
        if isinstance(target, Port):
            target_port = target
        elif hasattr(target, "get_primary_port"):
            target_port = target.get_primary_port()
        elif hasattr(target, "primary_port"):
            target_port = target.primary_port
        elif hasattr(target, "get_matching_input") and self.is_output:
            target_port = target.get_matching_input(self.port_type)
        elif hasattr(target, "get_matching_output") and self.is_input:
            target_port = target.get_matching_output(self.port_type)

        if target_port is None:
            raise TypeError(f"Cannot connect {self} to {type(target).__name__}")

        if not self.is_compatible_with(target_port):
            raise TypeError(
                f"Incompatible ports: '{self.node.node_type}.{self.name}' ({self.port_type.name}) "
                f"and '{target_port.node.node_type}.{target_port.name}' ({target_port.port_type.name})"
            )

        src = self if self.is_output else target_port
        dst = target_port if self.is_output else self

        # Auto-convert numeric Int <-> Float
        if src.port_type == PortType.Int and dst.port_type == PortType.Float:
            from .TypeConvert.int_to_float_node import IntToFloatNode
            conv = IntToFloatNode()
            src.connect(conv.get_input("整数"))
            return conv.get_output("浮点数").connect(dst)
        elif src.port_type == PortType.Float and dst.port_type == PortType.Int:
            from .TypeConvert.float_to_int_node import FloatToIntNode
            conv = FloatToIntNode()
            src.connect(conv.get_input("浮点数"))
            return conv.get_output("整数").connect(dst)

        # If ConnectionMgr has an active context, register directly into it
        try:
            from ...Core.connection_mgr import ConnectionMgr
            active_mgr = ConnectionMgr.get_active()
            if active_mgr is not None:
                active_mgr.connect(src.node, src.name, dst.node, dst.name)
        except Exception:
            pass

        return {
            "sourceNodeId": src.node.node_id,
            "sourcePortName": src.name,
            "targetNodeId": dst.node.node_id,
            "targetPortName": dst.name,
        }

    def __rshift__(self, target: Union[Port, Node, Any]) -> Any:
        """Enables fluent wiring via the >> operator: out_port >> in_port."""
        self.connect(target)
        return target

    def __repr__(self) -> str:
        dir_name = "IN" if self.is_input else "OUT"
        return f"<Port {self.node.node_type}.{self.name} [{dir_name}:{self.port_type.name}]>"


def to_port(val: Any) -> Port:
    """Coerces primitives, variables, or enums into an active output Port."""
    if isinstance(val, Port):
        return val
    if hasattr(val, "_get_primary_port"):
        p = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
        if p is not None:
            return to_port(p)
    if hasattr(val, "get_primary_port") and callable(val.get_primary_port):
        p = val.get_primary_port()
        if p is not None:
            return to_port(p)
    if hasattr(val, "primary_port") and val.primary_port is not None:
        return to_port(val.primary_port)
    if hasattr(val, "port") and isinstance(val.port, Port):
        return val.port
    if hasattr(val, "value"):
        v = val.value
        if isinstance(v, Port):
            return v
    if hasattr(val, "node") and hasattr(val, "port_name"):
        return val.node.get_port(val.port_name)


    from enum import Enum
    if isinstance(val, Enum):
        if val.__class__.__name__ == "PlantType":
            from .Constants.plant_type_value_node import PlantTypeValueNode
            return PlantTypeValueNode(val=val.value).port
        elif val.__class__.__name__ == "ZombieType":
            from .Constants.zombie_type_value_node import ZombieTypeValueNode
            return ZombieTypeValueNode(val=val.value).port
        val = val.value

    if isinstance(val, (tuple, list)) and len(val) == 2:
        src, port_name = val
        if hasattr(src, "get_port"):
            return src.get_port(port_name)
        from ...Core.context import ctx
        from ...Core.node_mgr import NodeMgr
        n = None
        active_mgr = NodeMgr.get_active()
        if active_mgr:
            n = active_mgr.get_node(str(src))
        if n is None and ctx is not None:
            try:
                n = ctx.level.graph.node_mgr.get_node(str(src))
            except Exception:
                pass
        if n and hasattr(n, "get_port"):
            return n.get_port(port_name)
        return Port(node=Node(node_id=str(src)), definition=PortDef(name=str(port_name), direction=PortDirection.Output, port_type=PortType.Trigger))

    if isinstance(val, bool):
        from .Constants.bool_value_node import BoolValueNode
        return BoolValueNode(val=val).get_output("值")
    elif isinstance(val, int):
        from .Constants.int_value_node import IntValueNode
        return IntValueNode(val=val).get_output("值")
    elif isinstance(val, float):
        from .Constants.float_value_node import FloatValueNode
        return FloatValueNode(val=val).get_output("值")
    elif isinstance(val, str):
        from .Constants.string_value_node import StringValueNode
        return StringValueNode(val=val).get_output("值")
    raise TypeError(f"Cannot convert value of type {type(val)} to a Port")


class Node(ABC):
    """Low-level abstract base class for all visual scripting nodes.
    
    Provides declarative flyweight port schemas, clean property storage,
    and side-effect-free JSON serialization into Unity level formats.
    """

    # Class-level flyweight metadata (shared across all instances)
    node_type: str = ""
    namespace: str = "GameLevel.EventNodes"
    assembly: str = "Assembly-CSharp"
    _class_ports: dict[str, PortDef] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Ensure each subclass maintains its own independent port definition dictionary
        cls._class_ports = dict(cls._class_ports)
        cls._generate_port_constants()

    PORT_MAP: dict[str, str] = {
        "和": "Sum",
        "差": "Diff",
        "积": "Product",
        "商": "Quotient",
        "余数": "Remainder",
        "结果": "Result",
        "被除数": "Dividend",
        "除数": "Divisor",
        "被减数": "Minuend",
        "减数": "Subtrahend",
        "操作数": "Operand",
        "加数A": "AddendA",
        "加数B": "AddendB",
        "因数A": "FactorA",
        "因数B": "FactorB",
        "值": "Value",
        "新值": "NewValue",
        "变量": "Variable",
        "变量Out": "VariableOut",
        "数值": "Value",
        "整数": "Int",
        "浮点数": "Float",
        "布尔": "Bool",
        "字符串": "String",
        "小数位数": "Decimals",
        "触发": "Trigger",
        "触发Out": "TriggerOut",
        "完成": "Complete",
        "循环体": "LoopBody",
        "当前索引": "Index",
        "条件": "Condition",
        "真（触发）": "Then",
        "假（停止）": "Else",
        "周期事件": "OnCycle",
        "切换开始时": "OnEnable",
        "切换关闭时": "OnDisable",
        "阳光数量": "SunAmount",
        "金币数量": "MoneyAmount",
        "文本": "Text",
        "持续时间": "Duration",
        "等待时间": "Duration",
        "消耗成功": "OnSuccess",
        "阳光不足": "OnFailed",
        "金币不足": "OnFailed",
        "植物": "Plant",
        "僵尸": "Zombie",
        "行": "Row",
        "列": "Col",
        "植物编号": "PlantType",
        "僵尸类型": "ZombieType",
        "强制种植": "ForcePlant",
        "创建成功": "OnCreated",
        "创建失败": "OnFailed",
        "等于": "Equal",
        "小于": "Less",
        "大于": "Greater",
        "波次": "Wave",
        "价格": "Price",
        "伤害值": "Damage",
        "伤害完成": "DamageComplete",
        "位置": "Position",
        "使用默认数据": "UseDefaultData",
        "修改成功": "ModifySuccess",
        "倒计时": "Countdown",
        "值A": "ValueA",
        "值B": "ValueB",
        "僵尸列表": "ZombieList",
        "僵尸类型A": "ZombieTypeA",
        "僵尸类型B": "ZombieTypeB",
        "全部僵尸": "AllZombies",
        "全部植物": "AllPlants",
        "具有状态": "HasState",
        "冷却时间": "Cooldown",
        "冻住的植物": "FrozenPlant",
        "冻结时间": "FreezeTime",
        "列表": "List",
        "列表1": "List1",
        "列表2": "List2",
        "列表A": "ListA",
        "列表B": "ListB",
        "列表长度": "ListLength",
        "创建弹坑": "CreateCrater",
        "刷新时触发": "OnRefresh",
        "刷新次数": "RefreshCount",
        "可刷新": "CanRefresh",
        "可取消": "CanCancel",
        "合并列表": "MergedList",
        "向量": "Vector",
        "周期间隔": "CycleInterval",
        "回血成功": "HealSuccess",
        "回血量": "HealAmount",
        "大标题": "BigTitle",
        "失败原因": "FailureReason",
        "子弹": "Bullet",
        "子弹类型": "BulletType",
        "存在": "Exists",
        "对象": "GameObject",
        "对象A": "GameObjectA",
        "对象B": "GameObjectB",
        "对象名称": "GameObjectName",
        "小标题": "SmallTitle",
        "属性倒计时": "PropertyCountdown",
        "工具类型": "ToolType",
        "工具类型A": "ToolTypeA",
        "工具类型B": "ToolTypeB",
        "底数": "Base",
        "强制": "Force",
        "当前僵尸": "CurrentZombie",
        "当前列表": "CurrentList",
        "当前植物": "CurrentPlant",
        "当前类型": "CurrentType",
        "循环完成": "LoopComplete",
        "循环次数": "LoopCount",
        "成功": "Success",
        "手上的物品": "HeldItem",
        "护盾值": "ShieldValue",
        "指数": "Exponent",
        "描述": "Description",
        "攻击力加成x100%": "AttackBonus",
        "攻击间隔": "AttackInterval",
        "攻速": "AttackSpeed",
        "旋转": "Rotation",
        "是否成功": "IsSuccess",
        "是否被魅惑": "IsHypnotized",
        "是否重置": "IsReset",
        "是否魅惑": "IsHypnotized",
        "是左键": "IsLeftButton",
        "最大值": "Max",
        "最小值": "Min",
        "条件A": "ConditionA",
        "条件B": "ConditionB",
        "标题": "Title",
        "植物列表": "PlantList",
        "植物类型": "PlantType",
        "植物类型A": "PlantTypeA",
        "植物类型B": "PlantTypeB",
        "植物类型列表": "PlantTypeList",
        "植物血量": "PlantHealth",
        "死亡原因": "DeathReason",
        "死亡完成": "DeathComplete",
        "添加失败": "AddFailed",
        "添加成功": "AddSuccess",
        "源列表": "SourceList",
        "点击卡牌时触发": "OnCardClicked",
        "状态": "State",
        "状态改变时": "OnStateChanged",
        "目标列": "TargetCol",
        "目标列表": "TargetList",
        "目标行": "TargetRow",
        "相同": "Same",
        "真数": "Number",
        "种植时触发": "OnPlant",
        "种植的植物": "PlantedPlant",
        "移动成功": "MoveSuccess",
        "窗口数量": "WindowCount",
        "索引": "Index",
        "组件": "Component",
        "结果列表": "ResultList",
        "缩放": "Scale",
        "脉冲触发时": "OnPulse",
        "血量倍率": "HealthMultiplier",
        "血量加成x100%": "HealthBonus",
        "要删除的类型": "TypeToRemove",
        "触发数量": "TriggerCount",
        "计数": "Count",
        "计数完成": "CountComplete",
        "输入": "Input",
        "输出": "Output",
        "退出时触发": "OnExit",
        "选项列表": "OptionList",
        "选项被点击": "OnOptionClicked",
        "重复触发": "RepeatTrigger",
        "重置": "Reset",
        "金钱数量": "MoneyAmount",
        "长度": "Length",
        "阶段名": "StageName",
        "随机整数": "RandomInt",
        "随机植物类型": "RandomPlantType",
        "随机浮点数": "RandomFloat",
        "音效ID": "SoundId",
    }

    @classmethod
    def _generate_port_constants(cls) -> None:
        """Generates English port name constants on the node class (e.g., Sum_out_port = '和')."""
        import re
        for pname, pdef in cls._class_ports.items():
            dir_str = "in" if pdef.is_input else "out"
            eng = cls.PORT_MAP.get(pname, pname)
            candidates = [eng, eng.lower(), eng.capitalize()]
            if re.match(r'^[a-zA-Z0-9_]+$', eng):
                snake = re.sub(r'(?<!^)(?=[A-Z])', '_', eng).lower()
                candidates.extend([snake, snake.upper()])
            for base in candidates:
                if re.match(r'^[a-zA-Z0-9_]+$', base):
                    setattr(cls, f"{base}_{dir_str}_port", pname)
                    setattr(cls, f"{base}_port", pname)

    def __init__(
        self,
        node_type: Optional[str] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        namespace: Optional[str] = None,
        assembly: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self.node_type = node_type or self.node_type or self.__class__.__name__
        self.node_name: str = self.node_type
        self.node_id: str = node_id or str(uuid.uuid4())
        self.rid: Optional[int] = rid

        self.position_x: float = float(position_x)
        self.position_y: float = float(position_y)

        if namespace:
            self.namespace = namespace
        if assembly:
            self.assembly = assembly

        # Dynamic instance-level port overrides (if needed by generative/custom nodes)
        self._instance_ports: dict[str, PortDef] = {}
        
        # Static properties (e.g. stageName, stat, operation, threshold)
        self._properties: dict[str, Any] = {}
        self._input_defaults: list[Any] = []

        # Bound port cache to avoid repeated object allocations
        self._bound_ports_cache: dict[str, Port] = {}
        self._port_name_map_cache: Optional[dict[str, str]] = None

        # Allow subclasses to register or customize their ports
        self._define_ports()

        # Context-aware auto-registration & execution wiring
        self._register_in_context()
        self._wire_init_kwargs(kwargs)

    @property
    def id(self) -> str:
        return self.node_id

    @property
    def type(self) -> str:
        return self.node_type

    def _define_ports(self) -> None:
        """Hook for subclasses to register ports dynamically or initialize defaults."""
        pass

    def _register_in_context(self) -> None:
        """Auto-registers in the active NodeMgr / Level and chains sequential execution flow."""
        try:
            from ...Core.context import ctx, ExecutionPath
            from ...Core.node_mgr import NodeMgr

            if ctx is not None:
                ctx.level.add_node(self)
            else:
                active_mgr = NodeMgr.get_active()
                if active_mgr is not None:
                    active_mgr.register_node(self)

            ctx.record_node_group(self)

            # Check if flow execution connection should be made
            is_event_root = (
                self.node_type.startswith("On")
                or "Event" in self.node_type
                or "Click" in self.node_type
                or "Press" in self.node_type
            )
            has_trigger_input = "触发" in self.all_port_defs and self.all_port_defs["触发"].is_input

            if has_trigger_input and ctx.trigger_stack and not is_event_root:
                prev = ctx.trigger_stack[-1]
                prev_id = getattr(prev, "id", getattr(prev, "node_id", str(prev)))
                prev_port = getattr(prev, "out_trigger", getattr(prev, "name", "触发"))
                if hasattr(prev, "get_default_out_trigger"):
                    prev_port = prev.get_default_out_trigger() or prev_port

                ctx.add_connection(prev_id, prev_port, self.node_id, "触发")

                if not isinstance(prev, ExecutionPath):
                    ctx.trigger_stack[-1] = self
        except Exception:
            pass

    def _wire_init_kwargs(self, kwargs: dict[str, Any]) -> None:
        """Wires kwargs provided to constructor to corresponding input ports."""
        for k, val in kwargs.items():
            if val is None:
                continue
            port_name = self.resolve_port_name(k)
            if port_name in self.all_port_defs and self.all_port_defs[port_name].is_input:
                target_port = self.get_input(port_name)
                if target_port.port_type.is_variable and hasattr(val, "variable"):
                    source_port = to_port(val.variable)
                else:
                    source_port = to_port(val)
                source_port.connect(target_port)


    def resolve_port_name(self, name: str) -> str:
        """Resolves friendly English/camelCase aliases or Chinese names to the actual Port name."""
        if self._port_name_map_cache is None:
            self._port_name_map_cache = self._build_port_name_map()
        return self._port_name_map_cache.get(name, self._port_name_map_cache.get(name.lower(), name))

    def _build_port_name_map(self) -> dict[str, str]:
        import re
        mapping = {}
        for p in self.all_port_defs:
            mapping[p] = p
            mapping[p.lower()] = p
            if p in self.PORT_MAP:
                eng = self.PORT_MAP[p]
                candidates = [eng, eng.lower(), eng.upper(), eng.capitalize()]
                if re.match(r'^[a-zA-Z0-9_]+$', eng):
                    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', eng).lower()
                    candidates.extend([snake, snake.upper()])
                for base in candidates:
                    mapping[base] = p
                    mapping[f"{base}_port"] = p
                    mapping[f"{base}_in_port"] = p
                    mapping[f"{base}_out_port"] = p

        # Inspect dump_data mappings
        try:
            data = self.dump_data()
            for k, v in data.items():
                if k.endswith("_PortName") and isinstance(v, str):
                    eng = k[:-9]
                    mapping[eng] = v
                    mapping[eng.lower()] = v
                    mapping[eng[0].upper() + eng[1:]] = v
        except Exception:
            pass

        val_port = "值"
        if "新值" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "新值"
        elif "操作数" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "操作数"
        elif "数值" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "数值"
        elif "整数" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "整数"
        elif "浮点数" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "浮点数"
        elif "阳光数量" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "阳光数量"
        elif "金币数量" in self.all_port_defs and "值" not in self.all_port_defs:
            val_port = "金币数量"

        amount_port = "阳光数量" if "阳光数量" in self.all_port_defs else ("金币数量" if "金币数量" in self.all_port_defs else None)

        aliases = {
            "trigger": "触发",
            "in_trigger": "触发",
            "condition": "条件",
            "then": "真（触发）",
            "else": "假（停止）",
            "loop_body": "循环体",
            "loopbody": "循环体",
            "completed": "完成",
            "index": "当前索引",
            "wave": "波次",
            "value": val_port,
            "val": val_port,
            "new_value": "新值",
            "newvalue": "新值",
            "operand": "操作数",
            "operation_number": "操作数",
            "variable": "变量",
            "var": "变量",
            "int_val": "整数",
            "intval": "整数",
            "int_value": "整数",
            "intvalue": "整数",
            "integer": "整数",
            "int": "整数",
            "float_val": "数值" if "数值" in self.all_port_defs else "浮点数",
            "floatval": "数值" if "数值" in self.all_port_defs else "浮点数",
            "float_value": "数值" if "数值" in self.all_port_defs else "浮点数",
            "floatvalue": "数值" if "数值" in self.all_port_defs else "浮点数",
            "float": "数值" if "数值" in self.all_port_defs else "浮点数",
            "decimals": "小数位数",
            "decimal": "小数位数",
            "places": "小数位数",
            "decimal_places": "小数位数",
            "string": "字符串",
            "str": "字符串",
            "str_val": "字符串",
            "bool": "布尔",
            "boolean": "布尔",
            "bool_val": "布尔",
            "a": "被除数" if "被除数" in self.all_port_defs else ("被减数" if "被减数" in self.all_port_defs else "A"),
            "b": "除数" if "除数" in self.all_port_defs else ("减数" if "减数" in self.all_port_defs else "B"),
            "plant": "植物",
            "zombie": "僵尸",
            "row": "行",
            "col": "列",
            "column": "列",
            "plant_type": "植物编号",
            "planttype": "植物编号",
            "zombie_type": "僵尸类型",
            "zombietype": "僵尸类型",
            "force": "强制",
            "force_plant": "强制种植",
            "forceplant": "强制种植",
            "on_created": "创建成功",
            "oncreated": "创建成功",
            "on_failed": "创建失败",
            "onfailed": "创建失败",
            "on_create_failed": "创建失败",
            "oncreatefailed": "创建失败",
            "display_text": "文本",
            "text": "文本",
            "duration": "持续时间",
            "sun_amount": "阳光数量",
            "sunamount": "阳光数量",
            "sun": "阳光数量",
            "money_amount": "金币数量",
            "moneyamount": "金币数量",
            "money": "金币数量",
            "coin": "金币数量",
            "coins": "金币数量",
            "equal": "等于",
            "less": "小于",
            "greater": "大于",
            "result": "结果",
        }
        if amount_port:
            aliases["amount"] = amount_port
        for a_k, a_v in aliases.items():
            if a_v in self.all_port_defs and a_k not in mapping:
                mapping[a_k] = a_v
                mapping[a_k.lower()] = a_v
        return mapping

    @property
    def Output(self) -> Any:
        """Exposes execution paths on this node for block scoping."""
        from ...Core.context import PathAccessor
        return PathAccessor(self)

    def path(self, trigger_name: str) -> Any:
        """Returns an ExecutionPath targeting the specified output trigger port."""
        from ...Core.context import ExecutionPath
        pname = self.resolve_port_name(trigger_name)
        return ExecutionPath(self.node_id, pname)

    @property
    def port(self) -> Port:
        """Returns the primary data or trigger output port of this node."""
        for candidate in ["值", "结果", "和", "差", "积", "商", "余数", "文本", "植物", "僵尸", "当前索引", "完成", "创建成功", "触发"]:
            if candidate in self.all_port_defs and self.all_port_defs[candidate].is_output:
                return self.get_port(candidate)
        outputs = [p for p in self.all_port_defs.values() if p.is_output]
        if outputs:
            return self.get_port(outputs[0].name)
        raise AttributeError(f"Node '{self.node_type}' has no output ports.")

    def get_default_out_trigger(self) -> Optional[str]:
        for candidate in ["完成", "创建成功", "触发", "周期事件"]:
            if candidate in self.all_port_defs and self.all_port_defs[candidate].is_output:
                return candidate
        for name, pdef in self.all_port_defs.items():
            if pdef.is_output and pdef.is_trigger:
                return name
        return None

    def __getattr__(self, name: str) -> Any:
        if name in ("result", "value"):
            for cand in ["结果", "值", "和", "差", "积", "商", "余数", "随机整数", "随机浮点数", "浮点数", "整数", "布尔", "字符串", "数值", "当前索引", "波次"]:
                if cand in self.all_port_defs and self.all_port_defs[cand].is_output:
                    return self.get_port(cand)
            data_outputs = [p for p in self.all_port_defs.values() if p.is_output and not p.is_trigger]
            if len(data_outputs) == 1:
                return self.get_port(data_outputs[0].name)

        if name.endswith(("_port", "_in_port", "_out_port")):
            clean = name
            for sfx in ["_in_port", "_out_port", "_port"]:
                if clean.lower().endswith(sfx):
                    clean = clean[:-len(sfx)]
                    break
            resolved = self.resolve_port_name(clean)
            if resolved in self.all_port_defs:
                return resolved

        pname = self.resolve_port_name(name)
        if pname in self.all_port_defs:
            return self.get_port(pname)
        if name in ("result", "value"):
            for cand in ["结果", "值", "和", "差", "积", "商", "余数", "随机整数", "随机浮点数", "浮点数", "整数", "布尔", "字符串", "数值", "当前索引", "波次"]:
                if cand in self.all_port_defs and self.all_port_defs[cand].is_output:
                    return self.get_port(cand)
            data_outputs = [p for p in self.all_port_defs.values() if p.is_output and not p.is_trigger]
            if len(data_outputs) == 1:
                return self.get_port(data_outputs[0].name)
        raise AttributeError(f"Node '{self.node_type}' has no port or attribute '{name}'")

    # =========================================================================
    # PORT DECLARATION & ACCESS
    # =========================================================================

    @classmethod
    def register_port(
        cls,
        name: str,
        direction: PortDirection,
        port_type: PortType,
        description: str = "",
    ) -> PortDef:
        """Declares a flyweight port definition at the class level."""
        port_def = PortDef(name=name, direction=direction, port_type=port_type, description=description)
        cls._class_ports[name] = port_def
        return port_def

    def add_dynamic_port(
        self,
        name: str,
        direction: PortDirection,
        port_type: PortType,
        description: str = "",
    ) -> Port:
        """Adds an instance-specific port (used by variadic/dynamic nodes)."""
        port_def = PortDef(name=name, direction=direction, port_type=port_type, description=description)
        self._instance_ports[name] = port_def
        port = Port(node=self, definition=port_def)
        self._bound_ports_cache[name] = port
        return port

    def add_input(self, name: str, port_type: PortType, description: str = "") -> Port:
        return self.add_dynamic_port(name, PortDirection.Input, port_type, description)

    def add_output(self, name: str, port_type: PortType, description: str = "") -> Port:
        return self.add_dynamic_port(name, PortDirection.Output, port_type, description)

    @property
    def all_port_defs(self) -> dict[str, PortDef]:
        """Combines shared class-level port definitions with dynamic instance ports."""
        combined = dict(self._class_ports)
        combined.update(self._instance_ports)
        return combined

    def get_port(self, name: str) -> Port:
        """Retrieves a bound Port object on this node instance."""
        if name in self._bound_ports_cache:
            return self._bound_ports_cache[name]

        all_defs = self.all_port_defs
        if name not in all_defs:
            clean = name
            for sfx in ["_in_port", "_out_port", "_port"]:
                if clean.lower().endswith(sfx):
                    clean = clean[:-len(sfx)]
                    break
            resolved = self.resolve_port_name(clean)
            if resolved in all_defs:
                name = resolved
            else:
                resolved_raw = self.resolve_port_name(name)
                if resolved_raw in all_defs:
                    name = resolved_raw
                else:
                    raise KeyError(
                        f"Node '{self.node_type}' ({self.node_id[:8]}) has no port named '{name}'. "
                        f"Available ports: {list(all_defs.keys())}"
                    )

        port = Port(node=self, definition=all_defs[name])
        self._bound_ports_cache[name] = port
        return port

    def get_input(self, name: str) -> Port:
        port = self.get_port(name)
        if not port.is_input:
            raise ValueError(f"Port '{name}' on node '{self.node_type}' is an Output port, not an Input port.")
        return port

    def get_output(self, name: str) -> Port:
        port = self.get_port(name)
        if not port.is_output:
            raise ValueError(f"Port '{name}' on node '{self.node_type}' is an Input port, not an Output port.")
        return port

    @property
    def inputs(self) -> dict[str, Port]:
        return {name: self.get_port(name) for name, p in self.all_port_defs.items() if p.is_input}

    @property
    def outputs(self) -> dict[str, Port]:
        return {name: self.get_port(name) for name, p in self.all_port_defs.items() if p.is_output}

    # =========================================================================
    # STATIC PROPERTY STORAGE
    # =========================================================================

    def set_property(self, key: str, value: Any) -> None:
        """Assigns an internal configuration property (e.g. stageName, stat)."""
        self._properties[key] = value

    def get_property(self, key: str, default: Any = None) -> Any:
        return self._properties.get(key, default)

    # =========================================================================
    # STRICT JSON SERIALIZATION
    # =========================================================================

    def _sanitize_for_json(self, value: Any) -> Any:
        """Recursively cleans values so that json.dump never encounters non-primitive objects."""
        if hasattr(value, "value"):  # Enums or PortReference/wrapper unpackers
            return self._sanitize_for_json(value.value)
        if isinstance(value, dict):
            return {str(k): self._sanitize_for_json(v) for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [self._sanitize_for_json(v) for v in value]
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        return str(value)

    def dump_data(self) -> dict[str, Any]:
        """Dumps the 'data' block adhering to Unity event node graph specifications."""
        data: dict[str, Any] = {
            "inputDefaults": [self._sanitize_for_json(x) for x in self._input_defaults],
            "nodeId": self.node_id,
            "nodeType": self.node_type,
            "position": {
                "x": self.position_x,
                "y": self.position_y,
            },
            "nodeName": self.node_name,
        }

        # 1. Properties
        for prop_key, prop_val in self._properties.items():
            data[prop_key] = self._sanitize_for_json(prop_val)

        # 2. Port Name Mappings (*_PortName)
        PORT_TO_ENG = {
            "值": "value",
            "新值": "newValue",
            "操作数": "operand",
            "变量": "variable",
            "触发": "trigger",
            "完成": "onComplete",
            "循环体": "loopBody",
            "真（触发）": "then",
            "假（停止）": "else",
            "条件": "condition",
            "结果": "result",
            "和": "result",
            "差": "result",
            "积": "result",
            "商": "result",
            "余数": "remainder",
            "被除数": "dividend",
            "除数": "divisor",
            "被减数": "minuend",
            "减数": "subtrahend",
            "加数A": "a",
            "加数B": "b",
            "因数A": "a",
            "因数B": "b",
            "A": "a",
            "B": "b",
            "值A": "a",
            "值B": "b",
            "文本": "text",
            "字符串": "result",
            "整数": "int",
            "浮点数": "float",
            "数值": "value",
            "小数位数": "decimals",
            "持续时间": "duration",
            "植物": "plant",
            "僵尸": "zombie",
            "行": "row",
            "列": "column",
            "植物编号": "plantType",
            "僵尸类型": "zombieType",
            "植物类型": "value",
            "强制种植": "forcePlant",
            "创建成功": "onCreated",
            "创建失败": "onCreateFailed",
            "等于": "equal",
            "小于": "less",
            "大于": "greater",
            "当前索引": "index",
            "波次": "wave",
            "周期间隔": "interval",
            "周期事件": "onCycle",
        }

        for port_name in self.all_port_defs:
            data[f"{port_name}_PortName"] = port_name
            if port_name in PORT_TO_ENG:
                eng = PORT_TO_ENG[port_name]
                data[f"{eng}_PortName"] = port_name
                if eng == "a":
                    data["A_PortName"] = port_name
                elif eng == "b":
                    data["B_PortName"] = port_name

        return data

    def dump_ref(self) -> dict[str, Any]:
        """Serializes the full entry for the 'references.RefIds' collection."""
        if self.rid is None:
            raise ValueError(f"Node '{self.node_type}' ({self.node_id}) cannot be serialized without an assigned 'rid'.")

        return {
            "rid": self.rid,
            "type": {
                "class": self.node_type,
                "ns": self.namespace,
                "asm": self.assembly,
            },
            "data": self.dump_data(),
        }

    def dump_graph_node(self) -> dict[str, int]:
        """Serializes the compact reference for 'eventNodeGraph.nodes'."""
        if self.rid is None:
            raise ValueError(f"Node '{self.node_type}' ({self.node_id}) cannot be serialized without an assigned 'rid'.")
        return {"rid": self.rid}

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.node_id[:8]} rid={self.rid} type={self.node_type}>"

