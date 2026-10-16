import sys
from .Core import (
    Config,
    export,
    _ctx,
    VariableAsset,
    IntVariableAsset,
    FloatVariableAsset,
    BoolVariableAsset,
    StringVariableAsset,
)
from .Core.connection_manager import (
    ConnectionManager,
    Connection,
    Port,
    PortDirection,
    PortType,
)
from . import Core
from . import _Nodes
from . import nodes
from . import Data
from . import StdLib

from ._Nodes.Extentions import (
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    Plant,
    Zombie,
    ForEachPlant,
    ForEachPlantType,
    PlantTypeList,
    While,
    For,
    Time,
    Mouse,
    Random,
    Option,
    MultiSelectMenu,
    InfoCard,
    Trigger,
    Spawner,
    SpawnedPlant,
    SpawnedZombie,
    Game,
    Board,
    Lawnf,
    InGameUI,
    format_string,
)

# Alias _Nodes in sys.modules so `from _Nodes import ...` or `import _Nodes` works as well
if "_Nodes" not in sys.modules:
    sys.modules["_Nodes"] = _Nodes

__all__ = [
    "Config",
    "export",
    "_ctx",
    "Core",
    "_Nodes",
    "nodes",
    "Data",
    "StdLib",
    "ConnectionManager",
    "Connection",
    "Port",
    "PortDirection",
    "PortType",
    "VariableAsset",
    "IntVariableAsset",
    "FloatVariableAsset",
    "BoolVariableAsset",
    "StringVariableAsset",
    # Extensions
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "Plant",
    "Zombie",
    "ForEachPlant",
    "ForEachPlantType",
    "PlantTypeList",
    "While",
    "For",
    "Time",
    "Mouse",
    "Random",
    "Option",
    "MultiSelectMenu",
    "InfoCard",
    "Trigger",
    "Spawner",
    "SpawnedPlant",
    "SpawnedZombie",
    "Game",
    "Board",
    "Lawnf",
    "InGameUI",
    "format_string",
]
