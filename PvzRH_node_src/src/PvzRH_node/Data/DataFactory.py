from typing import Any, Optional, Union, List, TYPE_CHECKING
from .TypeMgr import SceneType, LevelType, ZombieType,PlantType


def _to_json_val(val: Any) -> Any:
    """Recursively unwraps Enums, dicts, lists, and tuples into raw JSON values."""
    if hasattr(val, 'value'):
        return _to_json_val(val.value)
    if isinstance(val, dict):
        return {k: _to_json_val(v) for k, v in val.items()}
    if isinstance(val, (list, tuple, set)):
        return [_to_json_val(v) for v in val]
    return val


class BoardConfig:
    """Stores all configurable runtime parameters for board dynamics."""
    def __init__(self):
        self._dirty = False
        self._dirty_keys = set()
        self.izDropCount: int = 0
        self.redLineColumn: int = 5
        self.zombieStartAmmor: float = 0.0
        self.zombieHealthMultiplier: float = 1.0
        self.zombieDamageMultiplier: float = 1.0
        self.zombieSpeedMultiplier: float = 1.0
        self.zombieCountMultiplier: float = 1.0
        self.minOriginalSpeed: float = 1.0
        self.maxOriginalSpeed: float = 1.4
        self.waveInterval: float = 30.0
        """Default time interval in seconds between each wave spawn"""
        self.firstWaveArrivedTimer: float = 15.0
        """First wave arrival delay in seconds"""
        self.conveyInterval: float = 6.0
        self.gloveSpeed: float = 10.0
        """Cooldown for glove"""
        self.holdTimer: float = 4.2
        self.holdTimer2: float = 1.8
        self.holdTimer3: float = 5.0
        self.startTip: str = ""
        """Text to be displayed at the start of the level
        
        Change the time for which this text is shown by BoardConfig.tipTime
        """
        self.tipTime: float = 6.0
        """The time for which the start tip is displayed"""
        self.applyRandomData: bool = False
        """Enable Gacha random data generation"""
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

    def __setattr__(self, name, value):
        if not name.startswith("_"):
            super().__setattr__("_dirty", True)
            if hasattr(self, "_dirty_keys"):
                self._dirty_keys.add(name)
        super().__setattr__(name, value)

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class BoardTag:
    """Stores all active game modifier and mode flags."""
    def __init__(self):
        self._dirty = False
        self._dirty_keys = set()
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
        """Skips seed selection phase and directly start the level. 
        
        This doesn't disable the intro animation.
        use board_tag.disableInInterlude to disable it.
        """
        self.disableInInterlude: bool = False
        """Skips initial camera movement at the start of the level."""

    def __setattr__(self, name, value):
        if not name.startswith("_"):
            super().__setattr__("_dirty", True)
            if hasattr(self, "_dirty_keys"):
                self._dirty_keys.add(name)
        super().__setattr__(name, value)

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class PlantEntry:
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
        upgrade_type: int = 0
    ) -> dict[str, Any]:
        return {
            "thePlantColumn": col,
            "thePlantRow": row,
            "thePlantType": _to_json_val(plant_type),
            "thePlantHealth": health,
            "theLilyType": lily_type,
            "thePlantStage": stage,
            "theAttributeCount": attribute_count,
            "theLevel": level,
            "imitatless": imitatless,
            "diemeanlose": diemeanlose,
            "uncrashable": uncrashable,
            "starUp": star_up,
            "towards": towards,
            "upgradeType": upgrade_type,
            "objects": []
        }


class OrderedSpawn:
    """Factory helper for creating wave-ordered zombie spawns."""
    @staticmethod
    def create(
        wave: int,
        zombies: list[Any] | None = None,
        zombies_with_row: list[Any] | None = None
    ) -> dict[str, Any]:
        formatted_rows = []
        for item in (zombies_with_row or []):
            if isinstance(item, (tuple, list)) and len(item) == 2:
                # Flexibly handles both (ZombieType, row) and (row, ZombieType)
                first, second = item
                if isinstance(first, int) and not isinstance(first, bool) and not hasattr(first, 'value'):
                    z_type, row_num = second, first
                else:
                    z_type, row_num = first, second

                formatted_rows.append({
                    "zombieType": _to_json_val(z_type),
                    "row": row_num
                })
            elif isinstance(item, dict):
                formatted_rows.append({
                    "zombieType": _to_json_val(item.get("zombieType", item.get("zombie_type"))),
                    "row": item.get("row", -1)
                })
            else:
                formatted_rows.append({
                    "zombieType": _to_json_val(item),
                    "row": -1
                })

        return {
            "wave": wave,
            "zombies": [_to_json_val(z) for z in (zombies or [])],
            "zombiesWithRow": formatted_rows
        }


class GodPlant:
    """Builder for a God Mode plant, its upgrade routes, and stages."""
    def __init__(self, base_plant: Union['PlantType', str, Any]):
        self.base_plant = base_plant.name if hasattr(base_plant, 'name') else str(base_plant) #type: ignore
        self.routes: list[dict[str, Any]] = []
        self._current_route: Optional[dict[str, Any]] = None

    def add_route(self, route_name: str) -> 'GodPlant':
        """Creates a new upgrade route and sets it as the active route."""
        self._current_route = {
            "routeName": route_name,
            "stages": [],
            "stageCost": []
        }
        self.routes.append(self._current_route)
        return self

    def add_stage(
        self, 
        plant_type: Union['PlantType', str, Any], 
        cost: int,
        attack_damage: Union[int, float] = 0,
        attack_interval: float = 0.0,
        max_health: int = 0,
        attack_speed_adder: float = 0.0
    ) -> 'GodPlant':
        """Adds an upgrade stage and its cost to the most recently created route."""
        if self._current_route is None:
            raise ValueError("❌ Error: You must call add_route() before calling add_stage().")
            
        p_type = plant_type.name if hasattr(plant_type, 'name') else str(plant_type) #type: ignore
        
        self._current_route["stages"].append({
            "plantType": p_type,
            "attackDamage": attack_damage,
            "attackInterval": attack_interval,
            "maxHealth": max_health,
            "attackSpeedAdder": attack_speed_adder
        })
        self._current_route["stageCost"].append(cost)
        return self

    def to_dict(self) -> dict[str, Any]:
        """Serializes the complete GodPlant configuration for the level JSON."""
        return {
            "key": self.base_plant,
            "value": {
                "basePlant": self.base_plant,
                "routes": self.routes
            }
        } 


class LevelConfig:
    """Convenience proxy for builder level parameters with full IDE auto-completion."""

    # Type annotations for VS Code Pylance / IntelliSense
    name: str | None 
    """Name of the level"""
    level_number: Optional[int]
    """The unique id for the level"""
    scene_type: SceneType | int | None
    level_type: LevelType | int | None
    start_sun: Optional[int]
    max_wave: Optional[int]
    card_count: Optional[int]
    victory_type: Optional[int]
    """0: Normal Victory
    
    1: IZombie Victory"""

    plant_datas: Optional[List[dict[str, Any]]]
    """Advannced modifed data for each plant
    
    Add a new data by using add_plant_data()
    """
    plants: Optional[List[dict[str, Any]]]
    """Data of preplaced plants
    
    Add a new data by using add_plant()
    """
    pre_select_cards: Optional[List[Union[PlantType, int]]]
    """Plant cards that are preselected and cannot be removed"""
    pre_select_cards_zombie: Optional[List[Union[ZombieType, int]]]
    """Zombie cards that are preselected and cannot be removed"""
    
    adv_buffs: Optional[List[int]]
    ulti_buffs: Optional[List[int]]
    ulti_buffs2: Optional[List[int]]
    travel_debuffs: Optional[List[int]]

    spawn_zombies: Optional[List[Union[ZombieType, int]]]
    """Contains the list of allowd zombie to appear in the level"""
    ordered_spawns: Optional[List[dict[str, Any]]]
    """Data of custom ordered zombie spawn
    
    Add a new data by using add_ordered_spawn()
    """
    god_plants: Optional[List[dict[str, Any]]]
    board_config: BoardConfig
    board_tag: BoardTag

    if TYPE_CHECKING:
        from ..core import CompilerState
    def __init__(self, state: CompilerState):
        self._state = state

    # ==========================================================
    # LEVEL DATA BUILDER METHODS
    # ==========================================================
    def add_plant_data(self, plant_data: dict[str, Any]) -> None:
        """Appends plant stat overrides created via PlantData.create()."""
        if not isinstance(plant_data, dict):
            raise TypeError("❌ Error: Expected a dictionary generated by PlantData.create().")
        if self._state.plant_datas is None:
            self._state.plant_datas = []
        self._state.plant_datas.append(_to_json_val(plant_data))

    def add_plant(self, plant_entry: dict[str, Any]) -> None:
        """Appends a pre-placed board plant created via PlantEntry.create()."""
        if not isinstance(plant_entry, dict):
            raise TypeError("❌ Error: Expected a dictionary generated by PlantEntry.create().")
        if self._state.plants is None:
            self._state.plants = []
        self._state.plants.append(_to_json_val(plant_entry))

    def add_ordered_spawn(self, spawn_entry: dict[str, Any]) -> None:
        """Appends a wave spawn entry generated via OrderedSpawn.create()."""
        if not isinstance(spawn_entry, dict):
            raise TypeError("❌ Error: Expected a dictionary generated by OrderedSpawn.create().")
        if self._state.ordered_spawns is None:
            self._state.ordered_spawns = []
        self._state.ordered_spawns.append(_to_json_val(spawn_entry))

    def add_god_plant(self, god_plant: Union[GodPlant, dict[str, Any]]) -> None:
        """Appends a God Mode plant configuration."""
        if hasattr(god_plant, "to_dict"):
            data = god_plant.to_dict() #type: ignore
        elif isinstance(god_plant, dict):
            data = god_plant
        else:
            raise TypeError("❌ Error: Expected a GodPlant instance or dictionary.")
            
        if self._state.god_plants is None:
            self._state.god_plants = []
        self._state.god_plants.append(_to_json_val(data))
        
    # ==========================================================
    # PROXY ASSIGNMENT & ACCESS
    # ==========================================================
    def __setattr__(self, name: str, value: Any):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            unwrapped_val = _to_json_val(value)
            setattr(self._state, name, unwrapped_val)

    def __getattr__(self, name: str):
        if hasattr(self._state, name):
            return getattr(self._state, name)
        raise AttributeError(f"'LevelConfig' has no attribute '{name}'")


DEFAULT_LEVEL_TEMPLATE = {
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
        "notes": []
    },
    "eventNodeGraph": {
        "nodes": [],
        "connections": [],
        "variables": [],
        "groups": []
    },
    "plantDatas": [],
    "plants": [],
    "preSelectCards": [],
    "preSelectCards_zombie": [],
    "GodShootingConfig": {
        "plants": []
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
    "levelNumber": 1,
    "name": "Unnamed",
    "startSun": 500,
    "maxWave": 10,
    "cardCount": 14,
    "references": {
        "version": 2,
        "RefIds": []
    }
}
