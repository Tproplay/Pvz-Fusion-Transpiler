"""
Generalized RPG-style stat tracking and entity stat management system.
"""

from __future__ import annotations
from typing import Any, Dict, Iterable, Union

from ...Data.TypeMgr import PlantType, ZombieType
from ...Nodes.Extentions.extensions import FloatVar, IntVar, If, PlantTypeList, Plant, Zombie
from ...node_base import PortReference
from ...api import Lawnf
from .collections import ZombieTypeList

NumericVal = Union[float, int, FloatVar, IntVar, PortReference, Any]


class StatManager:
    """A high-performance, generalized RPG-style stat tracking system.
    
    Handles Global, Tag-based (Categories), and Individual modifiers for Plant ATK/HP 
    and Zombie HP, abstracting complex math and loops.

    Example:
    ```python
    stats = pvn.StdLib.StatManager(base_plant_stat=1.0)
    stats.create_tag("FirePlants", [PlantType.CherryBomb, PlantType.Jalapeno])
    
    # Add a 50% damage buff to all fire plants
    stats.add_tag_atk("FirePlants", 0.5)
    
    with pvn.Trigger.OnPlantCreate() as plant:
        stats.apply_stats_to_plant(plant)
    ```
    """

    def __init__(self, base_plant_stat: float = 0.0, base_zombie_hp_mult: float = 1.0) -> None:
        self.base_plant_stat = base_plant_stat
        self.base_zombie_hp_mult = base_zombie_hp_mult

        self.global_atk = FloatVar(name="Global_ATK_Bonus")
        self.global_hp = FloatVar(name="Global_HP_Bonus")
        self.global_zombie_hp = FloatVar(name="Global_Zombie_HP_Mult")

        self.tags: Dict[str, Dict[str, Any]] = {}
        self.zombie_tags: Dict[str, Dict[str, Any]] = {}

        self.plant_vars: Dict[int, Dict[str, FloatVar]] = {}
        self.zombie_vars: Dict[int, Dict[str, FloatVar]] = {}

        self._calc_atk = FloatVar(name="Temp_Calc_ATK")
        self._calc_hp = FloatVar(name="Temp_Calc_HP")
        self._calc_zombie_hp = FloatVar(name="Temp_Calc_Zombie_HP")

    def create_tag(
        self, tag_name: str, plants: Union[PlantTypeList, Iterable[Union[PlantType, int]]]
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

    def _lazy_init_plant(self, plant_type: Union[PlantType, int]) -> Dict[str, FloatVar]:
        p_id = int(plant_type.value if hasattr(plant_type, "value") else plant_type)  # type: ignore
        if p_id not in self.plant_vars:
            name_str = plant_type.name if hasattr(plant_type, "name") else str(p_id)  # type: ignore
            self.plant_vars[p_id] = {
                "atk": FloatVar(name=f"Plant_{name_str}_ATK"),
                "hp": FloatVar(name=f"Plant_{name_str}_HP"),
            }
        return self.plant_vars[p_id]

    def add_plant_atk(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds an attack bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["atk"] += value

    def add_plant_hp(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds a health bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["hp"] += value

    def create_zombie_tag(
        self, tag_name: str, zombies: Union[ZombieTypeList, Iterable[Union[ZombieType, int]]]
    ) -> None:
        """Registers a category of zombies that can receive shared health modifiers."""
        if not isinstance(zombies, ZombieTypeList):
            zombies = ZombieTypeList(list(zombies))

        self.zombie_tags[tag_name] = {
            "zombies": zombies,
            "hp": FloatVar(name=f"ZTag_{tag_name}_HP"),
        }

    def _lazy_init_zombie(self, zombie_type: Union[ZombieType, int]) -> Dict[str, FloatVar]:
        z_id = int(zombie_type.value if hasattr(zombie_type, "value") else zombie_type)  # type: ignore
        if z_id not in self.zombie_vars:
            name_str = zombie_type.name if hasattr(zombie_type, "name") else str(z_id)  # type: ignore
            self.zombie_vars[z_id] = {
                "hp": FloatVar(name=f"Zombie_{name_str}_HP"),
            }
        return self.zombie_vars[z_id]

    def add_zombie_tag_hp(self, tag_name: str, value: NumericVal) -> None:
        """Adds a health multiplier to an entire registered zombie tag."""
        if tag_name not in self.zombie_tags:
            raise KeyError(f"Zombie tag '{tag_name}' is not registered.")
        self.zombie_tags[tag_name]["hp"] += value

    def add_zombie_hp(self, zombie_type: Union[ZombieType, int], value: NumericVal) -> None:
        """Adds a health multiplier to a single specific zombie type."""
        self._lazy_init_zombie(zombie_type)["hp"] += value

    def get_atk_stat(self, plant_ref: Plant) -> FloatVar:
        """Compiles global, tag, and individual ATK buffs for a specific plant entity at runtime."""
        self._calc_atk.set(self.base_plant_stat + self.global_atk)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_atk += tag_data["atk"]
        for p_id, p_vars in self.plant_vars.items():
            with If(PlantTypeList([p_id]).contains(plant_ref.plantType)):
                self._calc_atk += p_vars["atk"]
        return self._calc_atk

    def get_hp_stat(self, plant_ref: Plant) -> FloatVar:
        """Compiles global, tag, and individual HP buffs for a specific plant entity at runtime."""
        self._calc_hp.set(self.base_plant_stat + self.global_hp)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_hp += tag_data["hp"]
        for p_id, p_vars in self.plant_vars.items():
            with If(PlantTypeList([p_id]).contains(plant_ref.plantType)):
                self._calc_hp += p_vars["hp"]
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
        for z_id, z_vars in self.zombie_vars.items():
            with If(ZombieTypeList([z_id]).contains(zombie_ref.zombieType)):
                self._calc_zombie_hp += z_vars["hp"]
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


class PlantStatsManager(StatManager):
    """Specialized StatManager focused exclusively on plant stats and category buffs."""
    pass


class StatPreset:
    """Predefined stat modifier templates for common RPG archetypes."""

    TANK_ATK = 0.5
    TANK_HP = 3.0

    GLASS_CANNON_ATK = 2.5
    GLASS_CANNON_HP = 0.5

    BALANCED_ATK = 1.0
    BALANCED_HP = 1.0


__all__ = [
    "NumericVal",
    "StatManager",
    "PlantStatsManager",
    "StatPreset",
]
