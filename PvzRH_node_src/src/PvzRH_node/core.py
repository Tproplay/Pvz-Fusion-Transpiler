from __future__ import annotations

import copy
import json
import math
import os
import uuid
from typing import Any, List, Optional, Union

from .Data.TypeMgr import LevelType, PlantType, SceneType, ZombieType

# =====================================================================
# STATE TRACKING DATA STRUCTURES
# =====================================================================

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

# =====================================================================
# HELPER UTILITIES & DATA FACTORIES
# =====================================================================

def _to_json_val(val: Any) -> Any:
    """Recursively unwraps Enums, dicts, lists, and tuples into raw JSON values."""
    if hasattr(val, 'value'):
        return _to_json_val(val.value)
    if isinstance(val, dict):
        return {k: _to_json_val(v) for k, v in val.items()}
    if isinstance(val, (list, tuple, set)):
        return [_to_json_val(v) for v in val]
    return val


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

# =====================================================================
# COMPILER STATE & ENGINE
# =====================================================================

class CompilerSetting:
    group_level: int = 0
    spacing_x: float = 220.0
    spacing_y: float = 170.0
    hierarchical_spacing_x: float = 240.0
    hierarchical_spacing_y: float = 180.0

settings = CompilerSetting()


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

    board_config: BoardConfig
    board_tag: BoardTag

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


class CompilerState:
    def __init__(self) -> None:
        self.config = {"output": "./", "name": "exported level"}
        self.nodes = []
        self.connections = []
        self.trigger_stack = [] 
        self.registry = {}      
        self.variables = []

        self.group_level = settings.group_level
        self.spacing_x = settings.spacing_x
        self.spacing_y = settings.spacing_y
        self.hierarchical_spacing_x = settings.hierarchical_spacing_x
        self.hierarchical_spacing_y = settings.hierarchical_spacing_y
        self.groups_map = {}

        # LEVEL CONFIGURATION PROXY
        self.level_config = LevelConfig(self)

        self.board_config = BoardConfig()
        self.board_tag = BoardTag()

        self.name: Optional[str] = None
        self.level_number: Optional[int] = None
        self.scene_type: Optional[int] = None
        self.level_type: Optional[int] = None
        self.start_sun: Optional[int] = None
        self.max_wave: Optional[int] = None
        self.card_count: Optional[int] = None
        self.victory_type: Optional[int] = None

        self.plant_datas: Optional[List[dict[str, Any]]] = None
        self.plants: Optional[List[dict[str, Any]]] = None
        self.pre_select_cards: Optional[List[Any]] = None
        self.pre_select_cards_zombie: Optional[List[Any]] = None

        self.adv_buffs: Optional[List[int]] = None
        self.ulti_buffs: Optional[List[int]] = None
        self.ulti_buffs2: Optional[List[int]] = None
        self.travel_debuffs: Optional[List[int]] = None

        self.spawn_zombies: Optional[List[Any]] = None
        self.ordered_spawns: Optional[List[dict[str, Any]]] = None

    def _generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def add_connection(self, source_id: str, source_port: str, target_id: str, target_port: str) -> None:
        self.connections.append({
            "sourceNodeId": source_id,
            "sourcePortName": source_port,
            "targetNodeId": target_id,
            "targetPortName": target_port
        })

    def remove_connection(self, source_id: str = None, source_port: str = None, #type: ignore
                          target_id: str = None, target_port: str = None): #type: ignore
        original_count = len(self.connections)
        self.connections = [
            conn for conn in self.connections
            if not (
                (source_id is None or conn["sourceNodeId"] == source_id) and
                (source_port is None or conn["sourcePortName"] == source_port) and
                (target_id is None or conn["targetNodeId"] == target_id) and
                (target_port is None or conn["targetPortName"] == target_port)
            )
        ]
        return original_count - len(self.connections)

    def export(self) -> None:
        self.group_level = settings.group_level
        self.spacing_x = settings.spacing_x
        self.spacing_y = settings.spacing_y
        self.hierarchical_spacing_x = settings.hierarchical_spacing_x
        self.hierarchical_spacing_y = settings.hierarchical_spacing_y
        
        file_name = self.config.get("name", "exported level")
        file_path = os.path.join(self.config["output"], f"{file_name}.json")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        is_new_file = not os.path.exists(file_path)
        level_data = {}

        if not is_new_file:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    level_data = json.load(f)
                print(f"Modifying existing premade level data found at: {file_path}")
            except Exception as e:
                print(f"Warning: Failed to read existing file ({e}). Creating a fresh level instead.")
                is_new_file = True
                level_data = copy.deepcopy(DEFAULT_LEVEL_TEMPLATE)
        else:
            level_data = copy.deepcopy(DEFAULT_LEVEL_TEMPLATE)

        # =====================================================================
        # PASS 0: MERGE LEVEL CONFIGURATION DATA SELECTIVELY
        # =====================================================================
        if self.name is not None:
            level_data["name"] = self.name
        elif is_new_file:
            level_data["name"] = file_name if self.config.get("name") else "Unnamed"

        if self.level_number is not None:
            level_data["levelNumber"] = self.level_number
        elif is_new_file:
            level_data["levelNumber"] = 8001

        if self.scene_type is not None:
            level_data["sceneType"] = _to_json_val(self.scene_type)
        if self.level_type is not None:
            level_data["levelType"] = _to_json_val(self.level_type)
        if self.start_sun is not None:
            level_data["startSun"] = self.start_sun
        if self.max_wave is not None:
            level_data["maxWave"] = self.max_wave
        if self.card_count is not None:
            level_data["cardCount"] = self.card_count
        if self.victory_type is not None:
            level_data["victoryType"] = self.victory_type

        # Merge BoardConfig & BoardTag keys selectively
        if not is_new_file and "boardConfig" in level_data:
            for k in self.board_config._dirty_keys:
                level_data["boardConfig"][k] = getattr(self.board_config, k)
        elif self.board_config._dirty or is_new_file:
            level_data["boardConfig"] = self.board_config.to_dict()

        if not is_new_file and "boardTag" in level_data:
            for k in self.board_tag._dirty_keys:
                level_data["boardTag"][k] = getattr(self.board_tag, k)
        elif self.board_tag._dirty or is_new_file:
            level_data["boardTag"] = self.board_tag.to_dict()

        # List Overwrites (Only applied when explicitly configured)
        if self.plant_datas is not None:
            level_data["plantDatas"] = _to_json_val(self.plant_datas)
        if self.plants is not None:
            level_data["plants"] = _to_json_val(self.plants)
            for plant in level_data["plants"]:
                if isinstance(plant, dict):
                    plant["objects"] = []
        if self.pre_select_cards is not None:
            level_data["preSelectCards"] = _to_json_val(self.pre_select_cards)
        if self.pre_select_cards_zombie is not None:
            level_data["preSelectCards_zombie"] = _to_json_val(self.pre_select_cards_zombie)
        if self.adv_buffs is not None:
            level_data["advBuffs"] = _to_json_val(self.adv_buffs)
        if self.ulti_buffs is not None:
            level_data["ultiBuffs"] = _to_json_val(self.ulti_buffs)
        if self.ulti_buffs2 is not None:
            level_data["ultiBuffs2"] = _to_json_val(self.ulti_buffs2)
        if self.travel_debuffs is not None:
            level_data["travelDebuffs"] = _to_json_val(self.travel_debuffs)
        if self.spawn_zombies is not None:
            level_data["SpawnZombies"] = _to_json_val(self.spawn_zombies)
        if self.ordered_spawns is not None:
            level_data["orderedSpawns"] = _to_json_val(self.ordered_spawns)

        # =====================================================================
        # PASS 1: GRAPH OPTIMIZATION (DEDUPLICATION)
        # =====================================================================
        if self.group_level == 0:
            DEDUPE_TYPES = {
                "IntValueNode", "FloatValueNode", "BoolValueNode", "StringValueNode",
                "OnBoardStartNode", "OnPlantCreateNode", "OnPlantClickNode", 
                "OnPlantDieNode", "OnZombieDieNode", "OnZombieSpawnNode", "WaveEventNode",
                "OnMouseClickNode", "OnKeyPressNode", "OnPlantDeathCompleteNode"
            }

            unique_nodes = {} 
            remap_dict = {}   
            optimized_nodes = []

            for node in self.nodes:
                if node["type"] in DEDUPE_TYPES:
                    kwargs_signature = json.dumps(node.get("kwargs", {}), sort_keys=True)
                    signature = f"{node['type']}_{kwargs_signature}"
                    
                    if signature in unique_nodes:
                        remap_dict[node["id"]] = unique_nodes[signature]
                    else:
                        unique_nodes[signature] = node["id"]
                        optimized_nodes.append(node)
                else:
                    optimized_nodes.append(node)
                    
            self.nodes = optimized_nodes

            optimized_conns = []
            unique_conn_signatures = set()
            
            for conn in self.connections:
                src = remap_dict.get(conn["sourceNodeId"], conn["sourceNodeId"])
                tgt = remap_dict.get(conn["targetNodeId"], conn["targetNodeId"])
                
                conn_signature = f"{src}:{conn['sourcePortName']}->{tgt}:{conn['targetPortName']}"
                
                if conn_signature not in unique_conn_signatures:
                    unique_conn_signatures.add(conn_signature)
                    optimized_conns.append({
                        "sourceNodeId": src,
                        "sourcePortName": conn["sourcePortName"],
                        "targetNodeId": tgt,
                        "targetPortName": conn["targetPortName"]
                    })
            self.connections = optimized_conns

        # =====================================================================
        # PASS 2: LAYOUT ENGINE
        # =====================================================================
        node_positions = {}

        if self.group_level == 0:
            N = len(self.nodes)
            grid_size = int(math.ceil(math.sqrt(N))) if N > 0 else 1
            X_SPACING = self.spacing_x
            Y_SPACING = self.spacing_y
            
            in_degree = {node["id"]: 0 for node in self.nodes}
            adj = {node["id"]: [] for node in self.nodes}
            
            for conn in self.connections:
                src = conn["sourceNodeId"]
                tgt = conn["targetNodeId"]
                if src in in_degree and tgt in in_degree:
                    adj[src].append(tgt)
                    in_degree[tgt] += 1
                    
            queue = [n_id for n_id, deg in in_degree.items() if deg == 0]
            sorted_nodes = []
            
            while queue:
                curr = queue.pop(0)
                sorted_nodes.append(curr)
                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                        
            visited = set(sorted_nodes)
            for node in self.nodes:
                if node["id"] not in visited:
                    sorted_nodes.append(node["id"])
                    
            for index, n_id in enumerate(sorted_nodes):
                col = index % grid_size
                row = index // grid_size
                node_positions[n_id] = {"x": col * X_SPACING, "y": row * Y_SPACING}
        else:
            current_x = 0.0
            current_y = 120.0
            
            X_SPACING = self.hierarchical_spacing_x
            Y_SPACING = self.hierarchical_spacing_y
            ROW_RESET_LIMIT = 3.0
            
            group_index = 0
            max_row_height = 0.0
            
            for code_line, grp in self.groups_map.items():
                num_nodes = len(grp["nodeIds"])
                if num_nodes == 0:
                    continue
                
                if group_index > 0 and group_index % ROW_RESET_LIMIT == 0:
                    current_x = 0.0
                    current_y += max_row_height + 150.0 
                    max_row_height = 0.0
                
                group_grid_size = int(math.ceil(math.sqrt(num_nodes)))
                
                for index, n_id in enumerate(grp["nodeIds"]):
                    col = index % group_grid_size
                    row = index // group_grid_size
                    
                    node_positions[n_id] = {
                        "x": current_x + (col * X_SPACING),
                        "y": current_y + 80.0 + (row * Y_SPACING)
                    }
                    
                    node_height = 80.0 + (row * Y_SPACING)
                    max_row_height = max(max_row_height, node_height)
                
                grp["position"] = {"x": current_x - 30.0, "y": current_y}
                
                actual_cols = min(num_nodes, group_grid_size)
                group_width = actual_cols * X_SPACING
                current_x += group_width + 120.0
                
                group_index += 1

            positioned_node_ids = set(node_positions.keys())
            orphaned_node_ids = [n["id"] for n in self.nodes if n["id"] not in positioned_node_ids]

            if orphaned_node_ids:
                if current_x > 0.0:
                    current_x = 0.0
                    current_y += max_row_height + 150.0

                num_orphans = len(orphaned_node_ids)
                orphan_grid_size = int(math.ceil(math.sqrt(num_orphans)))

                orphan_group = {
                    "groupId": self._generate_uuid(),
                    "title": "Global Constants & Variables",
                    "nodeIds": orphaned_node_ids,
                    "position": {"x": current_x - 30.0, "y": current_y}
                }
                self.groups_map["Global Constants & Variables"] = orphan_group

                for index, n_id in enumerate(orphaned_node_ids):
                    col = index % orphan_grid_size
                    row = index // orphan_grid_size

                    node_positions[n_id] = {
                        "x": current_x + (col * X_SPACING),
                        "y": current_y + 80.0 + (row * Y_SPACING)
                    }

        # =====================================================================
        # PASS 3: NATIVE SCHEMA EXPORT STITCHING
        # =====================================================================
        level_data["eventNodeGraph"] = {
            "nodes": [],
            "connections": self.connections,
            "variables": [],
            "groups": []
        }
        level_data["references"] = {"version": 2, "RefIds": []}

        num_nodes = len(self.nodes)
        active_groups = [grp for grp in self.groups_map.values() if grp["nodeIds"]] if self.group_level >= 1 else []
        num_groups = len(active_groups)
        
        asset_rid_map = {}
        variables_list = getattr(self, "variables", [])
        next_asset_rid = 1000 + num_nodes + num_groups
        
        for var_asset in variables_list:
            old_rid = var_asset["rid"]
            asset_rid_map[old_rid] = next_asset_rid
            var_asset["rid"] = next_asset_rid
            next_asset_rid += 1

        current_rid = 1000
        for node in self.nodes:
            level_data["eventNodeGraph"]["nodes"].append({"rid": current_rid})
            pos = node_positions.get(node["id"], {"x": 0.0, "y": 0.0})

            node_data = {
                "nodeId": node["id"],
                "nodeType": node["type"],
                "position": pos,
                "nodeName": node["type"]
            }
            for key, value in node.get("kwargs", {}).items():
                node_data[key] = value

            if "asset" in node_data and isinstance(node_data["asset"], dict) and "rid" in node_data["asset"]:
                old_rid = node_data["asset"]["rid"]
                if old_rid in asset_rid_map:
                    node_data["asset"]["rid"] = asset_rid_map[old_rid]

            level_data["references"]["RefIds"].append({
                "rid": current_rid,
                "type": {"class": node["type"], "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                "data": node_data
            })
            current_rid += 1

        if self.group_level >= 1:
            for code_line, grp in self.groups_map.items():
                if not grp["nodeIds"]:
                    continue
                
                level_data["eventNodeGraph"]["groups"].append({"rid": current_rid})
                level_data["references"]["RefIds"].append({
                    "rid": current_rid,
                    "type": {"class": "NodeGroup", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                    "data": {
                        "groupId": grp["groupId"],
                        "title": grp.get("title", code_line),
                        "nodeIds": grp["nodeIds"],
                        "position": grp["position"],
                        "isFolded": False
                    }
                })
                current_rid += 1

        for var_asset in variables_list:
            level_data["eventNodeGraph"]["variables"].append({"rid": var_asset["rid"]})
            level_data["references"]["RefIds"].append(var_asset)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(level_data, f, indent=4, ensure_ascii=False)
            
        print(f"Successfully Packed and Exported to: {file_path}")


ctx = CompilerState()

def save_trigger_stack(clear: bool = True) -> list[Any]:
    """
    Saves a shallow copy of the active compiler trigger stack.
    If clear=True (default), clears ctx.trigger_stack to start an isolated execution tree.
    """
    saved_stack = ctx.trigger_stack[:]
    if clear:
        ctx.trigger_stack.clear()
    return saved_stack


def restore_trigger_stack(saved_stack: list[Any]) -> None:
    """
    Restores a previously saved trigger stack back into compiler context.
    """
    ctx.trigger_stack.clear()
    ctx.trigger_stack.extend(saved_stack)


class IsolatedTriggerScope:
    """
    Context manager that automatically saves/clears the trigger stack on entry
    and restores it on exit.
    """
    def __enter__(self):
        self.saved_stack = save_trigger_stack(clear=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        restore_trigger_stack(self.saved_stack)