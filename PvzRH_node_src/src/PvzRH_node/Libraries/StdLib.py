from __future__ import annotations

from typing import Any, Dict, Iterable, Union
from enum import Enum

from ..Data.TypeMgr import KeyCode
from .extensions import *
from ..node_base import PortReference
from ..api import *


def format_string(*args):
    """Dynamically chains text, variables, node ports, and constants into a single string port.

    Evaluates various input types (booleans, enums, objects with `to_string()`) and 
    generates a physical string concatenation chain on the visual node canvas.

    Args:
        *args: Variable number of arguments to concatenate.

    Returns:
        PortReference: The output port of the final StringConcat node.

    Example:
        ```python
        msg = pvn.StdLib.format_string("Wave ", wave_num, " has arrived!")
        pvn.Print(msg)
        ```
    """
    if not args:
        from ..nodes import string_value

        return string_value(val="").value

    from ..node_base import PortReference
    from ..nodes import string_concat, string_value

    def _parse_arg(arg):
        if hasattr(arg, "to_string") and callable(arg.to_string):
            return arg.to_string()

        if isinstance(arg, PortReference):
            return arg._to_string_port()

        if hasattr(arg, "node"):
            from ..node_base import PortReference as PR

            port_name = getattr(arg, "port_name", getattr(arg, "out_port", "Output"))
            return PR(arg.node, port_name)._to_string_port()

        if isinstance(arg, bool):
            return string_value(val="True" if arg else "False").value

        if isinstance(arg, Enum):
            return string_value(val=arg.name).value

        return string_value(val=str(arg)).value

    current_chain = _parse_arg(args[0])

    if len(args) == 1:
        return current_chain

    for i in range(1, len(args)):
        next_piece = _parse_arg(args[i])
        current_chain = string_concat(a=current_chain, b=next_piece).result

    return current_chain


class ZombieTypeList:
    """A static wrapper representing a list of Zombie Types.

    Since native zombie list storage nodes are unavailable, this manages a Python-side 
    set and dynamically generates an OR-chained comparison graph at transpilation time.

    Example:
    ```python
    bosses = pvn.StdLib.ZombieTypeList([ZombieType.Gargantuar, ZombieType.BungeeZombie])
    
    with pvn.Trigger.OnZombieSpawn() as zombie:
        with pvn.If(bosses.contains(zombie.zombieType)):
            pvn.Print("A boss has appeared!")
    ```
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

    def add(self, item: Any) -> ZombieTypeList:
        """Adds a zombie type or collection of types to the static list."""
        if isinstance(item, (list, tuple, set)) and not isinstance(item, PortReference):
            for i in item:
                self.add(i)
        elif isinstance(item, ZombieTypeList):
            self._items.update(item._items)
        else:
            self._items.add(self._extract_id(item))
        return self

    def remove(self, item: Any) -> ZombieTypeList:
        """Removes a zombie type or collection of types from the static list."""
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

    def contains(self, target_type: PortReference | Enum | int | Any) -> PortReference:
        """Builds a runtime node graph to check if target_type is in this static list.
        
        Generates a sequence of compare_zombie_type nodes chained with logical OR (`|`).
        """
        if not self._items:
            return nodes.bool_value(val=False).value #type: ignore

        if not isinstance(target_type, PortReference) and not hasattr(target_type, "node"):
            target_id = self._extract_id(target_type)
            return nodes.bool_value(val=(target_id in self._items)).value #type: ignore

        result_wire = None
        for z_id in self._items:
            z_node = nodes.zombie_type_value(val=z_id)
            z_port = z_node.value if hasattr(z_node, "value") else z_node
            compare_node = nodes.compare_zombie_type(a=target_type, b=z_port)
            is_equal = compare_node.equal

            if result_wire is None:
                result_wire = is_equal
            else:
                result_wire = result_wire | is_equal

        return result_wire #type: ignore


class _wasd_key:
    """Internal struct for default WASD KeyCode bindings."""
    def __init__(self):
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D


class WASDPlant:
    """Assigns WASD keyboard inputs to control the grid movement of a specific Plant entity.

    Example:
    ```python
    with pvn.Trigger.OnGameStart():
        hero = pvn.Spawner.Set_Plant(row=2, col=2, plant_type=pvn.PlantType.Peashooter)
        pvn.StdLib.WASDPlant(hero).Start()
    ```
    """

    def __init__(self, plant: Plant | Any):
        if isinstance(plant, Plant):
            self.plant = plant
        else:
            self.plant = Plant(plant)

        self.wasd_keys = _wasd_key()

    def Start(self):
        """Initializes the keyboard triggers and movement bindings."""
        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(0, -1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(0, 1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(-1, 0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(1, 0)


class Dictionary:
    """A Virtual Dictionary utilizing persistent Native Variables.

    Allows you to define a string-keyed dictionary schema that transpiles into individual
    Int, Float, and Bool variable nodes on the visual canvas.

    Example:
    ```python
    player_stats = pvn.StdLib.Dictionary({
        "kills": 0,
        "speed": 1.5,
        "is_poisoned": False
    })
    
    with pvn.Trigger.OnZombieDeath():
        player_stats.kills += 1
    ```
    """

    def __init__(self, schema: dict | None = None):  # type: ignore
        self._store = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val):  # type: ignore
        """Registers a new variable under the specified key."""
        if key in self._store:
            raise KeyError(f"Key '{key}' already exists!")

        if isinstance(initial_val, bool):
            self._store[key] = BoolVar(start_val=initial_val, name=f"dict_{key}")
        elif isinstance(initial_val, float):
            self._store[key] = FloatVar(start_val=initial_val, name=f"dict_{key}")
        elif isinstance(initial_val, int):
            self._store[key] = IntVar(start_val=initial_val, name=f"dict_{key}")
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
    """A Pre-Allocated Virtual Array utilizing persistent Native Variables.

    Transpiles a contiguous block of identically typed variable nodes that can be read 
    or written to via index ports at runtime.

    Example:
    ```python
    lane_health = pvn.StdLib.Array(size=5, default_val=100)
    
    with pvn.Trigger.OnZombieSpawn() as zombie:
        lane_health.write(zombie.row, 50)
    ```
    """

    def __init__(self, size: int, default_val=0):
        self.size = size
        self._store = []

        for i in range(size):
            if isinstance(default_val, bool):
                self._store.append(BoolVar(start_val=default_val, name=f"arr_{i}"))
            elif isinstance(default_val, float):
                self._store.append(FloatVar(start_val=default_val, name=f"arr_{i}"))
            elif isinstance(default_val, int):
                self._store.append(IntVar(start_val=default_val, name=f"arr_{i}"))

    def __getitem__(self, index: int):
        return self._store[index]

    def __setitem__(self, index: int, value):
        self._store[index].set(value)

    def __len__(self):
        return self.size

    def read(self, index_port, on_read_callback):
        """Reads a value from the array dynamically using a node port index.

        Args:
            index_port (Any): The numeric port specifying which array index to read.
            on_read_callback (Callable): Function that receives the retrieved variable.
        """
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])

    def write(self, index_port, value):
        """Writes a value to the array dynamically using a node port index.

        Args:
            index_port (Any): The numeric port specifying which array index to write to.
            value (Any): The value to store.
        """
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)


class Counter:
    """A high-level wrapper for the Engine's native CounterNode.

    Tracks an integer count and fires its `on_count` completion path when a target is reached,
    acting as an objective tracker or multi-hit trigger.

    Example:
    ```python
    zombie_counter = pvn.StdLib.Counter(start_val=0)

    with pvn.Trigger.OnZombieDeath():
        zombie_counter.up()
        
    with zombie_counter.on_count:
        pvn.Print("Objective complete!")
        ```
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
        """Exposes the 'Count Complete' execution track as a context manager timeline path."""
        return self.ref.path("计数完成")


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
    def __init__(self, base_plant_stat: float = 0, base_zombie_hp_mult: float = 1):
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

    def create_tag(self, tag_name: str, plants: Union[PlantTypeList, Iterable[Union[PlantType, int]]]) -> None:
        """Registers a category of plants that can receive shared stat buffs."""
        if not isinstance(plants, PlantTypeList):
            plants = PlantTypeList(list(plants))
            
        self.tags[tag_name] = {
            "plants": plants,
            "atk": FloatVar(name=f"Tag_{tag_name}_ATK"),
            "hp": FloatVar(name=f"Tag_{tag_name}_HP")
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
        p_id = int(plant_type.value if hasattr(plant_type, "value") else plant_type) #type: ignore
        if p_id not in self.plant_vars:
            name_str = plant_type.name if hasattr(plant_type, "name") else str(p_id) #type: ignore
            self.plant_vars[p_id] = {
                "atk": FloatVar(name=f"Plant_{name_str}_ATK"),
                "hp": FloatVar(name=f"Plant_{name_str}_HP")
            }
        return self.plant_vars[p_id]

    def add_plant_atk(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds an attack bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["atk"] += value

    def add_plant_hp(self, plant_type: Union[PlantType, int], value: NumericVal) -> None:
        """Adds a health bonus to a single specific plant type."""
        self._lazy_init_plant(plant_type)["hp"] += value

    def create_zombie_tag(self, tag_name: str, zombies: Union[ZombieTypeList, Iterable[Union[ZombieType, int]]]) -> None:
        """Registers a category of zombies that can receive shared health modifiers."""
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