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
    ListVariableAsset,
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
from . import _Data
from . import _Data as Data
from . import nodes
from . import StdLib
from . import Types

from ._Nodes.Extentions import (
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    Plant,
    Zombie,
    Bullet,
    ForEachPlant,
    ForEachPlantType,
    ForEachZombieType,
    PlantTypeList,
    ZombieTypeList,
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
    SpawnedBullet,
    Game,
    Board,
    Lawnf,
    InGameUI,
    format_string,
)

# Alias _Nodes and _Data in sys.modules so imports work cleanly
if "_Nodes" not in sys.modules:
    sys.modules["_Nodes"] = _Nodes
if "PvZ_Fusion_Transpiler.Data" not in sys.modules:
    sys.modules["PvZ_Fusion_Transpiler.Data"] = _Data

__all__ = [
    "Config",
    "export",
    "_ctx",
    "Core",
    "_Nodes",
    "_Data",
    "Data",
    "nodes",
    "StdLib",
    "Types",
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
    "ListVariableAsset",
    # Extensions
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "Plant",
    "Zombie",
    "Bullet",
    "ForEachPlant",
    "ForEachPlantType",
    "ForEachZombieType",
    "PlantTypeList",
    "ZombieTypeList",
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
    "SpawnedBullet",
    "Game",
    "Board",
    "Lawnf",
    "InGameUI",
    "format_string",
]
