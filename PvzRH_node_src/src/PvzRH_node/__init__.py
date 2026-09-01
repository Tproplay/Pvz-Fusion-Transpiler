import atexit  # noqa: N999

from . import nodes as nodes

# API Setup
from .api import Board, InGameUI, Lawnf, Mouse, Spawner, Trigger, Print
from .core import (
    IsolatedTriggerScope,
    settings,
)
from .core import ctx as _ctx
from .Data.PlantData import PlantData
from .Data.TypeMgr import (
    PlantType,
    ZombieType,
)
from .Data.DataFactory import(
    PlantEntry,
    OrderedSpawn,
    GodPlant
)

from .typing import(
    single_group,
)


from .Libraries.extensions import (
    BoolVar,
    FloatVar,
    For,
    ForEachPlant,
    ForEachPlantType,
    If,
    IntVar,
    MultiSelectMenu,
    Option,
    Plant,
    PlantTypeList,
    Random,
    Switch,
    Time,
    While,
    Zombie,
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

__all__ = [  # noqa: RUF022
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
    "Print",

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
    "Option",
    "IsolatedTriggerScope",

    # Level Data Helpers
    "PlantData",
    "PlantEntry",
    "OrderedSpawn",
    "GodPlant",

    # Types
    "PlantType",
    "ZombieType",
    
    # typing
    "single_group",

]