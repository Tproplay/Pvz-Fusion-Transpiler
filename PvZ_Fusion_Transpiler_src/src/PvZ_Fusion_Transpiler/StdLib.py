from __future__ import annotations

from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Union
from ._Nodes.Extensions.UI.format_string import format_string
from ._Nodes.Extensions.Branching import If
from ._Nodes.Extensions.Variables import IntVar, FloatVar, BoolVar
from ._Nodes.Extensions.Entity import Plant, Zombie, PlantTypeList, ZombieTypeList
from ._Nodes.Extensions.Lawn import Lawnf
from ._Nodes.Extensions.Triggers import Trigger
from ._Data.TypeMgr import KeyCode, PlantType, ZombieType


class _wasd_key:
    def __init__(self) -> None:
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D


class WASDPlant:
    """Assigns WASD keys to control a plant's movement across the grid."""

    def __init__(self, plant: Plant | Any) -> None:
        if isinstance(plant, Plant):
            self.plant = plant
        else:
            self.plant = Plant(plant)
        self.wasd_keys = _wasd_key()

    def Start(self) -> None:
        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(col_diff=0, row_diff=-1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(col_diff=0, row_diff=1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(col_diff=-1, row_diff=0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(col_diff=1, row_diff=0)


class Dictionary:
    """A Virtual Dictionary (Global State Manager) utilizing Native Variables."""

    def __init__(self, schema: Optional[Dict[str, Any]] = None) -> None:
        self._store: Dict[str, Any] = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val: Any) -> None:
        if key in self._store:
            raise KeyError(f"Key '{key}' already exists!")

        if isinstance(initial_val, bool):
            self._store[key] = BoolVar(start_val=initial_val)
        elif isinstance(initial_val, float):
            self._store[key] = FloatVar(start_val=initial_val)
        elif isinstance(initial_val, int):
            self._store[key] = IntVar(start_val=initial_val)
        else:
            raise TypeError("Unsupported Dictionary type. Use int, float, or bool.")

    def __getitem__(self, key: str) -> Any:
        return self._store[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._store[key].set(value)

    def __getattr__(self, key: str) -> Any:
        if key in ("_store",):
            return super().__getattribute__(key)
        if "_store" in self.__dict__ and key in self._store:
            return self._store[key]
        return super().__getattribute__(key)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "_store":
            super().__setattr__(key, value)
        elif "_store" in self.__dict__ and key in self._store:
            self._store[key].set(value)
        else:
            super().__setattr__(key, value)


class Array:
    """A Pre-Allocated Virtual Array utilizing Native Variables."""

    def __init__(self, size: int, default_val: Any = 0) -> None:
        self.size = size
        self._store: List[Any] = []

        for _ in range(size):
            if isinstance(default_val, bool):
                self._store.append(BoolVar(start_val=default_val))
            elif isinstance(default_val, float):
                self._store.append(FloatVar(start_val=default_val))
            elif isinstance(default_val, int):
                self._store.append(IntVar(start_val=default_val))
            else:
                raise TypeError("Unsupported Array element type. Use int, float, or bool.")

    def __getitem__(self, index: int) -> Any:
        return self._store[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._store[index].set(value)

    def __len__(self) -> int:
        return self.size

    def read(self, index_port: Any, on_read_callback: Callable[[Any], None]) -> None:
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])

    def write(self, index_port: Any, value: Any) -> None:
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)


NumericVal = Union[float, int, FloatVar, IntVar, Any]


class StatManager:
    """High-level stat tracking system handling Global, Tag-based, and Individual modifiers
    for Plant ATK/HP and Zombie HP.
    """

    def __init__(self, base_plant_stat: float = 0.0, base_zombie_hp_mult: float = 1.0) -> None:
        self.base_plant_stat = base_plant_stat
        self.base_zombie_hp_mult = base_zombie_hp_mult

        self.global_atk = FloatVar(name="Global_ATK_Bonus")
        self.global_hp = FloatVar(name="Global_HP_Bonus")
        self.global_zombie_hp = FloatVar(name="Global_Zombie_HP_Mult")

        self.tags: Dict[str, Dict[str, Any]] = {}
        self.zombie_tags: Dict[str, Dict[str, Any]] = {}

        self.plant_vars: Dict[int, Dict[str, Any]] = {}
        self.zombie_vars: Dict[int, Dict[str, Any]] = {}

        self._calc_atk = FloatVar(name="Temp_Calc_ATK")
        self._calc_hp = FloatVar(name="Temp_Calc_HP")
        self._calc_zombie_hp = FloatVar(name="Temp_Calc_Zombie_HP")

    def create_tag(
        self, tag_name: str, plants: Union[PlantTypeList, Iterable[PlantType]]
    ) -> None:
        """Registers a category of plants that can receive shared stat buffs."""
        if not isinstance(plants, PlantTypeList):
            plants = PlantTypeList(list(plants))

        self.tags[tag_name] = {
            "plants": plants,
            "atk": FloatVar(name=f"Tag_{tag_name}_ATK"),
            "hp": FloatVar(name=f"Tag_{tag_name}_HP"),
        }

    def add_tag_atk(self, tag_name: str, value: NumericVal) -> None:
        """Adds an attack bonus to an entire registered plant tag."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered.")
        self.tags[tag_name]["atk"] += value

    def add_tag_hp(self, tag_name: str, value: NumericVal) -> None:
        """Adds a health bonus to an entire registered plant tag."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered.")
        self.tags[tag_name]["hp"] += value

    def _lazy_init_plant(self, plant_type: PlantType) -> Dict[str, Any]:
        if not isinstance(plant_type, Enum):
            raise TypeError("PlantType must be handled through the PlantType enum; direct int input is not allowed.")
        p_id = int(plant_type.value)
        if p_id not in self.plant_vars:
            name_str = plant_type.name
            self.plant_vars[p_id] = {
                "enum": plant_type,
                "atk": FloatVar(name=f"Plant_{name_str}_ATK"),
                "hp": FloatVar(name=f"Plant_{name_str}_HP"),
            }
        return self.plant_vars[p_id]

    def add_plant_atk(self, plant_type: PlantType, value: NumericVal) -> None:
        """Adds an attack bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["atk"] += value

    def add_plant_hp(self, plant_type: PlantType, value: NumericVal) -> None:
        """Adds a health bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["hp"] += value

    def create_zombie_tag(
        self, tag_name: str, zombies: Union[ZombieTypeList, Iterable[ZombieType]]
    ) -> None:
        """Registers a category of zombies that can receive shared health modifiers."""
        if not isinstance(zombies, ZombieTypeList):
            zombies = ZombieTypeList(list(zombies))

        self.zombie_tags[tag_name] = {
            "zombies": zombies,
            "hp": FloatVar(name=f"ZTag_{tag_name}_HP"),
        }

    def _lazy_init_zombie(self, zombie_type: ZombieType) -> Dict[str, Any]:
        if not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be handled through the ZombieType enum; direct int input is not allowed.")
        z_id = int(zombie_type.value)
        if z_id not in self.zombie_vars:
            name_str = zombie_type.name
            self.zombie_vars[z_id] = {
                "enum": zombie_type,
                "hp": FloatVar(name=f"Zombie_{name_str}_HP"),
            }
        return self.zombie_vars[z_id]

    def add_zombie_tag_hp(self, tag_name: str, value: NumericVal) -> None:
        """Adds a health multiplier to an entire registered zombie tag."""
        if tag_name not in self.zombie_tags:
            raise KeyError(f"Zombie tag '{tag_name}' is not registered.")
        self.zombie_tags[tag_name]["hp"] += value

    def add_zombie_hp(self, zombie_type: ZombieType, value: NumericVal) -> None:
        """Adds a health multiplier to a single specific zombie type."""
        self._lazy_init_zombie(zombie_type)["hp"] += value

    def get_atk_stat(self, plant_ref: Plant) -> FloatVar:
        """Compiles global, tag, and individual ATK buffs for a specific plant entity at runtime."""
        self._calc_atk.set(self.base_plant_stat + self.global_atk)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_atk += tag_data["atk"]
        for p_data in self.plant_vars.values():
            with If(PlantTypeList([p_data["enum"]]).contains(plant_ref.plantType)):
                self._calc_atk += p_data["atk"]
        return self._calc_atk

    def get_hp_stat(self, plant_ref: Plant) -> FloatVar:
        """Compiles global, tag, and individual HP buffs for a specific plant entity at runtime."""
        self._calc_hp.set(self.base_plant_stat + self.global_hp)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_hp += tag_data["hp"]
        for p_data in self.plant_vars.values():
            with If(PlantTypeList([p_data["enum"]]).contains(plant_ref.plantType)):
                self._calc_hp += p_data["hp"]
        return self._calc_hp

    def get_tag_atk_stat(self, tag_name: str) -> FloatVar:
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered.")
        return self.tags[tag_name]["atk"]

    def get_tag_hp_stat(self, tag_name: str) -> FloatVar:
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered.")
        return self.tags[tag_name]["hp"]

    def get_zombie_hp_stat(self, zombie_ref: Zombie) -> FloatVar:
        """Compiles global, tag, and individual HP multipliers for a specific zombie entity at runtime."""
        self._calc_zombie_hp.set(self.base_zombie_hp_mult + self.global_zombie_hp)
        for tag_data in self.zombie_tags.values():
            with If(tag_data["zombies"].contains(zombie_ref.zombieType)):
                self._calc_zombie_hp += tag_data["hp"]
        for z_data in self.zombie_vars.values():
            with If(ZombieTypeList([z_data["enum"]]).contains(zombie_ref.zombieType)):
                self._calc_zombie_hp += z_data["hp"]
        return self._calc_zombie_hp

    def get_zombie_tag_hp_stat(self, tag_name: str) -> FloatVar:
        if tag_name not in self.zombie_tags:
            raise KeyError(f"Zombie tag '{tag_name}' is not registered.")
        return self.zombie_tags[tag_name]["hp"]

    def apply_stats_to_plant(self, plant_ref: Plant) -> None:
        """Calculates and applies all applicable ATK and HP modifiers to a plant."""
        plant_ref.modify_attack(self.get_atk_stat(plant_ref))
        plant_ref.modify_health(self.get_hp_stat(plant_ref))

    def apply_stats_to_zombie(self, zombie_ref: Zombie) -> None:
        """Calculates and applies all applicable HP multipliers to a zombie."""
        zombie_ref.set_health_multiplier(self.get_zombie_hp_stat(zombie_ref))

    def refresh_all_plants(self) -> None:
        """Iterates through all active plants on the lawn and updates their stats."""
        with Lawnf.for_each_plant_on_lawn() as plant:
            self.apply_stats_to_plant(plant)


__all__ = ["format_string", "WASDPlant", "Dictionary", "Array", "StatManager"]
