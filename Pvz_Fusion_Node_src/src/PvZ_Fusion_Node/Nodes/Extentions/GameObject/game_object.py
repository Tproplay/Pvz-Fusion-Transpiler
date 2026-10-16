from __future__ import annotations
from typing import Any, Optional, Union
from ..extension_node import ExtensionNode
from ....Core.context import ctx, ExecutionPath
from ...Original.ObjectOperation.create_event_object_node import CreateEventObjectNode
from ...Original.ObjectOperation.destroy_event_object_node import DestroyEventObjectNode
from ...Original.ObjectOperation.bind_object_node import BindObjectNode
from ...Original.ObjectOperation.get_object_transform_node import GetObjectTransformNode
from ...Original.ObjectOperation.set_event_object_transform_node import SetEventObjectTransformNode
from ...Original.ObjectOperation.make_vector3_node import MakeVector3Node
from ...Original.TypeConvert.object_to_plant_node import ObjectToPlantNode
from ...Original.TypeConvert.object_to_zombie_node import ObjectToZombieNode
from ...Original.TypeConvert.object_to_string_node import ObjectToStringNode
from ...Original.TypeConvert.string_to_object_node import StringToObjectNode
from ...Original.Node import to_port


class Vector3(ExtensionNode):
    """3D Vector representation supporting engine Vector3 ports, component coordinates, and math operations."""

    def __init__(
        self,
        x: Any = 0.0,
        y: Any = 0.0,
        z: Any = 0.0,
        port: Any = None,
    ) -> None:
        from ...Original.Node import Port, PortType
        if port is not None:
            self._port = to_port(port)
            self._x = None
            self._y = None
            self._z = None
            super().__init__(root_node=getattr(self._port, "node", None))
        elif hasattr(x, "port_type") and getattr(x, "port_type", None) == PortType.Vector3:
            self._port = x
            self._x = None
            self._y = None
            self._z = None
            super().__init__(root_node=getattr(x, "node", None))
        elif isinstance(x, Vector3):
            self._port = x._port
            self._x = x._x
            self._y = x._y
            self._z = x._z
            super().__init__(root_node=getattr(self._port, "node", None))
        else:
            node = MakeVector3Node()
            to_port(x).connect(node.get_input(MakeVector3Node.X_input_float))
            to_port(y).connect(node.get_input(MakeVector3Node.Y_input_float))
            to_port(z).connect(node.get_input(MakeVector3Node.Z_input_float))
            self._port = node.get_output(MakeVector3Node.Vector_output_vector3)
            self._x = to_port(x)
            self._y = to_port(y)
            self._z = to_port(z)
            super().__init__(root_node=node)

    @property
    def port(self) -> Any:
        """The underlying Vector3 Port in the visual node graph."""
        return self._port

    def get_primary_port(self) -> Any:
        return self._port

    def _get_primary_port(self) -> Any:
        return self._port

    @property
    def x(self) -> Any:
        """X coordinate component port or value."""
        return self._x if self._x is not None else self._port

    @property
    def y(self) -> Any:
        """Y coordinate component port or value."""
        return self._y if self._y is not None else self._port

    @property
    def z(self) -> Any:
        """Z coordinate component port or value."""
        return self._z if self._z is not None else self._port

    # Static Factories
    @classmethod
    def zero(cls) -> Vector3:
        """Shorthand for writing Vector3(0.0, 0.0, 0.0)."""
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def one(cls) -> Vector3:
        """Shorthand for writing Vector3(1.0, 1.0, 1.0)."""
        return cls(1.0, 1.0, 1.0)

    @classmethod
    def up(cls) -> Vector3:
        """Shorthand for writing Vector3(0.0, 1.0, 0.0)."""
        return cls(0.0, 1.0, 0.0)

    @classmethod
    def down(cls) -> Vector3:
        """Shorthand for writing Vector3(0.0, -1.0, 0.0)."""
        return cls(0.0, -1.0, 0.0)

    @classmethod
    def left(cls) -> Vector3:
        """Shorthand for writing Vector3(-1.0, 0.0, 0.0)."""
        return cls(-1.0, 0.0, 0.0)

    @classmethod
    def right(cls) -> Vector3:
        """Shorthand for writing Vector3(1.0, 0.0, 0.0)."""
        return cls(1.0, 0.0, 0.0)

    @classmethod
    def forward(cls) -> Vector3:
        """Shorthand for writing Vector3(0.0, 0.0, 1.0)."""
        return cls(0.0, 0.0, 1.0)

    @classmethod
    def back(cls) -> Vector3:
        """Shorthand for writing Vector3(0.0, 0.0, -1.0)."""
        return cls(0.0, 0.0, -1.0)

    # Formatting Integration
    def to_string(self) -> Any:
        """Formats the vector as string port for display or logging."""
        if self._x is not None and self._y is not None and self._z is not None:
            from ....Libraries.StdLib.formatting import format_string
            return format_string("(", self.x, ", ", self.y, ", ", self.z, ")")
        from ...Original.TypeConvert.object_to_string_node import ObjectToStringNode
        o2s = ObjectToStringNode()
        self.port.connect(o2s.get_input(ObjectToStringNode.GameObject_input_gameobject))
        return o2s.get_output(ObjectToStringNode.String_output_string)

    def __repr__(self) -> str:
        if self._x is not None and self._y is not None and self._z is not None:
            return f"Vector3({self._x}, {self._y}, {self._z})"
        return f"<Vector3 port={self._port}>"

    # Math operators
    def __add__(self, other: Any) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector3(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other: Any) -> Vector3:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector3(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other: Any) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.y, other.z - self.z)
        return Vector3(other - self.x, other - self.y, other - self.z)

    def __mul__(self, other: Any) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: Any) -> Vector3:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __neg__(self) -> Vector3:
        return Vector3(-self.x, -self.y, -self.z)


class GameObject(ExtensionNode):
    """High-level Extension class representing an engine GameObject."""

    def __init__(self, obj_port: Any = None):
        self._obj_port = obj_port
        super().__init__(root_node=getattr(obj_port, "node", None))

    @property
    def port(self) -> Any:
        return self._obj_port

    def _get_primary_port(self) -> Any:
        return self._obj_port

    @classmethod
    def create(
        cls,
        name: Any = "EventObject",
        position: Any = None,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
    ) -> GameObject:
        """Spawns an Event GameObject at the given location."""
        if position is None:
            position = Vector3(x, y, z)

        node = CreateEventObjectNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, CreateEventObjectNode.Trigger_input_trigger)

        to_port(name).connect(node.get_input(CreateEventObjectNode.GameObjectName_input_string))
        to_port(position).connect(node.get_input(CreateEventObjectNode.Position_input_vector3))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, CreateEventObjectNode.Complete_output_trigger)

        return cls(node.get_output(CreateEventObjectNode.GameObject_output_gameobject))

    @classmethod
    def from_string(cls, str_port: Any) -> GameObject:
        """Converts an object name string or reference to a GameObject."""
        node = StringToObjectNode()
        to_port(str_port).connect(node.get_input(StringToObjectNode.String_input_string))
        return cls(node.get_output(StringToObjectNode.GameObject_output_gameobject))

    def destroy(self) -> GameObject:
        """Destroys this GameObject from the game scene."""
        node = DestroyEventObjectNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, DestroyEventObjectNode.Trigger_input_trigger)

        if self._obj_port:
            to_port(self._obj_port).connect(node.get_input(DestroyEventObjectNode.GameObject_input_gameobject))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, DestroyEventObjectNode.Complete_output_trigger)

        return self

    def bind(self, name: str = "守护目标") -> GameObject:
        """Binds this GameObject under a named identifier."""
        node = BindObjectNode(binding_name=name)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, BindObjectNode.Trigger_input_trigger)

        if self._obj_port:
            to_port(self._obj_port).connect(node.get_input(BindObjectNode.GameObject_input_gameobject))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, BindObjectNode.Complete_output_trigger)

        return self

    def get_transform(self) -> dict[str, Any]:
        """Queries the position, rotation, and scale vectors of this GameObject."""
        node = GetObjectTransformNode()
        if self._obj_port:
            to_port(self._obj_port).connect(node.get_input(GetObjectTransformNode.GameObject_input_gameobject))

        return {
            "position": node.get_output(GetObjectTransformNode.Position_output_vector3),
            "rotation": node.get_output(GetObjectTransformNode.Rotation_output_vector3),
            "scale": node.get_output(GetObjectTransformNode.Scale_output_vector3),
        }

    def set_transform(
        self,
        position: Any = None,
        rotation: Any = None,
        scale: Any = None,
    ) -> GameObject:
        """Updates the transform (position, rotation, scale) of this GameObject."""
        node = SetEventObjectTransformNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetEventObjectTransformNode.Trigger_input_trigger)

        if self._obj_port:
            to_port(self._obj_port).connect(node.get_input(SetEventObjectTransformNode.GameObject_input_gameobject))

        if position is not None:
            to_port(position).connect(node.get_input(SetEventObjectTransformNode.Position_input_vector3))
        if rotation is not None:
            to_port(rotation).connect(node.get_input(SetEventObjectTransformNode.Rotation_input_vector3))
        if scale is not None:
            to_port(scale).connect(node.get_input(SetEventObjectTransformNode.Scale_input_vector3))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetEventObjectTransformNode.Complete_output_trigger)

        return self

    def to_plant(self) -> Any:
        """Casts this GameObject port to a Plant entity."""
        from ..Entity.entities import Plant
        node = ObjectToPlantNode()
        to_port(self._obj_port).connect(node.get_input(ObjectToPlantNode.GameObject_input_gameobject))
        return Plant(node.get_output(ObjectToPlantNode.Plant_output_plant))

    def to_zombie(self) -> Any:
        """Casts this GameObject port to a Zombie entity."""
        from ..Entity.entities import Zombie
        node = ObjectToZombieNode()
        to_port(self._obj_port).connect(node.get_input(ObjectToZombieNode.GameObject_input_gameobject))
        return Zombie(node.get_output(ObjectToZombieNode.Zombie_output_zombie))

    def to_string(self) -> Any:
        """Converts this GameObject reference into a String."""
        node = ObjectToStringNode()
        to_port(self._obj_port).connect(node.get_input(ObjectToStringNode.GameObject_input_gameobject))
        return node.get_output(ObjectToStringNode.String_output_string)
