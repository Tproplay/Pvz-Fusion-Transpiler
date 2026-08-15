import atexit
from .core import (
    ctx as _ctx, 
    settings,
    PlantData,
    PlantEntry,
    OrderedSpawn
)
from . import nodes as nodes

# API Setup

from .api import (
    Trigger,
    Spawner,
    InGameUI,
    Random,
    Board,
    Lawnf,
    Mouse
)

from .extensions import (
    Plant,
    Zombie,
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    MultiSelectMenu,
    ForEachPlant,
    ForEachPlantType,
    PlantTypeList,
    While,
    For,
    Time
)

from .TypeMgr import (
    PlantType,
    ZombieType,
    SoundType,
    KeyCode,
    ZombieAnimation,
    SceneType,
    LevelType,
    TravelBuffType
)


def Config(output="./", name="Untitled"):
    """Specify the Output folder and Name.
    If the file already exists, its NodeGraph and Connections will be overwritten."""
    _ctx.config["output"] = output
    _ctx.config["name"] = name

def add_graph(*func):
    """Executes a function block to populate the compiler context."""
    for function in func:
        function()

atexit.register(_ctx.export)

class _TriggerNamespace:
    on_wave = nodes.on_wave

class _GeneralNamespace:
    add_sun = nodes.add_sun
    add_money = nodes.add_money
    branch_node = nodes.branch_node

level_config = _ctx.level_config

__all__ = [
    "Config",
    "add_graph",
    "settings",

    # API
    "Trigger",
    "Spawner",
    "InGameUI",
    "Random",
    "Board",
    "Lawnf",
    "Mouse",

    # Extensions
    "Plant",
    "Zombie",
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "MultiSelectMenu",
    "ForEachPlant",
    "ForEachPlantType",
    "PlantTypeList",
    "While",
    "For",
    "Time",

    # Level Data Helpers
    "PlantData",
    "PlantEntry",
    "OrderedSpawn",

    # Types
    "PlantType",
    "ZombieType",
    "SoundType",
    "KeyCode",
    "ZombieAnimation",
    "SceneType",
    "LevelType",
    "TravelBuffType",

    # Modules
    "nodes",
]