"""Contains some useful functions and classes for level creation and manipulation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Iterable
from enum import Enum


from ..Data.TypeMgr import KeyCode
from .extensions import *
from ..core import IsolatedTriggerScope
from ..node_base import PortReference

__all__ = [
    "format_string",
    "Dictionary",
    "Array",
    "Counter",
    "StatManager",
    "WASDPlant",
    "ZombieTypeList",
]

def format_string(*args):
    """
    Dynamically chains text, variables, node ports, and constants into a single string port.
    """
    if not args:
        from ..nodes import string_value

        return string_value(val="").value

    from ..node_base import PortReference
    from ..nodes import string_concat, string_value

    def _parse_arg(arg):
        # 1. Objects with explicit .to_string() method
        if hasattr(arg, "to_string") and callable(arg.to_string):
            return arg.to_string()

        # 2. PortReference instances (math/logic node outputs)
        if isinstance(arg, PortReference):
            return arg._to_string_port()

        # 3. Node outputs wrapped in objects exposing a .node attribute
        if hasattr(arg, "node"):
            from ..node_base import PortReference as PR

            port_name = getattr(arg, "port_name", getattr(arg, "out_port", "Output"))
            return PR(arg.node, port_name)._to_string_port()

        # 4. Python Booleans (True / False)
        if isinstance(arg, bool):
            return string_value(val="True" if arg else "False").value

        # 5. Python Enums
        if isinstance(arg, Enum):
            return string_value(val=arg.name).value

        # 6. Primitive Fallback (str, int, float)
        return string_value(val=str(arg)).value

    current_chain = _parse_arg(args[0])

    if len(args) == 1:
        return current_chain

    for i in range(1, len(args)):
        next_piece = _parse_arg(args[i])
        current_chain = string_concat(a=current_chain, b=next_piece).result

    return current_chain



from ..api import *

class ZombieTypeList:
    """
    A static wrapper representing a list of Zombie Types.
    Since native zombie list storage nodes are unavailable, this manages a Python-side set
    and dynamically generates an OR-chained comparison graph at transpilation time.
    """

    def __init__(self, initial: Any | None = None):
        self._items: set[int] = set()
        if initial is not None:
            self.add(initial)

    def _extract_id(self, item: Any) -> int:
        """Helper to extract the raw integer ID from an Enum, int, or wrapped value."""
        if hasattr(item, "value"):
            return int(item.value)
        return int(item)

    # =========================================================================
    # STATIC LIST MANAGEMENT (Runs in Python during Transpilation)
    # =========================================================================

    def add(self, item: Any) -> ZombieTypeList:
        if isinstance(item, (list, tuple, set)) and not isinstance(item, PortReference):
            for i in item:
                self.add(i)
        elif isinstance(item, ZombieTypeList):
            self._items.update(item._items)
        else:
            self._items.add(self._extract_id(item))
        return self

    def remove(self, item: Any) -> ZombieTypeList:
        if isinstance(item, (list, tuple, set)) and not isinstance(item, PortReference):
            for i in item:
                self.remove(i)
        elif isinstance(item, ZombieTypeList):
            self._items.difference_update(item._items)
        else:
            self._items.discard(self._extract_id(item))
        return self

    def __iadd__(self, other: Any) -> ZombieTypeList:
        return self.add(other)

    def __add__(self, other: Any) -> ZombieTypeList:
        copy_list = ZombieTypeList(self._items)
        return copy_list.add(other)

    def __isub__(self, other: Any) -> ZombieTypeList:
        return self.remove(other)

    def __sub__(self, other: Any) -> ZombieTypeList:
        copy_list = ZombieTypeList(self._items)
        return copy_list.remove(other)

    @property
    def count(self) -> PortReference:
        """Returns a graph node representing the static length of this list."""
        return nodes.int_value(val=len(self._items)).value #type: ignore

    # =========================================================================
    # GRAPH GENERATION (Runs on Node Canvas)
    # =========================================================================

    def contains(self, target_type: PortReference | Enum | int | Any) -> PortReference:
        """
        Builds a graph to check if target_type is in this static list.
        Generates a sequence of compare_zombie_type nodes chained with logical OR.
        """
        # 1. Edge Case: List is empty
        if not self._items:
            return nodes.bool_value(val=False).value #type: ignore

        # 2. Edge Case: Static check if target_type is just an integer/enum, not a graph port
        if not isinstance(target_type, PortReference) and not hasattr(target_type, "node"):
            target_id = self._extract_id(target_type)
            return nodes.bool_value(val=(target_id in self._items)).value #type: ignore

        # 3. Dynamic Graph Generation: Chain comparisons with OR (|)
        result_wire = None
        for z_id in self._items:
            # Generate the literal value node for this specific stored zombie type
            z_node = nodes.zombie_type_value(val=z_id)
            z_port = z_node.value if hasattr(z_node, "value") else z_node

            # Compare it with the target incoming port
            compare_node = nodes.compare_zombie_type(a=target_type, b=z_port)
            is_equal = compare_node.equal

            # Chain the logic gates: (target == ID_1) OR (target == ID_2) OR ...
            if result_wire is None:
                result_wire = is_equal
            else:
                result_wire = result_wire | is_equal

        return result_wire #type: ignore


class _wasd_key:
    def __init__(self):
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D


class WASDPlant:
    """Assigns WaSD keys to control a plant in the game."""

    def __init__(self, plant: Plant | Any):

        if isinstance(plant, Plant):
            self.plant = plant
        else:
            self.plant = Plant(plant)

        self.wasd_keys = _wasd_key()

    def Start(self):

        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(0, -1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(0, 1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(-1, 0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(1, 0)


class Dictionary:
    """A Virtual Dictionary (Global State Manager) utilizing Native Variables."""

    def __init__(self, schema: dict | None = None):  # type: ignore
        self._store = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val):  # type: ignore
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

    def __getitem__(self, key):
        return self._store[key]

    def __setitem__(self, key, value):
        self._store[key].set(value)

    def __getattr__(self, key):
        return self._store[key]

    def __setattr__(self, key, value):
        if key == "_store":
            super().__setattr__(key, value)
        else:
            self._store[key].set(value)


class Array:
    """A Pre-Allocated Virtual Array utilizing Native Variables."""

    def __init__(self, size: int, default_val=0):
        self.size = size
        self._store = []

        for _ in range(size):
            if isinstance(default_val, bool):
                self._store.append(BoolVar(start_val=default_val))
            elif isinstance(default_val, float):
                self._store.append(FloatVar(start_val=default_val))
            elif isinstance(default_val, int):
                self._store.append(IntVar(start_val=default_val))

    def __getitem__(self, index: int):
        return self._store[index]

    def __setitem__(self, index: int, value):
        self._store[index].set(value)

    def __len__(self):
        return self.size

    def read(self, index_port, on_read_callback):
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])

    def write(self, index_port, value):
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)


class Counter:
    """
    A high-level wrapper for the Engine's native CounterNode.

    Usage:
        zombie_counter = pvn.Counter(start_val=0, reset_condition=is_wave_over)

        with pvn.nodes.on_zombie_die().trigger:
            zombie_counter.up()
    """

    def __init__(self, start_val=0, reset_condition=None):
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        self.ref = nodes.counter_node(start_val=start_val, reset=reset_condition)

        ctx.trigger_stack.extend(saved_stack)

    def up(self):
        """Increments the counter by 1 manually along the current execution timeline track."""
        if ctx.trigger_stack:
            previous_exec = ctx.trigger_stack[-1]
            ctx.add_connection(
                previous_exec.id, previous_exec.out_trigger, self.ref.id, "触发"
            )

            ctx.trigger_stack[-1] = ExecutionPath(self.ref.id, "触发")
        return self

    @property
    def value(self):
        """Returns the data output port reference containing the current count."""
        return self.ref.count

    @property
    def on_count(self):
        """Exposes the '计数完成' (Count Complete) execution track as a context manager timeline path."""
        return self.ref.path("计数完成")

NumericVal = Union[float, int, FloatVar, IntVar, PortReference, Any]

class StatManager:
    """
    A high-performance, generalized stat tracking system.
    Handles Global, Tag-based, and Individual stats for both Plants and Zombies.
    """
    def __init__(self, base_plant_stat: float = 0, base_zombie_hp_mult: float = 1):
        # Base values for absolute setters (e.g., modify_attack, modify_health)
        self.base_plant_stat = base_plant_stat
        self.base_zombie_hp_mult = base_zombie_hp_mult
        
        # ==========================================
        # 1. GLOBAL VARIABLES
        # ==========================================
        self.global_atk = FloatVar(name="Global_ATK_Bonus")
        self.global_hp = FloatVar(name="Global_HP_Bonus")
        
        self.global_zombie_hp = FloatVar(name="Global_Zombie_HP_Mult")
        
        # ==========================================
        # 2. TAG STORAGE
        # ==========================================
        self.tags: Dict[str, Dict[str, Any]] = {}
        self.zombie_tags: Dict[str, Dict[str, Any]] = {}
        
        # ==========================================
        # 3. INDIVIDUAL STORAGE (LAZY LOADED)
        # ==========================================
        self.plant_vars: Dict[int, Dict[str, FloatVar]] = {}
        self.zombie_vars: Dict[int, Dict[str, FloatVar]] = {}
        
        # ==========================================
        # 4. COMPUTATION ACCUMULATORS
        # ==========================================
        self._calc_atk = FloatVar(name="Temp_Calc_ATK")
        self._calc_hp = FloatVar(name="Temp_Calc_HP")
        
        self._calc_zombie_hp = FloatVar(name="Temp_Calc_Zombie_HP")

    # =========================================================================
    # PLANT: CATEGORY / TAG MANAGEMENT
    # =========================================================================

    def create_tag(self, tag_name: str, plants: Union[PlantTypeList, Iterable[Union[PlantType, int]]]) -> None:
        if not isinstance(plants, PlantTypeList):
            plants = PlantTypeList(list(plants))
            
        self.tags[tag_name] = {
            "plants": plants,
            "atk": FloatVar(name=f"Tag_{tag_name}_ATK"),
            "hp": FloatVar(name=f"Tag_{tag_name}_HP")
        }

    def add_tag_atk(self, tag_name: str, value: NumericVal) -> None:
        """Adds ATK bonus to a tag. Accepts float, int, FloatVar, or IntVar."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered in MasterStatManager.")
        self.tags[tag_name]["atk"] += value

    def add_tag_hp(self, tag_name: str, value: NumericVal) -> None:
        """Adds HP bonus to a tag. Accepts float, int, FloatVar, or IntVar."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered in MasterStatManager.")
        self.tags[tag_name]["hp"] += value

    # =========================================================================
    # PLANT: INDIVIDUAL MANAGEMENT
    # =========================================================================

    def _lazy_init_plant(self, plant_type: Union[PlantType, int]) -> Dict[str, FloatVar]:
        p_id = int(plant_type.value if hasattr(plant_type, "value") else plant_type) #type: ignore
        if p_id not in self.plant_vars:
            name_str = plant_type.name if hasattr(plant_type, "name") else str(p_id) #type: ignore
            self.plant_vars[p_id] = {
                "atk": FloatVar(name=f"Plant_{name_str}_ATK"),
                "hp": FloatVar(name=f"Plant_{name_str}_HP")
            }
        return self.plant_vars[p_id]

    def add_plant_atk(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds ATK bonus to a specific plant. Accepts float, int, FloatVar, or IntVar."""
        self._lazy_init_plant(plant_type)["atk"] += value

    def add_plant_hp(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds HP bonus to a specific plant. Accepts float, int, FloatVar, or IntVar."""
        self._lazy_init_plant(plant_type)["hp"] += value

    # =========================================================================
    # ZOMBIE: CATEGORY & INDIVIDUAL MANAGEMENT
    # =========================================================================

    def create_zombie_tag(self, tag_name: str, zombies: Union[ZombieTypeList, Iterable[Union[ZombieType, int]]]) -> None:
        if not isinstance(zombies, ZombieTypeList):
            zombies = ZombieTypeList(list(zombies))
            
        self.zombie_tags[tag_name] = {
            "zombies": zombies,
            "hp": FloatVar(name=f"ZTag_{tag_name}_HP")
        }

    def _lazy_init_zombie(self, zombie_type: Union[ZombieType, int]) -> Dict[str, FloatVar]:
        z_id = int(zombie_type.value if hasattr(zombie_type, "value") else zombie_type) #type: ignore
        if z_id not in self.zombie_vars:
            name_str = zombie_type.name if hasattr(zombie_type, "name") else str(z_id) #type: ignore
            self.zombie_vars[z_id] = {
                "hp": FloatVar(name=f"Zombie_{name_str}_HP")
            }
        return self.zombie_vars[z_id]

    def add_zombie_tag_hp(self, tag_name: str, value: NumericVal) -> None:
        """Adds HP multiplier to a zombie tag. Accepts float, int, FloatVar, or IntVar."""
        if tag_name not in self.zombie_tags:
            raise KeyError(f"Zombie tag '{tag_name}' is not registered.")
        self.zombie_tags[tag_name]["hp"] += value

    def add_zombie_hp(self, zombie_type: Union[ZombieType, int], value: NumericVal) -> None:
        """Adds HP multiplier to a specific zombie type. Accepts float, int, FloatVar, or IntVar."""
        self._lazy_init_zombie(zombie_type)["hp"] += value

    # =========================================================================
    # ACCUMULATORS & CALCULATION
    # =========================================================================

    def get_atk_stat(self, plant_ref : Plant) -> FloatVar:
        self._calc_atk.set(self.base_plant_stat + self.global_atk)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_atk += tag_data["atk"]
        for p_id, p_vars in self.plant_vars.items():
            with If(PlantTypeList([p_id]).contains(plant_ref.plantType)):
                self._calc_atk += p_vars["atk"]
        return self._calc_atk

    def get_hp_stat(self, plant_ref : Plant) -> FloatVar:
        self._calc_hp.set(self.base_plant_stat + self.global_hp)
        for tag_data in self.tags.values():
            with If(tag_data["plants"].contains(plant_ref.plantType)):
                self._calc_hp += tag_data["hp"]
        for p_id, p_vars in self.plant_vars.items():
            with If(PlantTypeList([p_id]).contains(plant_ref.plantType)):
                self._calc_hp += p_vars["hp"]
        return self._calc_hp
    
    def get_tag_atk_stat(self, tag_name: str) -> FloatVar:
        """Returns the FloatVar tracking the attack bonus for a given plant tag."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered in MasterStatManager.")
        return self.tags[tag_name]["atk"]

    def get_tag_hp_stat(self, tag_name: str) -> FloatVar:
        """Returns the FloatVar tracking the HP bonus for a given plant tag."""
        if tag_name not in self.tags:
            raise KeyError(f"Tag '{tag_name}' is not registered in MasterStatManager.")
        return self.tags[tag_name]["hp"]
        
    def get_zombie_hp_stat(self, zombie_ref:Zombie) -> FloatVar:
        self._calc_zombie_hp.set(self.base_zombie_hp_mult + self.global_zombie_hp)
        for tag_data in self.zombie_tags.values():
            with If(tag_data["zombies"].contains(zombie_ref.zombieType)):
                self._calc_zombie_hp += tag_data["hp"]
        for z_id, z_vars in self.zombie_vars.items():
            with If(ZombieTypeList([z_id]).contains(zombie_ref.zombieType)):
                self._calc_zombie_hp += z_vars["hp"]
        return self._calc_zombie_hp
    
    def get_zombie_tag_hp_stat(self, tag_name: str) -> FloatVar:
        """Returns the FloatVar tracking the HP multiplier for a given zombie tag."""
        if tag_name not in self.zombie_tags:
            raise KeyError(f"Zombie tag '{tag_name}' is not registered in MasterStatManager.")
        return self.zombie_tags[tag_name]["hp"]

    # =========================================================================
    # CONVENIENCE REFRESHERS
    # =========================================================================

    def apply_stats_to_plant(self, plant_ref : Plant) -> None:
        plant_ref.modify_attack(self.get_atk_stat(plant_ref))
        plant_ref.modify_health(self.get_hp_stat(plant_ref))

    def apply_stats_to_zombie(self, zombie_ref : Zombie) -> None:
        zombie_ref.set_health_multiplier(self.get_zombie_hp_stat(zombie_ref))

    def refresh_all_plants(self) -> None:
        with Lawnf.for_each_plant_on_lawn() as plant:
            self.apply_stats_to_plant(plant)
        