from __future__ import annotations

from typing import Any, Optional
from enum import Enum
from .... import nodes
from ....typing import to_int_port, to_float_port, to_bool_port, to_string_port


class Int:
    """Int node constructor and static type casting helper."""

    def __new__(cls, val: int = 1, **kwargs: Any) -> Any:
        return nodes.int_value(val=val, **kwargs)

    @staticmethod
    def Cast(val: Any) -> Any:
        """Casts float or string to an Int port."""
        cls_name = val.__class__.__name__
        if isinstance(val, float) or cls_name == "FloatVar" or getattr(val, "type_name", None) == "Float":
            return nodes.float_to_int(float_val=val).port_output_int_Int
        if isinstance(val, str) or cls_name == "StringVar" or getattr(val, "type_name", None) == "String":
            return nodes.string_to_int(text=val).port_output_int_Value
        return to_int_port(val)

    cast = Cast

    @staticmethod
    def from_ascii(text: Any, index: Any = 0) -> Any:
        """Returns the ASCII code of the character at the given index in text."""
        return nodes.string_to_ascii(text=text, index=index).port_output_int_AsciiCode


class Float:
    """Float node constructor and static type casting helper."""

    def __new__(cls, val: float = 3.0, **kwargs: Any) -> Any:
        return nodes.float_value(val=val, **kwargs)

    @staticmethod
    def Cast(val: Any) -> Any:
        """Casts int or string to a Float port."""
        cls_name = val.__class__.__name__
        if isinstance(val, int) or cls_name == "IntVar" or getattr(val, "type_name", None) == "Int":
            return nodes.int_to_float(int_val=val).port_output_float_Float
        if isinstance(val, str) or cls_name == "StringVar" or getattr(val, "type_name", None) == "String":
            return nodes.string_to_float(text=val).port_output_float_Value
        return to_float_port(val)

    cast = Cast


class String:
    """String node constructor and static type casting helper."""

    def __new__(cls, val: str = "", **kwargs: Any) -> Any:
        return nodes.string_value(val=val, **kwargs)

    @staticmethod
    def Cast(val: Any, decimals: Any = None) -> Any:
        """Casts any entity, enum, or numeric port to a String port."""
        cls_name = val.__class__.__name__
        if isinstance(val, float) or cls_name == "FloatVar" or getattr(val, "type_name", None) == "Float":
            dec = decimals if decimals is not None else 2
            return nodes.float_to_string(float_val=val, decimals=dec).port_output_string_String
        if isinstance(val, int) or cls_name == "IntVar" or getattr(val, "type_name", None) == "Int":
            return nodes.int_to_string(value=val).port_output_string_String
        if getattr(val, "type_name", None) == "PlantType":
            return nodes.plant_type_to_string(plant_type=val).port_output_string_String
        if getattr(val, "type_name", None) == "ZombieType":
            return nodes.zombie_type_to_string(zombie_type=val).port_output_string_String
        if getattr(val, "type_name", None) == "GameObject":
            return nodes.object_to_string(obj=val).port_output_string_String
        return to_string_port(val)

    cast = Cast

    @staticmethod
    def from_ascii(code: Any) -> Any:
        """Converts an integer ASCII code to a character string port."""
        return nodes.ascii_to_string(code=code).port_output_string_String

    @staticmethod
    def to_ascii(text: Any, index: Any = 0) -> Any:
        """Returns the ASCII code of character at index in text."""
        return nodes.string_to_ascii(text=text, index=index).port_output_int_AsciiCode

    @staticmethod
    def to_plant_type(text: Any) -> Any:
        """Parses a string name to a PlantType port."""
        return nodes.string_to_plant_type(text=text).port_output_planttype_Value

    @staticmethod
    def to_zombie_type(text: Any) -> Any:
        """Parses a string name to a ZombieType port."""
        return nodes.string_to_zombie_type(text=text).port_output_zombietype_Value

    @staticmethod
    def to_object(text: Any) -> Any:
        """Resolves a string name/path to a GameObject port."""
        return nodes.string_to_object(text=text).port_output_gameobject_GameObject


class Bool:
    """Bool node constructor and static type casting helper."""

    def __new__(cls, val: bool = False, **kwargs: Any) -> Any:
        return nodes.bool_value(val=val, **kwargs)

    @staticmethod
    def Cast(val: Any) -> Any:
        """Casts int or float to a Bool port."""
        cls_name = val.__class__.__name__
        if isinstance(val, int) or cls_name == "IntVar" or getattr(val, "type_name", None) == "Int":
            return nodes.int_to_bool(val=val).port_output_bool_Bool
        if isinstance(val, float) or cls_name == "FloatVar" or getattr(val, "type_name", None) == "Float":
            return nodes.float_to_bool(val=val).port_output_bool_Bool
        return to_bool_port(val)

    cast = Cast


__all__ = ["Int", "Float", "String", "Bool"]
