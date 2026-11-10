from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional, Union
from enum import Enum


def _to_json_val(val: Any) -> Any:
    """Recursively unwraps Enums, tuples, lists, and dicts into JSON-compatible values."""
    if hasattr(val, "value"):
        inner = val.value
        # For TravelBuffType like ("AdvBuff", 0), unwrap to the integer index
        if isinstance(inner, tuple) and len(inner) == 2 and isinstance(inner[1], int):
            return inner[1]
        return _to_json_val(inner)
    if isinstance(val, dict):
        return {k: _to_json_val(v) for k, v in val.items()}
    if isinstance(val, (list, tuple, set)):
        return [_to_json_val(v) for v in val]
    return val


class BoardConfig:
    """Stores all configurable runtime parameters for board dynamics."""

    def __init__(self) -> None:
        self._dirty: bool = False
        self.izDropCount: int = 0
        self.redLineColumn: int = 5
        self.ignoreZombieHouse: bool = False
        self.zombieStartAmmor: float = 0.0
        self.zombieHealthMultiplier: float = 1.0
        self.zombieDamageMultiplier: float = 1.0
        self.zombieSpeedMultiplier: float = 1.0
        self.zombieCountMultiplier: float = 1.0
        self.minOriginalSpeed: float = 1.0
        self.maxOriginalSpeed: float = 1.4
        self.waveInterval: float = 30.0
        self.firstWaveArrivedTimer: float = 15.0
        self.conveyInterval: float = 6.0
        self.gloveSpeed: float = 10.0
        self.holdTimer: float = 4.2
        self.holdTimer2: float = 1.8
        self.holdTimer3: float = 5.0
        self.startTip: str = ""
        self.tipTime: float = 6.0
        self.applyRandomData: bool = False
        self.plantModifyMin: float = 0.2
        self.plantModifyMax: float = 6.0
        self.plantSpeedMin: float = 0.2
        self.plantSpeedMax: float = 6.0
        self.plantSpeedAvg: float = 1.5
        self.zombieModifyMin: float = 0.1
        self.zombieModifyMax: float = 10.0
        self.zombieModifyAvg: float = 3.0
        self.zombieSpeedMin: float = 0.3
        self.zombieSpeedMax: float = 4.0
        self.zombieSpeedAvg: float = 1.5
        self.zombieScaleMin: float = 0.3
        self.zombieScaleMax: float = 2.5
        self.zombieScaleAvg: float = 1.0
        super().__setattr__("_dirty", False)

    def __setattr__(self, name: str, value: Any) -> None:
        if not name.startswith("_"):
            super().__setattr__("_dirty", True)
        super().__setattr__(name, value)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class BoardTag:
    """Stores all active game modifier and mode flags."""

    def __init__(self) -> None:
        self._dirty: bool = False
        self.waveLeaders: bool = False
        self.evolutionWar: bool = False
        self.rhythmGame: bool = False
        self.imZombieBoss: bool = False
        self.allScaryPotShow: bool = False
        self.customEdit: bool = False
        self.allCards: bool = False
        self.isIZ: bool = False
        self.HorseBoss: bool = False
        self.Iz_ai: bool = False
        self.rShowHealth: bool = False
        self.lessSun: bool = False
        self.lessMoney: bool = False
        self.zombieDropSun: bool = False
        self.disableNormalSun: bool = False
        self.zombieRevive: bool = False
        self.isScaredyDream: bool = False
        self.isTowerDefence: bool = False
        self.isShooting: bool = False
        self.rogueShooting: bool = False
        self.newShooting: bool = False
        self.isSeedRain: bool = False
        self.isIndestructible: bool = False
        self.isColumn: bool = False
        self.isSuperRandom: bool = False
        self.isNormalRandom: bool = False
        self.isElementRandom: bool = False
        self.isDrawCards: bool = False
        self.isUltimateSuperRandom: bool = False
        self.isNight: bool = False
        self.isBigMap: bool = False
        self.freeCamera: bool = False
        self.isEndless: bool = False
        self.isTravel: bool = False
        self.isEasyTravel: bool = False
        self.randomTravel: bool = False
        self.superCustomEditorMode: bool = False
        self.enableTravelPlant: bool = False
        self.enableAllTravelPlant: bool = False
        self.enableTravelBuff: bool = False
        self.isRoof: bool = False
        self.isGarden: bool = False
        self.isMirror: bool = False
        self.isConvey: bool = False
        self.isExchange: bool = False
        self.shooting_loon: bool = False
        self.isBoss: bool = False
        self.isBoss2: bool = False
        self.isFreeCardSelect: bool = False
        self.isTutor: bool = False
        self.isObsidianImp: bool = False
        self.isDixMix: bool = False
        self.isSingle: bool = False
        self.bungiBattle: bool = False
        self.isBejeweled: bool = False
        self.isBubbleGame: bool = False
        self.isScaryPot: bool = False
        self.isMidMap: bool = False
        self.isChess: bool = False
        self.isMidMap2: bool = False
        self.isLookStar: bool = False
        self.isGardenBattle: bool = False
        self.isRandomMix: bool = False
        self.isRandomMix2: bool = False
        self.freeGloveZombie: bool = False
        self.disableMower: bool = False
        self.isHappyRandom: bool = False
        self.oppsiteBuff: bool = False
        self.pvpScaryPot: bool = False
        self.pvpRandom: bool = False
        self.ultimateEndless: bool = False
        self.isHammerZombie: bool = False
        self.fastZombie: bool = False
        self.isHugeGravity: bool = False
        self.zombieSplit: bool = False
        self.fullStrike: bool = False
        self.billiardBall: bool = False
        self.isSnake: bool = False
        self.isSquash: bool = False
        self.zombieBattle: bool = False
        self.plantingZombie: bool = False
        self.is2048: bool = False
        self.isRogue: bool = False
        self.isFruitNinjia: bool = False
        self.isFruitNinjia2: bool = False
        self.lightShadow: bool = False
        self.isLoonGame: bool = False
        self.snowBoss: bool = False
        self.playerShooting: bool = False
        self.smallZombie: bool = False
        self.isFlagGame: bool = False
        self.isTreasure: bool = False
        self.isBrick: bool = False
        self.disableSummonZombie: bool = False
        self.disableSelectCard: bool = False
        self.disableInInterlude: bool = False
        super().__setattr__("_dirty", False)

    def __setattr__(self, name: str, value: Any) -> None:
        if not name.startswith("_"):
            super().__setattr__("_dirty", True)
        super().__setattr__(name, value)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class PlantData:
    """Helper factory for configuring custom plant stats in plantDatas."""

    @staticmethod
    def create(
        plant_type: Any,
        cost: int = 100,
        cd: float = 10.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        return {
            "thePlantType": _to_json_val(plant_type),
            "attackInterval": float(attack_interval),
            "produceInterval": float(produce_interval),
            "attackDamage": int(attack_damage),
            "maxHealth": int(max_health),
            "cd": float(cd),
            "cost": int(cost),
        }


class PlantEntry:
    """Helper factory for pre-placing plants on the board at level start."""

    @staticmethod
    def create(
        row: int,
        col: int,
        plant_type: Any,
        health: int = 300,
        stage: int = 0,
        lily_type: int = -1,
        attribute_count: int = 0,
        level: int = 0,
        imitatless: bool = False,
        diemeanlose: bool = False,
        uncrashable: bool = False,
        star_up: bool = False,
        towards: int = 0,
        upgrade_type: int = 0,
    ) -> Dict[str, Any]:
        return {
            "thePlantColumn": int(col),
            "thePlantRow": int(row),
            "thePlantType": _to_json_val(plant_type),
            "thePlantHealth": int(health),
            "theLilyType": int(lily_type),
            "thePlantStage": int(stage),
            "theAttributeCount": int(attribute_count),
            "theLevel": int(level),
            "imitatless": bool(imitatless),
            "diemeanlose": bool(diemeanlose),
            "uncrashable": bool(uncrashable),
            "starUp": bool(star_up),
            "towards": int(towards),
            "upgradeType": int(upgrade_type),
            "objects": [],
        }


class OrderedSpawn:
    """Helper factory for configuring wave-ordered zombie spawns."""

    @staticmethod
    def create(
        wave: int,
        zombies: Optional[List[Any]] = None,
        zombies_with_row: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        formatted_rows: List[Dict[str, Any]] = []
        for item in (zombies_with_row or []):
            if isinstance(item, (tuple, list)) and len(item) == 2:
                first, second = item
                if isinstance(first, int) and not isinstance(first, bool) and not hasattr(first, "value"):
                    z_type, row_num = second, first
                else:
                    z_type, row_num = first, second

                formatted_rows.append({
                    "zombieType": _to_json_val(z_type),
                    "row": int(row_num),
                })
            elif isinstance(item, dict):
                formatted_rows.append({
                    "zombieType": _to_json_val(item.get("zombieType", item.get("zombie_type"))),
                    "row": int(item.get("row", -1)),
                })
            else:
                formatted_rows.append({
                    "zombieType": _to_json_val(item),
                    "row": -1,
                })

        return {
            "wave": int(wave),
            "zombies": [_to_json_val(z) for z in (zombies or [])],
            "zombiesWithRow": formatted_rows,
        }


DEFAULT_LEVEL_TEMPLATE: Dict[str, Any] = {
    "scaryPots": [],
    "victoryType": 0,
    "boardConfig": BoardConfig().to_dict(),
    "boardTag": BoardTag().to_dict(),
    "rhythmLevelData": {
        "musicType": 13,
        "musicName": "song",
        "fallTime": 1.0,
        "bpm": 160.0,
        "audioOffset": 0.0,
        "notes": [],
    },
    "eventNodeGraph": {
        "nodes": [],
        "connections": [],
        "variables": [],
        "groups": [],
        "executionVersion": 1,
    },
    "plantDatas": [],
    "plants": [],
    "preSelectCards": [],
    "preSelectCards_zombie": [],
    "GodShootingConfig": {
        "plants": [],
    },
    "advBuffs": [],
    "ultiBuffs2": [],
    "ultiBuffs": [],
    "travelDebuffs": [],
    "zombieDatas": [],
    "SpawnZombies": [],
    "orderedSpawns": [],
    "sceneType": 0,
    "levelType": 11,
    "levelNumber": 8001,
    "name": "Test",
    "startSun": 500,
    "maxWave": 10,
    "cardCount": 14,
    "references": {
        "version": 2,
        "RefIds": [],
    },
}


class LevelConfig:
    """Manages all game-level configurations, rules, and initial wave layouts."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._dirty: bool = False
        self.board_config: BoardConfig = BoardConfig()
        self.board_tag: BoardTag = BoardTag()

        self.level_number: Optional[int] = None
        self.scene_type: Optional[Any] = None
        self.level_type: Optional[Any] = None
        self.start_sun: Optional[int] = None
        self.max_wave: Optional[int] = None
        self.card_count: Optional[int] = None
        self.victory_type: Optional[int] = None

        self.plant_datas: Optional[List[Dict[str, Any]]] = None
        self.plants: Optional[List[Dict[str, Any]]] = None
        self.pre_select_cards: Optional[List[Any]] = None
        self.pre_select_cards_zombie: Optional[List[Any]] = None

        self.adv_buffs: Optional[List[Any]] = None
        self.ulti_buffs: Optional[List[Any]] = None
        self.ulti_buffs2: Optional[List[Any]] = None
        self.travel_debuffs: Optional[List[Any]] = None

        self.spawn_zombies: Optional[List[Any]] = None
        self.ordered_spawns: Optional[List[Dict[str, Any]]] = None
        super().__setattr__("_dirty", False)

    def __setattr__(self, name: str, value: Any) -> None:
        if not name.startswith("_"):
            super().__setattr__("_dirty", True)
        super().__setattr__(name, value)

    def is_dirty(self) -> bool:
        return (
            self._dirty
            or self.board_config._dirty
            or self.board_tag._dirty
            or self.level_number is not None
            or self.scene_type is not None
            or self.level_type is not None
            or self.start_sun is not None
            or self.max_wave is not None
            or self.card_count is not None
            or self.victory_type is not None
            or self.plant_datas is not None
            or self.plants is not None
            or self.pre_select_cards is not None
            or self.pre_select_cards_zombie is not None
            or self.adv_buffs is not None
            or self.ulti_buffs is not None
            or self.ulti_buffs2 is not None
            or self.travel_debuffs is not None
            or self.spawn_zombies is not None
            or self.ordered_spawns is not None
        )

    def add_plant_data(self, plant_data: Dict[str, Any]) -> None:
        if self.plant_datas is None:
            self.plant_datas = []
        self.plant_datas.append(_to_json_val(plant_data))
        self._dirty = True

    def add_plant(self, plant_entry: Dict[str, Any]) -> None:
        if self.plants is None:
            self.plants = []
        self.plants.append(_to_json_val(plant_entry))
        self._dirty = True

    def add_ordered_spawn(self, spawn_entry: Dict[str, Any]) -> None:
        if self.ordered_spawns is None:
            self.ordered_spawns = []
        self.ordered_spawns.append(_to_json_val(spawn_entry))
        self._dirty = True

    def merge_into(self, target_data: Dict[str, Any], file_name: Optional[str] = None) -> None:
        """Merges all configured level parameters into target_data dictionary."""
        if file_name and ("name" not in target_data or target_data.get("name") in ("", "Test", "exported level", "Untitled")):
            target_data["name"] = file_name

        if self.level_number is not None:
            target_data["levelNumber"] = int(self.level_number)
        if self.scene_type is not None:
            target_data["sceneType"] = _to_json_val(self.scene_type)
        if self.level_type is not None:
            target_data["levelType"] = _to_json_val(self.level_type)
        if self.start_sun is not None:
            target_data["startSun"] = int(self.start_sun)
        if self.max_wave is not None:
            target_data["maxWave"] = int(self.max_wave)
        if self.card_count is not None:
            target_data["cardCount"] = int(self.card_count)
        if self.victory_type is not None:
            target_data["victoryType"] = int(self.victory_type)

        if self.board_config._dirty or "boardConfig" not in target_data:
            target_data["boardConfig"] = self.board_config.to_dict()
        if self.board_tag._dirty or "boardTag" not in target_data:
            target_data["boardTag"] = self.board_tag.to_dict()

        if self.plant_datas is not None:
            target_data["plantDatas"] = _to_json_val(self.plant_datas)
        if self.plants is not None:
            target_data["plants"] = _to_json_val(self.plants)
        if self.pre_select_cards is not None:
            target_data["preSelectCards"] = _to_json_val(self.pre_select_cards)
        if self.pre_select_cards_zombie is not None:
            target_data["preSelectCards_zombie"] = _to_json_val(self.pre_select_cards_zombie)
        if self.adv_buffs is not None:
            target_data["advBuffs"] = _to_json_val(self.adv_buffs)
        if self.ulti_buffs is not None:
            target_data["ultiBuffs"] = _to_json_val(self.ulti_buffs)
        if self.ulti_buffs2 is not None:
            target_data["ultiBuffs2"] = _to_json_val(self.ulti_buffs2)
        if self.travel_debuffs is not None:
            target_data["travelDebuffs"] = _to_json_val(self.travel_debuffs)
        if self.spawn_zombies is not None:
            target_data["SpawnZombies"] = _to_json_val(self.spawn_zombies)
        if self.ordered_spawns is not None:
            target_data["orderedSpawns"] = _to_json_val(self.ordered_spawns)


__all__ = [
    "BoardConfig",
    "BoardTag",
    "PlantData",
    "PlantEntry",
    "OrderedSpawn",
    "LevelConfig",
    "DEFAULT_LEVEL_TEMPLATE",
]
