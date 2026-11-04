from __future__ import annotations

from typing import Any, NamedTuple, Optional
from enum import Enum
from .... import nodes
from ..Entity.plant import Plant
from ..Entity.zombie import Zombie


class Vector3(NamedTuple):
    x: Any
    y: Any
    z: Any


class ObjectTransform(NamedTuple):
    position: Any
    scale: Any
    exists: Any


class WorldObject:
    """Wrapper around runtime GameObject entities, transforms, and bindings."""

    def __init__(self, obj_ref: Any) -> None:
        if isinstance(obj_ref, WorldObject):
            self.ref = obj_ref.ref
        else:
            self.ref = obj_ref

    @staticmethod
    def create(name: Any = "EventObject", position: Any = None, icon_plant: Any = None) -> WorldObject:
        node = nodes.create_event_object(name=name, position=position, icon_plant=icon_plant)
        return WorldObject(node.port_output_gameobject_GameObject)

    def destroy(self) -> Any:
        return nodes.destroy_event_object(game_object=self.ref)

    def get_transform(self) -> ObjectTransform:
        node = nodes.get_object_transform(game_object=self.ref)
        return ObjectTransform(
            position=node.port_output_vector3_Position,
            scale=node.port_output_vector3_Scale,
            exists=node.port_output_bool_Exists,
        )

    def set_transform(self, position: Any = None, scale_multiplier: Any = None) -> Any:
        return nodes.set_event_object_transform(game_object=self.ref, position=position, scale=scale_multiplier)

    def to_plant(self) -> Plant:
        """CastTo: casts this GameObject to a Plant."""
        node = nodes.object_to_plant(game_object=self.ref)
        return Plant(node.port_output_plant_Plant)

    cast_to_plant = to_plant

    def try_cast_to_plant(self) -> tuple[Plant, Any]:
        """TryCast: attempts to cast this GameObject to a Plant, returning (Plant, exists_port)."""
        node = nodes.object_to_plant(game_object=self.ref)
        return (Plant(node.port_output_plant_Plant), node.port_output_bool_Exists)

    def to_zombie(self) -> Zombie:
        """CastTo: casts this GameObject to a Zombie."""
        node = nodes.object_to_zombie(game_object=self.ref)
        return Zombie(node.port_output_zombie_Zombie)

    cast_to_zombie = to_zombie

    def try_cast_to_zombie(self) -> tuple[Zombie, Any]:
        """TryCast: attempts to cast this GameObject to a Zombie, returning (Zombie, exists_port)."""
        node = nodes.object_to_zombie(game_object=self.ref)
        return (Zombie(node.port_output_zombie_Zombie), node.port_output_bool_Exists)

    def to_string(self) -> Any:
        return nodes.object_to_string(obj=self.ref).port_output_string_String

    @staticmethod
    def from_string(name: Any) -> WorldObject:
        node = nodes.string_to_object(text=name)
        return WorldObject(node.port_output_gameobject_GameObject)

    @staticmethod
    def vector3(x: Any = 0.0, y: Any = 0.0, z: Any = 0.0) -> Any:
        return nodes.make_vector3(x=x, y=y, z=z).port_output_vector3_Vector

    @staticmethod
    def mouse_world_position() -> Any:
        return nodes.get_mouse_world_position().port_output_vector3_Position

    @staticmethod
    def event_position() -> Any:
        return nodes.get_event_position().port_output_vector3_Position

    @staticmethod
    def bind_plant(plant: Any, name: str = "守护目标") -> Any:
        plant_ref = plant.ref if hasattr(plant, "ref") else plant
        return nodes.bind_plant(plant=plant_ref, binding_name=name)

    @staticmethod
    def get_bound_plant(name: str = "守护目标") -> Plant:
        node = nodes.get_bound_plant(binding_name=name)
        return Plant(node.port_output_plant_Plant)

    @staticmethod
    def bind_zombie(zombie: Any, name: str = "首领") -> Any:
        zombie_ref = zombie.ref if hasattr(zombie, "ref") else zombie
        return nodes.bind_zombie(zombie=zombie_ref, binding_name=name)

    @staticmethod
    def get_bound_zombie(name: str = "首领") -> Zombie:
        node = nodes.get_bound_zombie(binding_name=name)
        return Zombie(node.port_output_zombie_Zombie)

    def bind(self, name: Any = None) -> Any:
        return nodes.bind_object(game_object=self.ref, name=name)


GameObject = WorldObject
Object = WorldObject

__all__ = ["WorldObject", "GameObject", "Object", "Vector3", "ObjectTransform"]
