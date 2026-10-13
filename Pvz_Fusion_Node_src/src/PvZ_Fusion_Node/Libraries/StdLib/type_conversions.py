"""
Type conversion utilities and port casting functions.
"""

from __future__ import annotations
from typing import Any

from ...Nodes.Original.TypeConvert.ascii_to_string_node import AsciiToStringNode
from ...Nodes.Original.TypeConvert.string_to_ascii_node import StringToAsciiNode
from ...Nodes.Original.TypeConvert.int_to_float_node import IntToFloatNode
from ...Nodes.Original.TypeConvert.float_to_int_node import FloatToIntNode
from ...Nodes.Original.TypeConvert.int_to_string_node import IntToStringNode
from ...Nodes.Original.TypeConvert.string_to_int_node import StringToIntNode
from ...Nodes.Original.TypeConvert.float_to_string_node import FloatToStringNode
from ...Nodes.Original.TypeConvert.string_to_float_node import StringToFloatNode
from ...Nodes.Original.TypeConvert.int_to_bool_node import IntToBoolNode
from ...Nodes.Original.TypeConvert.float_to_bool_node import FloatToBoolNode
from ...Nodes.Original.TypeConvert.object_to_string_node import ObjectToStringNode
from ...Nodes.Original.TypeConvert.string_to_object_node import StringToObjectNode
from ...Nodes.Original.TypeConvert.object_to_plant_node import ObjectToPlantNode
from ...Nodes.Original.TypeConvert.plant_to_object_node import PlantToObjectNode
from ...Nodes.Original.TypeConvert.object_to_zombie_node import ObjectToZombieNode
from ...Nodes.Original.TypeConvert.zombie_to_object_node import ZombieToObjectNode
from ...Nodes.Original.TypeConvert.plant_type_to_string_node import PlantTypeToStringNode
from ...Nodes.Original.TypeConvert.string_to_plant_type_node import StringToPlantTypeNode
from ...Nodes.Original.TypeConvert.zombie_type_to_string_node import ZombieTypeToStringNode
from ...Nodes.Original.TypeConvert.string_to_zombie_type_node import StringToZombieTypeNode
from ...Nodes.Original.GeneralFunction.compare_tool_type_node import CompareToolTypeNode
from ...Nodes.Original.GeneralFunction.tool_type_value_node import ToolTypeValueNode
from ...Nodes.Original.GeneralFunction.get_event_position_node import GetEventPositionNode
from ...Nodes.Original.Node import to_port


def ascii_to_string(ascii_code: Any) -> Any:
    """Converts an ASCII integer code to its single-character string representation."""
    node = AsciiToStringNode()
    to_port(ascii_code).connect(node.get_input(AsciiToStringNode.ASCII_input_int))
    return node.get_output(AsciiToStringNode.String_output_string)


def string_to_ascii(string_val: Any) -> Any:
    """Converts a character string to its ASCII integer value."""
    node = StringToAsciiNode()
    to_port(string_val).connect(node.get_input(StringToAsciiNode.String_input_string))
    return node.get_output(StringToAsciiNode.ASCII_output_int)


def int_to_float(val: Any) -> Any:
    """Converts an integer to a floating-point number."""
    node = IntToFloatNode()
    to_port(val).connect(node.get_input(IntToFloatNode.Int_input_int))
    return node.get_output(IntToFloatNode.Float_output_float)


def float_to_int(val: Any) -> Any:
    """Converts a floating-point number to an integer."""
    node = FloatToIntNode()
    to_port(val).connect(node.get_input(FloatToIntNode.Float_input_float))
    return node.get_output(FloatToIntNode.Int_output_int)


def int_to_string(val: Any) -> Any:
    """Converts an integer to a string representation."""
    node = IntToStringNode()
    to_port(val).connect(node.get_input(IntToStringNode.Int_input_int))
    return node.get_output(IntToStringNode.String_output_string)


def string_to_int(val: Any) -> Any:
    """Parses a string into an integer."""
    node = StringToIntNode()
    to_port(val).connect(node.get_input(StringToIntNode.String_input_string))
    return node.get_output(StringToIntNode.Int_output_int)


def float_to_string(val: Any, decimals: int = 2) -> Any:
    """Converts a floating-point number to a string formatted to specified decimal places."""
    node = FloatToStringNode()
    to_port(val).connect(node.get_input(FloatToStringNode.Value_input_float))
    to_port(decimals).connect(node.get_input(FloatToStringNode.Decimals_input_int))
    return node.get_output(FloatToStringNode.String_output_string)


def string_to_float(val: Any) -> Any:
    """Parses a string into a floating-point number."""
    node = StringToFloatNode()
    to_port(val).connect(node.get_input(StringToFloatNode.String_input_string))
    return node.get_output(StringToFloatNode.Float_output_float)


def int_to_bool(val: Any) -> Any:
    """Converts an integer to a boolean."""
    node = IntToBoolNode()
    to_port(val).connect(node.get_input(IntToBoolNode.Int_input_int))
    return node.get_output(IntToBoolNode.Bool_output_bool)


def float_to_bool(val: Any) -> Any:
    """Converts a floating-point number to a boolean."""
    node = FloatToBoolNode()
    to_port(val).connect(node.get_input(FloatToBoolNode.Float_input_float))
    return node.get_output(FloatToBoolNode.Bool_output_bool)


def object_to_string(val: Any) -> Any:
    """Converts a GameObject reference to string."""
    node = ObjectToStringNode()
    to_port(val).connect(node.get_input(ObjectToStringNode.GameObject_input_gameobject))
    return node.get_output(ObjectToStringNode.String_output_string)


def string_to_object(val: Any) -> Any:
    """Parses a GameObject reference from string."""
    node = StringToObjectNode()
    to_port(val).connect(node.get_input(StringToObjectNode.String_input_string))
    return node.get_output(StringToObjectNode.GameObject_output_gameobject)


def object_to_plant(val: Any) -> Any:
    """Casts a generic GameObject to a Plant reference."""
    node = ObjectToPlantNode()
    to_port(val).connect(node.get_input(ObjectToPlantNode.GameObject_input_gameobject))
    return node.get_output(ObjectToPlantNode.Plant_output_plant)


def plant_to_object(val: Any) -> Any:
    """Casts a Plant reference to a generic GameObject."""
    node = PlantToObjectNode()
    to_port(val).connect(node.get_input(PlantToObjectNode.Plant_input_plant))
    return node.get_output(PlantToObjectNode.GameObject_output_gameobject)


def object_to_zombie(val: Any) -> Any:
    """Casts a generic GameObject to a Zombie reference."""
    node = ObjectToZombieNode()
    to_port(val).connect(node.get_input(ObjectToZombieNode.GameObject_input_gameobject))
    return node.get_output(ObjectToZombieNode.Zombie_output_zombie)


def zombie_to_object(val: Any) -> Any:
    """Casts a Zombie reference to a generic GameObject."""
    node = ZombieToObjectNode()
    to_port(val).connect(node.get_input(ZombieToObjectNode.Zombie_input_zombie))
    return node.get_output(ZombieToObjectNode.GameObject_output_gameobject)


def plant_type_to_string(val: Any) -> Any:
    """Converts a PlantType value or port to its string name."""
    node = PlantTypeToStringNode()
    to_port(val).connect(node.get_input(PlantTypeToStringNode.PlantType_input_planttype))
    return node.get_output(PlantTypeToStringNode.String_output_string)


def string_to_plant_type(val: Any) -> Any:
    """Parses a string into a PlantType value."""
    node = StringToPlantTypeNode()
    to_port(val).connect(node.get_input(StringToPlantTypeNode.String_input_string))
    return node.get_output(StringToPlantTypeNode.PlantType_output_planttype)


def zombie_type_to_string(val: Any) -> Any:
    """Converts a ZombieType value or port to its string name."""
    node = ZombieTypeToStringNode()
    to_port(val).connect(node.get_input(ZombieTypeToStringNode.ZombieType_input_zombietype))
    return node.get_output(ZombieTypeToStringNode.String_output_string)


def string_to_zombie_type(val: Any) -> Any:
    """Parses a string into a ZombieType value."""
    node = StringToZombieTypeNode()
    to_port(val).connect(node.get_input(StringToZombieTypeNode.String_input_string))
    return node.get_output(StringToZombieTypeNode.ZombieType_output_zombietype)


def compare_tool_type(a: Any, b: Any) -> Any:
    """Compares two ToolType values or ports for equality."""
    def _to_tool(v: Any) -> Any:
        if hasattr(v, "value") and not hasattr(v, "node"):
            v = v.value
        if isinstance(v, int):
            return ToolTypeValueNode(tool_type=v).get_output(ToolTypeValueNode.ToolType_output_tooltype)
        return to_port(v)

    node = CompareToolTypeNode()
    _to_tool(a).connect(node.get_input(CompareToolTypeNode.ToolTypeA_input_tooltype))
    _to_tool(b).connect(node.get_input(CompareToolTypeNode.ToolTypeB_input_tooltype))
    return node.get_output(CompareToolTypeNode.Same_output_bool)


def get_event_position() -> Any:
    """Returns the Vector3 position port of the current trigger event."""
    return GetEventPositionNode().get_output(GetEventPositionNode.Position_output_vector3)


__all__ = [
    "ascii_to_string",
    "string_to_ascii",
    "int_to_float",
    "float_to_int",
    "int_to_string",
    "string_to_int",
    "float_to_string",
    "string_to_float",
    "int_to_bool",
    "float_to_bool",
    "object_to_string",
    "string_to_object",
    "object_to_plant",
    "plant_to_object",
    "object_to_zombie",
    "zombie_to_object",
    "plant_type_to_string",
    "string_to_plant_type",
    "zombie_type_to_string",
    "string_to_zombie_type",
    "compare_tool_type",
    "get_event_position",
]
