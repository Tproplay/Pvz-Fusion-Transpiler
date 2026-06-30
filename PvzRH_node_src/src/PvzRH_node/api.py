from . import nodes
from .core import ctx
from .node_base import ExecutionPath, PortReference
from .extensions import Plant, Zombie, If
from .functions import format_string

from enum import Enum
from .TypeMgr import *


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
        """Triggers every wave, including non-flag waves."""
        def __init__(self, wave_num): self.node = nodes.on_wave(wave_val=wave_num)
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
        def __exit__(self, *args): ctx.trigger_stack.pop()

    class OnMouseClick:
        """Triggers when the mouse (left button) is clicked."""
        def __init__(self): self.node = nodes.on_mouse_click()
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发")) # type: ignore
            return self.node
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

class GameAPP:
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
    def display_text(*args, duration=3.0):
        """Pass any mix of text and variables, and it will auto-format and display them!"""
        final_text = format_string(*args)
        nodes.show_text(text=final_text, duration=duration)

    
    @staticmethod
    def trigger_game_over(reason="Defeated!"): nodes.game_over(reason=format_string(reason))
    @staticmethod
    def trigger_game_win(): nodes.game_win()

class InGameUI:
    @staticmethod
    def display_info_card(big_title, small_title) -> None: 
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

class Mouse:
    @staticmethod
    def col():
        return nodes.on_mouse_click().column
    @staticmethod
    def row():
        return nodes.on_mouse_click().row
    @staticmethod
    def theItemType():
        return nodes.on_mouse_click().item

class Repeat:
    """A visual 'For Loop' Context Manager."""
    def __init__(self, count): self.node = nodes.for_loop_node(count=count)
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self.node.index
    def __exit__(self, *args): ctx.trigger_stack.pop()

class Random:
    
    @staticmethod
    def randint(min_val, max_val) -> Int: return nodes.random_int(min_val=min_val, max_val=max_val).result # type: ignore
    @staticmethod
    def randf(min_val, max_val) -> Float: return nodes.random_float(min_val=min_val, max_val=max_val).result # type: ignore
    
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

class _BoardState:
    """Global singleton exposing high-level game state proxies."""
    @property
    def Sun(self) -> _SunManager:
        return _SunManager()
        
    @Sun.setter
    def Sun(self, value):
        # Ignore self-assignment triggered by Python's native += operator
        if isinstance(value, _SunManager): return
        _SunManager().set(value)
    
    @property
    def Money(self) -> _MoneyManager:
        return _MoneyManager()

    @property
    def Wave(self) -> Int: # type: ignore
        return nodes.on_wave().wave

Board = _BoardState()

class Lawnf:
    
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

    class all_plants:
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

    
