"""
PvZ Fusion Extensions Module.
Re-exports advanced modular extensions built on top of Nodes.Original.
"""

from .extension_node import ExtensionNode
from .branching import If, Switch
from .variables import IntVar, FloatVar, BoolVar, StrVar, ListVar
from .menu import Option, MultiSelectMenu
from .entities import Plant, Zombie, ForEachPlant, ForEachPlantType, PlantTypeList
from .loops import While, For
from .time_ext import Time
from .mouse_ext import Mouse
from .random_ext import Random
from .ui_ext import InfoCard

__all__ = [
    "ExtensionNode",
    "If",
    "Switch",
    "IntVar",
    "FloatVar",
    "BoolVar",
    "StrVar",
    "ListVar",
    "Option",
    "MultiSelectMenu",
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
    "InfoCard",
]
