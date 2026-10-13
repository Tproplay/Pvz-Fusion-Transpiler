"""
PvZ Fusion / PvzRH Visual Script Transpiler & Level Compiler.
"""

from __future__ import annotations
import atexit
import sys

from .Core import (
    Compiler,
    Level,
    EventNodeGraph,
    Connection,
    NodeGroup,
    SymbolRegistry,
    GraphLayoutEngine,
)
from .Core.context import (
    ctx,
    Config,
    add_graph,
    single_group,
    IsolatedTriggerScope,
    level_config,
    CompilerSetting,
)

# API
from .api import Board, InGameUI, Lawnf, Mouse, Spawner, Trigger, Print

# Extensions & DSL
from .Nodes.Extentions import (
    ExtensionNode,
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    StrVar,
    ListVar,
    Option,
    MultiSelectMenu,
    TypedChoiceOption,
    TypedChoiceMenu,
    ForEachPlant,
    ForEachPlantType,
    PlantTypeList,
    ForEachZombie,
    ForEachAllZombies,
    Plant,
    Zombie,
    While,
    For,
    Time,
    Random,
    InfoCard,
    Bullet,
    GameObject,
    Vector3,
    DoOnce,
    RepeatUntil,
    WaitUntil,
)

# Enums & Types
from .Extras.TypeMgr import (
    SceneType,
    LevelType,
    PlantType,
    Plant_DieReason,
    ZombieType,
    SoundType,
    KeyCode,
    ZombieAnimation,
    TravelBuffType,
)

from .Data.PlantData import PlantData
from .Data.DataFactory import PlantEntry, OrderedSpawn, GodPlant
from .Data.Recipes import Recipes

from .Libraries import Math, StdLib
from .Extras import TypeMgr as Types
from . import nodes

# AST Transpiler & Utilities
from .AST import (
    PvZNodeTransformer,
    transpile_to_ast,
    transpile_source,
    compile_ast,
    compile_level,
)
transpile = transpile_source

settings = ctx.settings

# Auto-export on script exit
atexit.register(ctx.export)

__all__ = [
    "Config",
    "add_graph",
    "single_group",
    "IsolatedTriggerScope",
    "level_config",
    "settings",
    "ctx",
    "Compiler",
    "Level",
    "EventNodeGraph",
    "Connection",
    "NodeGroup",
    "SymbolRegistry",
    "GraphLayoutEngine",
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
    "ExtensionNode",
    "Plant",
    "Zombie",
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "StrVar",
    "ListVar",
    "MultiSelectMenu",
    "Option",
    "TypedChoiceOption",
    "TypedChoiceMenu",
    "ForEachPlant",
    "ForEachPlantType",
    "PlantTypeList",
    "ForEachZombie",
    "ForEachAllZombies",
    "While",
    "For",
    "Time",
    "InfoCard",
    "Bullet",
    "GameObject",
    "Vector3",
    "DoOnce",
    "RepeatUntil",
    "WaitUntil",
    # Types
    "SceneType",
    "LevelType",
    "PlantType",
    "Plant_DieReason",
    "ZombieType",
    "SoundType",
    "KeyCode",
    "ZombieAnimation",
    "TravelBuffType",
    "Types",
    # Libraries
    "Math",
    "StdLib",
    "nodes",
    # Data
    "PlantData",
    "PlantEntry",
    "OrderedSpawn",
    "GodPlant",
    "Recipes",
    # AST Transpiler
    "AST",
    "PvZNodeTransformer",
    "transpile_to_ast",
    "transpile_source",
    "transpile",
    "compile_ast",
    "compile_level",
]
