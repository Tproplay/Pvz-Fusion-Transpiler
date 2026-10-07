"""
Master Level Document model for PvZ Fusion Visual Node Transpiler.
Handles level properties, board configurations, node wiring, and JSON export.
"""

from __future__ import annotations
import json
import os
import sys
from typing import Any, Dict, List, Optional

try:
    from .graph import EventNodeGraph
    from .registry import SymbolRegistry
except (ImportError, ValueError):
    from graph import EventNodeGraph
    from registry import SymbolRegistry

try:
    from ..Extras.Level_Config import BoardConfig, BoardTag, RhythmLevelData
    from ..Extras.Gods_Config import GodShootingConfig
except (ImportError, ValueError):
    try:
        from Extras.Level_Config import BoardConfig, BoardTag, RhythmLevelData
        from Extras.Gods_Config import GodShootingConfig
    except (ImportError, ValueError):
        from ..Extras.Level_Config import BoardConfig, BoardTag, RhythmLevelData
        from ..Extras.Gods_Config import GodShootingConfig


class Level:
    """Represents a complete PvZ Fusion level file with visual scripting graphs."""

    def __init__(
        self,
        name: str = "CustomLevel",
        level_number: int = 9998,
        level_type: int = 11,
        scene_type: int = 0,
        start_sun: int = 500,
        max_wave: int = 10,
        card_count: int = 14,
        victory_type: int = 0,
    ):
        # Metadata
        self.name: str = name
        self.levelNumber: int = level_number
        self.levelType: int = level_type
        self.sceneType: int = scene_type
        self.startSun: int = start_sun
        self.maxWave: int = max_wave
        self.cardCount: int = card_count
        self.victoryType: int = victory_type

        # Core Subsystems
        self.registry: SymbolRegistry = SymbolRegistry()
        self.graph: EventNodeGraph = EventNodeGraph()

        # Config Subsystems
        self.boardConfig: BoardConfig = BoardConfig()
        self.boardTag: BoardTag = BoardTag()
        self.rhythmLevelData: RhythmLevelData = RhythmLevelData()
        self.godShootingConfig: GodShootingConfig = GodShootingConfig()

        # Catalogs
        self.scaryPots: List[Any] = []
        self.plantDatas: List[Any] = []
        self.plants: List[Any] = []
        self.preSelectCards: List[int] = []
        self.preSelectCards_zombie: List[int] = []
        self.advBuffs: List[Any] = []
        self.ultiBuffs: List[Any] = []
        self.ultiBuffs2: List[Any] = []
        self.travelDebuffs: List[Any] = []
        self.zombieDatas: List[Any] = []
        self.SpawnZombies: List[Any] = []
        self.orderedSpawns: List[Any] = []

    # =========================================================================
    # BUILDER HELPERS
    # =========================================================================

    def add_node(self, node: Any) -> Any:
        """Registers a low-level or composite node into the graph."""
        return self.graph.add_node(node, self.registry)

    def add_variable(self, var_asset: Any) -> Any:
        """Registers a persistent variable asset into the level references."""
        return self.graph.add_variable(var_asset, self.registry)

    def connect(self, from_node: Any, from_port: str, to_node: Any, to_port: str):
        """Wires two ports together in the execution or data graph."""
        return self.graph.connect(from_node, from_port, to_node, to_port)

    # =========================================================================
    # SERIALIZATION / EXPORT
    # =========================================================================

    def to_dict(self) -> Dict[str, Any]:
        """Compiles the full level dictionary matching Unity's IL2CPP JSON schema."""
        return {
            "scaryPots": list(self.scaryPots),
            "victoryType": self.victoryType,
            "boardConfig": self.boardConfig.to_dict(),
            "boardTag": self.boardTag.to_dict(),
            "rhythmLevelData": self.rhythmLevelData.to_dict(),
            "eventNodeGraph": self.graph.to_dict(),
            "plantDatas": list(self.plantDatas),
            "plants": list(self.plants),
            "preSelectCards": list(self.preSelectCards),
            "preSelectCards_zombie": list(self.preSelectCards_zombie),
            "GodShootingConfig": self.godShootingConfig.to_dict(),
            "advBuffs": list(self.advBuffs),
            "ultiBuffs2": list(self.ultiBuffs2),
            "ultiBuffs": list(self.ultiBuffs),
            "travelDebuffs": list(self.travelDebuffs),
            "zombieDatas": list(self.zombieDatas),
            "SpawnZombies": list(self.SpawnZombies),
            "orderedSpawns": list(self.orderedSpawns),
            "sceneType": self.sceneType,
            "levelType": self.levelType,
            "levelNumber": self.levelNumber,
            "name": self.name,
            "startSun": self.startSun,
            "maxWave": self.maxWave,
            "cardCount": self.cardCount,
            "references": {
                "version": 2,
                "RefIds": self.registry.dump_ref_ids(),
            },
        }

    def to_json(self, indent: int = 4) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def save(self, filepath: str) -> None:
        """Saves the compiled level to a JSON file."""
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    @classmethod
    def load(cls, filepath: str) -> Level:
        """Loads and parses an existing level JSON file into a Level object."""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        lvl = cls(
            name=data.get("name", "CustomLevel"),
            level_number=data.get("levelNumber", 9998),
            level_type=data.get("levelType", 11),
            scene_type=data.get("sceneType", 0),
            start_sun=data.get("startSun", 500),
            max_wave=data.get("maxWave", 10),
            card_count=data.get("cardCount", 14),
            victory_type=data.get("victoryType", 0),
        )
        if "boardConfig" in data:
            lvl.boardConfig = BoardConfig.from_dict(data["boardConfig"])
        if "boardTag" in data:
            lvl.boardTag = BoardTag.from_dict(data["boardTag"])
        if "rhythmLevelData" in data:
            lvl.rhythmLevelData = RhythmLevelData.from_dict(data["rhythmLevelData"])
        if "GodShootingConfig" in data:
            lvl.godShootingConfig = GodShootingConfig.from_dict(data["GodShootingConfig"])
        return lvl
