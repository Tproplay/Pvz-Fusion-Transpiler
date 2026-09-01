from enum import Enum

from . import nodes
from .core import ctx
from .Data.TypeMgr import *
from .Libraries.extensions import If, Mouse, Plant, Zombie, InfoCard
from .node_base import ExecutionPath
from .typing import to_int_port
from typing import Optional, Union, Callable, Any


class Trigger:
    """Namespace containing event triggers that execute node logic in response to game events."""

    class OnGameStart:
        """Triggers immediately after the 'Ready, Set, Plant!' sequence finishes."""

        def __init__(self):
            self.node = nodes.on_game_start()

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnBoardStart:
        """Triggers on the very first frame of entering the level (before countdown / card selection)."""

        def __init__(self):
            self.node = nodes.on_board_start()

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnWave:
        """Triggers whenever a wave spawns, including non-flag waves.

        Returns:
            int: The wave index reference port.

        """

        def __init__(self):
            self.node = nodes.on_wave()

        def __enter__(self) -> int:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self.node.wave  # type: ignore

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnMouseClick:
        """Triggers when the mouse button is pressed.

        Returns:
            Mouse: An accessor object containing cursor coordinate data and button states.
            
        """

        def __init__(self):
            self.node = nodes.on_mouse_click()

        def __enter__(self) -> Mouse:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))  # type: ignore
            return Mouse(self.node)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnKeyDown:
        """Triggers when a specific keyboard key is pressed down.

        Args:
            key_code (KeyCode | Enum | int): Key code or Enum value representing the target key.

        """

        def __init__(self, key_code: KeyCode):
            if isinstance(key_code, Enum):
                key_code = key_code.value  # type: ignore
            self.node = nodes.on_key_press(target_key=key_code)

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnPlantCreate:
        """Triggers when a new plant is placed or created on the board.

        Returns:
            Plant: An accessor object for inspecting or modifying the created plant.
            
        """

        def __init__(self):
            self.node = nodes.on_plant_create()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnPlantClicked:
        """Triggers when a plant is clicked by the player.

        Returns:
            Plant: An accessor object for inspecting or modifying the clicked plant.

        """

        def __init__(self):
            self.node = nodes.on_plant_click()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnPlantDeath:
        """Triggers immediately before a plant dies.

        Note:
            Does not trigger for instantaneous sacrificial plants (such as Cherry Bomb or Doom-shroom).

        Returns:
            Plant: An accessor object for inspecting the dying plant.

        """

        def __init__(self):
            self.node = nodes.on_plant_die()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnZombieSpawn:
        """Triggers whenever a zombie spawns onto the board.

        Returns:
            Zombie: An accessor object for inspecting or modifying the spawned zombie.

        """

        def __init__(self):
            self.node = nodes.on_zombie_spawn()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnZombieDeath:
        """Triggers when a zombie is eliminated.

        Returns:
            Zombie: An accessor object for inspecting the defeated zombie.

        """

        def __init__(self):
            self.node = nodes.on_zombie_die()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

    class OnPlantDeathComplete:
        """Triggers after a plant's death animation has completely finished playing.

        Returns:
            Plant: An accessor object for inspecting the removed plant.

        """

        def __init__(self):
            self.node = nodes.on_plant_death_complete()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args):
            ctx.trigger_stack.pop()
    

class SpawnedPlant(Plant):
    """A `Plant` returned by `Spawner.Set_Plant`, carrying spawn-outcome execution paths."""
    node: Any
    on_created: "ExecutionPath"
    on_failed: "ExecutionPath"


class SpawnedZombie(Zombie):
    """A `Zombie` returned by `Spawner.Set_Zombie`, carrying a spawn-outcome execution path."""
    node: Any
    on_created: "ExecutionPath"


class Spawner:

    @staticmethod
    def Set_Plant(row, col, plant_type, force=False) -> SpawnedPlant:
        """
        Spawns a plant at the specified grid coordinates.

        Returns:
            SpawnedPlant: The spawned plant (a `Plant` subclass). Two extra
                attributes are available for handling the spawn outcome:
                - `.on_created`: ExecutionPath fired if placement succeeded.
                - `.on_failed`: ExecutionPath fired if placement failed.
        """
        from enum import Enum

        from . import nodes
        from .node_base import ExecutionPath

        if isinstance(plant_type, Enum):
            plant_type = plant_type.value

        node = nodes.set_plant(
            row=row,
            column=col,
            plant_type=nodes.plant_type_value(val=plant_type),
            force_plant=force,
        )

        plant = SpawnedPlant(node.plant)
        plant.node = node
        plant.on_created = ExecutionPath(node.id, "创建成功")
        plant.on_failed = ExecutionPath(node.id, "创建失败")
        return plant

    @staticmethod
    def Set_Zombie(row, col, zombie_type, mind_controlled=False) -> SpawnedZombie:
        """
        Spawns a zombie at the specified grid coordinates.

        Returns:
            SpawnedZombie: The spawned zombie (a `Zombie` subclass). One extra
                attribute is available for handling the spawn outcome:
                - `.on_created`: ExecutionPath fired if the zombie was successfully spawned.
        """
        from enum import Enum

        from . import nodes
        from .node_base import ExecutionPath

        if isinstance(zombie_type, Enum):
            zombie_type = zombie_type.value

        node = nodes.create_zombie(
            row=row,
            column=col,
            zombie_type=nodes.zombie_type_value(val=zombie_type),
            mind_controlled=mind_controlled,
        )

        zombie = SpawnedZombie(node.zombie)
        zombie.node = node
        zombie.on_created = ExecutionPath(node.id, "创建成功")
        return zombie


  
class _SunManager:
    """Manages the level's Sun resource with native math and transaction nodes."""

    @property
    def value(self) -> Int:  # type: ignore
        """Primary output port representing the current Sun count."""
        return nodes.get_sun_amount().sunAmount

    def _get_primary_port(self):
        return self.value

    class SpendSun:
        """Context manager for conditional Sun transactions.

        Executes the main body on successful consumption, or routes to `.Failed`
        if Sun is insufficient.

        Example:
            ```python
            with pvn.Board.Sun.SpendSun(50) as spend:
                ...

            with spend.Failed:
                pvn.Print("Not enough Sun!")
            ```
        """

        def __init__(self, amount: Int):  # type: ignore
            self.node = nodes.use_sun(amount=amount)

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient Sun."""
            return ExecutionPath(self.node.id, "阳光不足")

    # Native Math Overloads
    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value.__radd__(other)

    def __sub__(self, other):
        return self.value - other

    def __rsub__(self, other):
        return self.value.__rsub__(other)

    def __mul__(self, other):
        return self.value * other

    def __rmul__(self, other):
        return self.value.__rmul__(other)

    def __truediv__(self, other):
        return self.value / other

    def __rtruediv__(self, other):
        return self.value.__rtruediv__(other)

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    # Comparison Overloads
    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def set(self, target_value) -> "_SunManager":
        """Calculates difference and emits add/use nodes to match the target value."""
        diff = target_value - self.value

        with If(diff > 0) as flow:
            nodes.add_sun(amount=diff)

        with flow.Elif(diff < 0):
            abs_diff = diff * -1
            use_node = nodes.use_sun(amount=abs_diff)
            ctx.trigger_stack[-1] = use_node.path("onSuccess")

        return self

    def get(self):
        """Returns the current Sun port."""
        return self.value

    # In-Place Overloads
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
    """Manages the level's persistent coin balance."""

    @staticmethod
    def check_money(
        amount, on_true_callback=None, on_false_callback=None
    ) -> None:
        """Checks if the player has enough coins by spending and immediately refunding the amount."""
        with nodes.use_money(amount=amount) as node:
            with node.Output.OnSuccess:
                nodes.add_money(amount=amount)
                if on_true_callback:
                    on_true_callback()

            with node.Output.OnFailed:
                if on_false_callback:
                    on_false_callback()

    class SpendMoney:
        """Context manager for conditional coin transactions.

        Executes the main body on successful consumption, or routes to `.Failed`
        if coins are insufficient.

        Example:
        ```python
        with pvn.Board.Money.SpendMoney(100) as purchase:
            pvn.Board.Sun += 200

        with purchase.Failed:
            pvn.Print("Insufficient coins!")
        ```
        """

        def __init__(self, amount):
            self.node = nodes.use_money(amount=amount)

        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self

        def __exit__(self, *args):
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient coins."""
            return ExecutionPath(self.node.id, "金币不足")

    def __iadd__(self, other):
        nodes.add_money(amount=other)
        return self

    def __isub__(self, other):
        nodes.use_money(amount=other)
        return self


class _BoardMeta(type):
    """Metaclass exposing static resource accessors on the Board class."""

    @property
    def Sun(cls) -> _SunManager:
        """Board Sun manager for reading, setting, and checking Sun."""
        return _SunManager()

    @Sun.setter
    def Sun(cls, value):
        if isinstance(value, _SunManager):
            return
        _SunManager().set(value)

    @property
    def Money(cls) -> _MoneyManager:
        """Board Money manager for coin transactions and balance checks."""
        return _MoneyManager()

    @Money.setter
    def Money(cls, value):
        if isinstance(value, _MoneyManager):
            return
        raise NotImplementedError(
            "Direct assignment `Board.Money = X` is not supported by the game engine. "
            "Use `Board.Money += amount` or `Board.Money -= amount` instead."
        )

    @property
    def Wave(cls) -> int:
        """Output port reference to the current wave index."""
        return nodes.on_wave().wave  # type: ignore


class Board(metaclass=_BoardMeta):
    """Global level interface for accessing game resources and board properties."""

    def __new__(cls, *args, **kwargs):
        raise TypeError(
            "Board is a static interface and cannot be instantiated."
        )


class InGameUI:
    """Static helpers for on-screen UI: info cards, seed packet cards, and text popups."""

    @staticmethod
    def display_info_card(
        big_title: Any,
        small_title: Any,
        on_clicked: Optional[Callable[[], None]] = None
    ) -> InfoCard:
        """Displays an in-game Info Card popup.

        This is the callback-driven way to create an info card. For a
        context-manager style (`with InGameUI.InfoCard(...):`), see the
        nested `InGameUI.InfoCard` class below — both drive the same
        underlying node and are interchangeable.

        Args:
            big_title (Any): Main header text, or a text/variable port.
            small_title (Any): Secondary/subtitle text, or a text/variable port.
            on_clicked (Callable[[], None] | None): Logic to run when the player
                clicks the card. Equivalent to using `.on_click()` on the
                returned `InfoCard`.

        Returns:
            InfoCard: The card object. Use `.on_click(func)` to attach logic
                later, or `.Output.OnCardClicked` to access the click execution
                path directly.

        Example:
            ```python
            InGameUI.display_info_card(
                "New Wave!",
                "A horde approaches",
                on_clicked=lambda: pvn.Print("Card dismissed"),
            )
            ```
        """
        return InfoCard(big_title, small_title, callback=on_clicked)

    @staticmethod
    def give_plant_card(plant_type, cooldown=7.5, cost=100, use_default=True) -> None:
        """Adds a seed packet card for the given plant to the player's card selection.

        Args:
            plant_type (PlantType | int): Plant to make available, as a `PlantType`
                enum member or raw integer ID.
            cooldown (float): Recharge time (in seconds) before the card can be
                used again after planting. Defaults to `7.5`.
            cost (int): Sun cost to plant this card. Defaults to `100`.
            use_default (bool): When `True`, uses the plant's official base stats
                for cost/cooldown display instead of the values passed above.
                Defaults to `True`.
        """
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.add_plant_card(p_type=plant_type, cd=cooldown, cost=cost, default_data=use_default)

    @staticmethod
    def remove_plant_card(plant_type) -> None:
        """Removes a plant's seed packet card from the player's card selection.

        Args:
            plant_type (PlantType | int): Plant whose card should be removed, as
                a `PlantType` enum member or raw integer ID.
        """
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.delete_card_by_type(plant_type=plant_type)

    @staticmethod
    def spawn_dropped_card(row, col, plant_type) -> None:
        """Spawns a pickup-able plant card at a board location (e.g. a zombie drop).

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
            plant_type (PlantType | int): Plant the dropped card grants, as a
                `PlantType` enum member or raw integer ID.
        """
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type)
        nodes.create_plant_card(row=row, column=col, plant_type=plant_type)

    @staticmethod
    def display_text(*args, duration=3.0):
        """Formats and displays a mix of text, variables, and node ports on screen.

        Also available as `pvn.Print(...)`.

        If any argument is a boolean expression (`BoolVar` or a comparison/logic
        node port), the message is compiled into two branches — one text string
        rendered if the condition is `True`, another if `False` — so the correct
        wording shows up at runtime without you having to branch manually.

        Args:
            *args: Any mix of strings, numbers, `IntVar`/`FloatVar`/`BoolVar`,
                or raw node output ports. All arguments are concatenated in order.
            duration (float): How long the text stays on screen, in seconds.
                Defaults to `3.0`.

        Example:
            ```python
            pvn.Print("Wave ", wave_num, " incoming!")
            pvn.Print("Hard mode: ", hard_mode)  # hard_mode: BoolVar -> "True"/"False"
            ```
        """
        from .Libraries.extensions import BoolVar, If
        from .Libraries.StdLib import format_string
        from .node_base import PortReference
        from .nodes import show_text

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

    class InfoCard:
        """Context-manager style for displaying an in-game Info Card popup.

        Equivalent to `InGameUI.display_info_card`, but the click-handling logic
        is written as a `with` block instead of a callback function.

        Args:
            big_title (str): Main header text.
            small_title (str): Secondary/subtitle text. Defaults to `""`.

        Example:
            ```python
            with pvn.InGameUI.InfoCard("New Wave!", "A horde approaches"):
                pvn.Print("Card dismissed")
            ```
        """
        def __init__(self, big_title: str, small_title: str = ""):
            from . import nodes

            self.node = nodes.create_info_card(big_title=big_title, small_title=small_title)

        def __enter__(self):
            from .core import ctx
            from .node_base import ExecutionPath
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "点击卡牌时触发"))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            from .core import ctx
            if ctx.trigger_stack:
                ctx.trigger_stack.pop()


class Lawnf:
    """Static helpers for lawn props, area effects, sound, game state, and plant/zombie queries."""

    # ==========================================================
    # PROPS
    # ==========================================================
    @staticmethod
    def spawn_particle(row, col):
        """Spawns a imitator particle effect at the given cell.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
        """
        nodes.create_particle(row=row, column=col)

    @staticmethod
    def spawn_grave(row, col):
        """Spawns a gravestone prop on the given tile.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
        """
        nodes.create_grave(row=row, column=col)

    @staticmethod
    def spawn_crater(row, col):
        """Spawns a crater prop on the given tile (e.g. left behind by an explosion).

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
        """
        nodes.create_crater(row=row, column=col)

    @staticmethod
    def spawn_ladder(row, col):
        """Spawns a pool ladder prop on the given tile, letting zombies climb out of the pool there.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
        """
        nodes.create_ladder(row=row, column=col)

    @staticmethod
    def spawn_ice_block(row, col, plant_type: PlantType | int = -1):
        """Spawns an ice block prop on the given tile.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
            plant_type (PlantType | int): Plant model to encase in the ice block,
                as a `PlantType` enum member or raw integer ID. Defaults to `-1`
                (no plant — a bare ice block).
        """
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        plant_type = nodes.plant_type_value(val=plant_type) # type: ignore
        nodes.create_ice_block(row=row, column=col, plant_type=plant_type)

    # ==========================================================
    # EXPLOSIONS & AREA EFFECTS
    # ==========================================================
    @staticmethod
    def trigger_cherry_explosion(row, col, damage=1800):
        """Triggers a Cherry Bomb-style explosion effect and damage at the given tile.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
            damage (int | Any): Damage dealt to zombies within the blast radius.
                Defaults to `1800`.
        """
        nodes.create_cherry_explode(row=row, column=col, damage=to_int_port(damage))

    @staticmethod
    def trigger_doom_explosion(row, col, damage=1800, create_pit=True):
        """Triggers a Doom-shroom-style explosion effect and damage at the given tile.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
            damage (int | Any): Damage dealt to zombies within the blast radius.
                Defaults to `1800`.
            create_pit (bool): Whether the explosion leaves behind a pit at the
                target tile, matching the classic Doom-shroom crater. Defaults to `True`.
        """
        nodes.create_doom_shroom_effect(row=row, column=col, damage=to_int_port(damage), set_pit=create_pit)

    @staticmethod
    def trigger_zombie_explosion(row, col):
        """Triggers a zombie-explosion visual effect at the given tile (no damage).

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.
        """
        nodes.create_zombie_explode(row=row, column=col)

    @staticmethod
    def trigger_jalapeno(row, damage=1800):
        """Triggers a Jalapeno-style row-wide fire effect and damage.

        Args:
            row (int | Any): Target row to ignite across the entire lawn width.
            damage (int | Any): Damage dealt to zombies in the row. Defaults to `1800`.
        """
        nodes.create_jalapeno_effect(row=row, damage=to_int_port(damage))

    @staticmethod
    def trigger_ice_shroom(duration):
        """Triggers an Ice-shroom-style effect, freezing all zombies on the board.

        Args:
            duration (float | Any): How long the freeze lasts, in seconds.
        """
        nodes.create_ice_shroom_effect(duration=duration)

    # ==========================================================
    # SOUND
    # ==========================================================
    @staticmethod
    def play_sound(sound_id: SoundType):
        """Plays a one-shot sound effect.

        Args:
            sound_id (SoundType | int): Sound to play, as a `SoundType` enum
                member (from `PvzRH_node.Types`) or raw integer ID.
        """
        if isinstance(sound_id, Enum):
            sound_id = sound_id.value  # type: ignore
        nodes.play_sound(sound_id=sound_id)

    # ==========================================================
    # GAME STATE
    # ==========================================================
    @staticmethod
    def trigger_game_over(reason="Defeated!"):
        """Ends the level in defeat, displaying the given reason text.

        Args:
            reason (Any): Text (or a mix of text/variables) shown on the
                game-over screen. Defaults to `"Defeated!"`.
        """
        from .Libraries.StdLib import format_string
        nodes.game_over(reason=format_string(reason))

    @staticmethod
    def trigger_game_win():
        """Ends the level in victory."""
        nodes.game_win()

    # ==========================================================
    # BUFFS
    # ==========================================================
    @staticmethod
    def get_buff(buff_enum):
        """Grants a travel buff for the current level.

        Args:
            buff_enum (TravelBuffType | int): Buff to grant, as a `TravelBuffType`
                enum member (from `PvzRH_node.Types`) or raw integer ID.
        """
        if isinstance(buff_enum, Enum):
            buff_enum = buff_enum.value
        nodes.get_travel_buff(buff_enum=buff_enum)

    # ==========================================================
    # QUERIES & LOOPS
    # ==========================================================
    @staticmethod
    def get_closest_zombie(row, col) -> "Zombie":
        """Finds the zombie nearest to the given tile.

        Args:
            row (int | Any): Row to search from.
            col (int | Any): Column to search from.

        Returns:
            Zombie: An accessor object for the nearest zombie found.
        """
        n = nodes.get_nearest_zombie(row=row, column=col)
        return Zombie(n.zombie)

    @staticmethod
    def get_plants_at(row, col):
        """Returns the plant-list output port for a specific cell.

        Intended for use as the input to a `Lawnf.for_each_plant_on_lawn`-style
        loop or other list-consuming node — this itself is not a loop.

        Args:
            row (int | Any): Target row on the lawn grid.
            col (int | Any): Target column on the lawn grid.

        Returns:
            Any: The plant-list output port for the given cell.
        """
        return nodes.get_plants_in_cell(row=row, column=col).plants

    @staticmethod
    def get_all_plants():
        """Returns the plant-list output port for every plant on the board.

        Returns:
            Any: The plant-list output port for all plants currently on the lawn.
        """
        return nodes.get_all_plants().plants

    class for_each_plant_on_lawn:
        """Context manager that loops over every plant currently on the board.

        Example:
        ```python
        with pvn.Lawnf.for_each_plant_on_lawn() as plant:
            plant.heal(50)
        ```
        """
        def __init__(self):
            self.list_port = nodes.get_all_plants().plants
            self.loop_node = nodes.for_each_plant(plant_list=self.list_port)

        def __enter__(self) -> "Plant":
            ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, "循环体"))
            return Plant(self.loop_node.currentPlant)

        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

    
Print = InGameUI.display_text


