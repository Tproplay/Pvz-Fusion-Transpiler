"""
PvZ Fusion Standard Library.
Provides formatting, collections, controllers, stat management, and type conversion helpers.
"""

from .formatting import format_string

from .collections import (
    ZombieTypeList,
    Dictionary,
    Array,
    Counter,
)

from .controllers import (
    _wasd_key,
    WASDPlant,
)

from .stat_manager import (
    NumericVal,
    StatManager,
    PlantStatsManager,
    StatPreset,
)

from .type_conversions import (
    ascii_to_string,
    string_to_ascii,
    int_to_float,
    float_to_int,
    int_to_string,
    string_to_int,
    float_to_string,
    string_to_float,
    int_to_bool,
    float_to_bool,
    object_to_string,
    string_to_object,
    object_to_plant,
    plant_to_object,
    object_to_zombie,
    zombie_to_object,
    plant_type_to_string,
    string_to_plant_type,
    zombie_type_to_string,
    string_to_zombie_type,
    compare_tool_type,
    get_event_position,
)

__all__ = [
    # Formatting
    "format_string",
    # Collections
    "ZombieTypeList",
    "Dictionary",
    "Array",
    "Counter",
    # Controllers
    "_wasd_key",
    "WASDPlant",
    # Stat Manager
    "NumericVal",
    "StatManager",
    "PlantStatsManager",
    "StatPreset",
    # Type Conversions
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
