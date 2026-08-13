from . import nodes
from .core import ctx
from .node_base import ExecutionPath
from .extensions import Plant, Zombie, If, Mouse
from enum import Enum
from .TypeMgr import *
from .typing import staticproperty

class Trigger:
    
    class OnGameStart:
        """Triggers just after the Ready, Set, Plant!"""
        
        def __init__(self):
            self.node = nodes.on_game_start()
            
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
            
        def __exit__(self, *args):
            ctx.trigger_stack.pop()
    
    class OnBoardStart:
        """Triggers at first frame of entering the level."""
        def __init__(self): self.node = nodes.on_board_start()
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnWave:
        """Triggers every wave, including non-flag waves. Returns the wave number as an Int."""
        def __init__(self): self.node = nodes.on_wave()
        def __enter__(self) -> int:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self #type: ignore
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnMouseClick:
        """Triggers when the mouse is clicked."""
        def __init__(self): self.node = nodes.on_mouse_click()
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发")) # type: ignore
            return Mouse(self.node)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnKeyDown:
        """Triggers when a specific key is pressed."""
        def __init__(self, key_code : KeyCode):
            if isinstance(key_code, Enum):
                key_code = key_code.value # type: ignore
            self.node = nodes.on_key_press(target_key=key_code)
            
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnPlantCreate:
        """Triggers when a plant is created."""
        def __init__(self): self.node = nodes.on_plant_create()
        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnPlantClicked:
        """Triggers when a plant is clicked."""
        def __init__(self): self.node = nodes.on_plant_click()
        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnPlantDeath:
        """Triggers before a plant dies."""
        def __init__(self): self.node = nodes.on_plant_die()
        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnZombieSpawn:
        """Triggers when a zombie spawns."""
        def __init__(self): self.node = nodes.on_zombie_spawn()
        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnZombieDeath:
        """Triggers when a zombie dies."""
        def __init__(self): self.node = nodes.on_zombie_die()
        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnPlantDeathComplete:
        """Triggers after a plant's death animation completes."""
        def __init__(self): self.node = nodes.on_plant_death_complete()
        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)
        def __exit__(self, *args): ctx.trigger_stack.pop()

class Spawner:
    
    class Set_Plant:
        """
        Spawns a plant at the specified grid coordinates.
        """
        def __init__(self, row, col, plant_type, force=False):
            from . import nodes
            from enum import Enum
            
            if isinstance(plant_type, Enum):
                plant_type = plant_type.value
                
            self.node = nodes.set_plant(
                row=row, 
                column=col, 
                plant_type=nodes.plant_type_value(val=plant_type), 
                force_plant=force
            )
            
            self.ref = Plant(self.node.plant)

        @property
        def on_created(self):
            """Context manager for the '创建成功' (Created Successfully) execution port."""
            from .node_base import ExecutionPath
            return ExecutionPath(self.node.id, "创建成功")

        @property
        def on_failed(self):
            """Context manager for the '创建失败' (Creation Failed) execution port."""
            from .node_base import ExecutionPath
            return ExecutionPath(self.node.id, "创建失败")

    class Set_Zombie:
        """
        Spawns a zombie at the specified grid coordinates.
        """
        def __init__(self, row, col, zombie_type, mind_controlled=False):
            from . import nodes
            from enum import Enum
            
            if isinstance(zombie_type, Enum):
                zombie_type = zombie_type.value
                
            self.node = nodes.create_zombie(
                row=row, 
                column=col, 
                zombie_type=nodes.zombie_type_value(val=zombie_type),
                mind_controlled=mind_controlled
            )
            
            self.ref = Zombie(self.node.zombie)

        @property
        def on_created(self):
            """Context manager for the '创建成功' (Created Successfully) execution port."""
            from .node_base import ExecutionPath
            return ExecutionPath(self.node.id, "创建成功")

class InGameUI:
    @staticmethod
    def display_info_card(big_title, small_title) -> None: 
        from .StdLib import format_string
        nodes.create_info_card(big_title=format_string(big_title), small_title=format_string(small_title))
        
    @staticmethod
    def give_plant_card(plant_type, cooldown=7.5, cost=100, use_default=True) -> None:
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.add_plant_card(p_type=plant_type, cd=cooldown, cost=cost, default_data=use_default)
        
    @staticmethod
    def remove_plant_card(plant_type) -> None: 
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.delete_card_by_type(plant_type=plant_type)
        
    @staticmethod
    def spawn_dropped_card(row, col, plant_type) -> None: 
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.create_plant_card(row=row, column=col, plant_type=plant_type)
    
    @staticmethod
    def display_text(*args, duration=3.0):
        """Pass any mix of text and variables to auto-format and display them on screen."""
        from .StdLib import format_string
        from .extensions import BoolVar, If
        from .nodes import show_text, string_value
        from .node_base import PortReference

        BOOL_NODE_TYPES = {
            "BoolVariableNode", "GetBoolVariableValueNode", "CompareIntNode", 
            "CompareFloatNode", "CompareGameObjectNode", "AndNode", "OrNode", 
            "NotNode", "ToggleNode"
        }

        # 1. Detect if any argument is a dynamic boolean port or BoolVar
        bool_arg = None
        for arg in args:
            if isinstance(arg, BoolVar):
                bool_arg = arg.value
                break
            elif isinstance(arg, PortReference) or hasattr(arg, 'node'):
                node_type = getattr(getattr(arg, 'node', None), 'type', '')
                if node_type in BOOL_NODE_TYPES:
                    bool_arg = arg
                    break

        # 2. If a runtime boolean argument exists, branch execution to show "True" or "False"
        if bool_arg is not None:
            true_args = [
                "True" if (a is bool_arg or (isinstance(a, BoolVar) and a.value is bool_arg)) else a
                for a in args
            ]
            false_args = [
                "False" if (a is bool_arg or (isinstance(a, BoolVar) and a.value is bool_arg)) else a
                for a in args
            ]

            true_text_wire = format_string(*true_args)
            false_text_wire = format_string(*false_args)

            with If(bool_arg):
                show_text(text=true_text_wire, duration=duration)
            with If(~bool_arg): #type: ignore
                show_text(text=false_text_wire, duration=duration)
            return

        # 3. Standard execution path for string and numeric arguments
        final_text = format_string(*args)
        show_text(text=final_text, duration=duration)

class Random:

    class TriggerChance:
        """Fires its contents based on a random probability (e.g. TriggerChance(0.5) is 50%)."""
        def __init__(self, probability):
            rand = Random.randf(0.0, 1.0)
            self.flow = If(rand <= probability)
        def __enter__(self):
            self.flow.__enter__()
            return self
        def __exit__(self, *args):
            self.flow.__exit__(*args)
    
    class RandomTrigger:
        """
        Triggers a random connected event.
        """
        def __init__(self, count=1, allow_repeat=False):
            self.node = nodes.random_trigger(count=count, allow_repeat=allow_repeat)

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()
    
    @staticmethod
    def randint(min_val, max_val) -> Int: return nodes.random_int(min_val=min_val, max_val=max_val).result # type: ignore
    @staticmethod
    def randf(min_val, max_val) -> Float: return nodes.random_float(min_val=min_val, max_val=max_val).result # type: ignore
        
    @staticproperty
    def value():
        return Random.randf(0.0, 1.0)
    
    class Seeded:
        """
        A deterministic, graph-compatible pseudo-random number generator (LCG).
        Uses overflow-safe LCG constants (a=75, c=74, m=65537) to prevent C# 32-bit integer wrapping.
        """
        def __init__(self, seed: int = 12345, name: str = "PRNG_State"):
            from .extensions import IntVar
            # Clamp seed into valid positive range
            safe_seed = (abs(seed) % 65537) or 1
            self.state = IntVar(start_val=safe_seed, name=name)
            
            # Overflow-safe LCG constants: Max math is (75 * 65536 + 74) = 4,915,274 << 2,147,483,647
            self.a = 75
            self.c = 74
            self.m = 65537

        def set_seed(self, seed_value):
            """Manually update or reset the active random seed at runtime."""
            safe_seed = (abs(seed_value) % self.m) or 1
            return self.state.set(safe_seed)

        def _next(self):
            """Advances LCG state. Guaranteed strictly positive without overflow or BranchNodes."""
            next_state = ((self.state * self.a) + self.c) % self.m
            self.state.set(next_state)
            return self.state.value

        def randint(self, min_val: int, max_val: int):
            """Generates a seeded random integer within [min_val, max_val]."""
            range_size = (max_val - min_val) + 1
            raw_val = self._next()
            return min_val + (raw_val % range_size)

        def randf(self, min_val: float = 0.0, max_val: float = 1.0):
            """Generates a seeded random float within [min_val, max_val]."""
            raw_val = self._next()
            normalized = raw_val / float(self.m - 1)
            return min_val + (normalized * (max_val - min_val))

        class TriggerChance:
            """Context manager that fires based on seeded probability (0.0 to 1.0)."""
            def __init__(self, rng: Seeded, probability: float): #type: ignore
                roll = rng.randf(0.0, 1.0)
                self.flow = If(roll <= probability)

            def __enter__(self):
                self.flow.__enter__()
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                self.flow.__exit__(exc_type, exc_val, exc_tb)
    
class _SunManager:
    """Get/Set the board Sun value."""
    @property
    def value(self) -> Int: # type: ignore
        return nodes.get_sun_amount().sunAmount

    def _get_primary_port(self):
        return self.value
    
    class SpendSun:
        """Context Manager for spending sun safely."""
        def __init__(self, amount : Int): self.node = nodes.use_sun(amount=amount) # type: ignore
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self
        def __exit__(self, *args): ctx.trigger_stack.pop()
        
        @property
        def Failed(self) -> ExecutionPath: return ExecutionPath(self.node.id, "阳光不足")

    # 1. Overload Native Math so `Board.Sun + 50` creates a node wire
    def __add__(self, other): return self.value + other
    def __radd__(self, other): return self.value.__radd__(other)
    def __sub__(self, other): return self.value - other
    def __rsub__(self, other): return self.value.__rsub__(other)
    def __mul__(self, other): return self.value * other
    def __rmul__(self, other): return self.value.__rmul__(other)
    def __truediv__(self, other): return self.value / other
    def __rtruediv__(self, other): return self.value.__rtruediv__(other)
    def __floordiv__(self, other): return self.value // other
    def __mod__(self, other): return self.value % other
    
    def __eq__(self, other): return self.value == other
    def __ne__(self, other): return self.value != other
    def __lt__(self, other): return self.value < other
    def __le__(self, other): return self.value <= other
    def __gt__(self, other): return self.value > other
    def __ge__(self, other): return self.value >= other

    def set(self, target_value) -> '_SunManager':
        """Set the Board Sun value."""
        diff = target_value - self.value 
        
        with If(diff > 0) as flow:
            nodes.add_sun(amount=diff)
            
        with flow.Elif(diff < 0):
            abs_diff = diff * -1
            use_node = nodes.use_sun(amount=abs_diff)
            ctx.trigger_stack[-1] = use_node.path("onSuccess")
            
        return self

    def get(self):
        """Get the Board Sun value."""
        return self.value
    
    # 2. Overload In-Place Operators (+=, -=, *=, /=)
    def __iadd__(self, other):
        nodes.add_sun(amount=other)
        return self

    def __isub__(self, other):
        use_node = nodes.use_sun(amount=other)
        ctx.trigger_stack[-1] = use_node.path("onSuccess")
        return self

    def __imul__(self, other):
        self.set(self.value * other)
        return self

    def __itruediv__(self, other):
        self.set(self.value / other)
        return self

    def __ifloordiv__(self, other):
        self.set(self.value // other)
        return self

class _MoneyManager:
    
    @staticmethod
    def check_money(amount, on_true_callback=None, on_false_callback=None) -> None:
        """Checks if the player has enough money by safely spending and refunding it."""
        with nodes.use_money(amount=amount) as node:
            with node.Output.OnSuccess:
                nodes.add_money(amount=amount)
                if on_true_callback: on_true_callback()
                
            with node.Output.OnFailed:
                if on_false_callback: on_false_callback()

    
    class SpendMoney:
        """Context Manager for spending money safely."""
        def __init__(self, amount): self.node = nodes.use_money(amount=amount)
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self
        def __exit__(self, *args): ctx.trigger_stack.pop()
        
        @property
        def Failed(self) -> ExecutionPath: return ExecutionPath(self.node.id, "金币不足")
    
    def __iadd__(self, other):
        nodes.add_money(amount=other)
        return self

    def __isub__(self, other):
        nodes.use_money(amount=other)
        return self

class _BoardMeta(type):
    """Metaclass that exposes properties directly on the Board class."""
    
    @property
    def Sun(cls) -> _SunManager:
        return _SunManager()
        
    @Sun.setter
    def Sun(cls, value):
        if isinstance(value, _SunManager): 
            return
        _SunManager().set(value)
    
    @property
    def Money(cls) -> _MoneyManager:
        return _MoneyManager()

    @property
    def Wave(cls) -> int: 
        return nodes.on_wave().wave #type: ignore

class Board(metaclass=_BoardMeta):
    """Global game state interface"""
    def __new__(cls, *args, **kwargs):
        raise TypeError("Board is a static interface and cannot be instantiated.")

class Lawnf:
    """Contains methods for interacting with the in-game events."""
    
    @staticmethod
    def spawn_particle(row, col): nodes.create_particle(row=row, column=col)
    @staticmethod
    def spawn_grave(row, col): nodes.create_grave(row=row, column=col)
    @staticmethod
    def spawn_crater(row, col): nodes.create_crater(row=row, column=col)
    @staticmethod
    def spawn_ladder(row, col): nodes.create_ladder(row=row, column=col)
    @staticmethod
    def spawn_ice_block(row, col, plant_type=-1): 
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.create_ice_block(row=row, column=col, plant_type=plant_type)

    @staticmethod
    def trigger_cherry_explosion(row, col, damage=1800): nodes.create_cherry_explode(row=row, column=col, damage=damage)
    @staticmethod
    def trigger_doom_explosion(row, col, damage=1800, create_pit=True): nodes.create_doom_shroom_effect(row=row, column=col, damage=damage, set_pit=create_pit)
    @staticmethod
    def trigger_zombie_explosion(row, col): nodes.create_zombie_explode(row=row, column=col)
    @staticmethod
    def trigger_jalapeno(row, damage=1800): nodes.create_jalapeno_effect(row=row, damage=damage)
    @staticmethod
    def trigger_ice_shroom(duration): nodes.create_ice_shroom_effect(duration=duration)
    @staticmethod
    def play_sound(sound_id : SoundType):
        if isinstance(sound_id, Enum):
            sound_id = sound_id.value  # type: ignore 
        nodes.play_sound(sound_id=sound_id)
    
    @staticmethod
    def trigger_game_over(reason="Defeated!"):
        from .StdLib import format_string 
        nodes.game_over(reason=format_string(reason))
    @staticmethod
    def trigger_game_win(): nodes.game_win()
    
    @staticmethod
    def get_buff(buff_enum):
        if isinstance(buff_enum, Enum):
            buff_enum = buff_type.value #type: ignore
        nodes.get_travel_buff(buff_enum=buff_enum)
        
    @staticmethod
    def get_closest_zombie(row, col) -> Zombie:
        """Returns a Zombie Object."""
        n = nodes.get_nearest_zombie(row=row, column=col)
        return Zombie(n.zombie)

    @staticmethod
    def get_plants_at(row, col):
        """Returns the list port for a specific cell, to be used in For_each_plant loops."""
        return nodes.get_plants_in_cell(row=row, column=col).plants
    
    @staticmethod
    def get_all_plants():
        """Returns the list port for all plants on the board, to be used in For_each_plant loops."""
        return nodes.get_all_plants().plants

    class for_each_plant_on_lawn:
        """
        Returns a Plant Object for each plant on the Board.
        """
        def __init__(self):
            self.list_port = nodes.get_all_plants().plants
            self.loop_node = nodes.for_each_plant(plant_list=self.list_port)
            
        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, "循环体"))
            return Plant(self.loop_node.currentPlant)
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

    



