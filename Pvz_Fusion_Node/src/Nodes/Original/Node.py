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

        # Unity GameObject polymorphic wiring rules
        if target.port_type == PortType.GameObject and self.port_type in (
            PortType.Plant,
            PortType.Zombie,
            PortType.Bullet,
        ):
            return True

        return False

    def __repr__(self) -> str:
        dir_name = "IN" if self.is_input else "OUT"
        return f"<Port {self.node.node_type}.{self.name} [{dir_name}:{self.port_type.name}]>"


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

    def __init__(
        self,
        node_type: Optional[str] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        namespace: Optional[str] = None,
        assembly: Optional[str] = None,
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

        # Allow subclasses to register or customize their ports
        self._define_ports()

    def _define_ports(self) -> None:
        """Hook for subclasses to register ports dynamically or initialize defaults."""
        pass

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
        for port_name in self.all_port_defs:
            data[f"{port_name}_PortName"] = port_name

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

