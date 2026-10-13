"""
PvZ Fusion Event Triggers Subsystem.
Defines lifecycle, input, and entity event triggers that hook into the game engine execution graph.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Union

from .. import nodes
from ..Core.context import ctx, ExecutionPath
from ..Nodes.Extentions.extensions import Mouse, Plant, Zombie
from ..Extras.TypeMgr import KeyCode


class Trigger:
    """Namespace containing event triggers that execute node logic in response to game events."""

    class OnGameStart:
        """Triggers immediately after the 'Ready, Set, Plant!' sequence finishes."""

        def __init__(self) -> None:
            self.node = nodes.on_game_start()

        def __enter__(self) -> "Trigger.OnGameStart":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnBoardStart:
        """Triggers on the very first frame of entering the level (before countdown / card selection)."""

        def __init__(self) -> None:
            self.node = nodes.on_board_start()

        def __enter__(self) -> "Trigger.OnBoardStart":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnWave:
        """Triggers whenever a wave spawns, including non-flag waves.

        Returns:
            int: The wave index reference port.
        """

        def __init__(self) -> None:
            self.node = nodes.on_wave()

        def __enter__(self) -> Any:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self.node.wave

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnMouseClick:
        """Triggers when the mouse button is pressed.

        Returns:
            Mouse: An accessor object containing cursor coordinate data and button states.
        """

        def __init__(self) -> None:
            self.node = nodes.on_mouse_click()

        def __enter__(self) -> Mouse:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Mouse(self.node)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnKeyDown:
        """Triggers when a specific keyboard key is pressed down.

        Args:
            key_code (KeyCode | Enum | int): Key code or Enum value representing the target key.
        """

        def __init__(self, key_code: Union[KeyCode, Enum, int]) -> None:
            if isinstance(key_code, Enum):
                key_code = key_code.value
            self.node = nodes.on_key_press(target_key=key_code)

        def __enter__(self) -> "Trigger.OnKeyDown":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnPlantCreate:
        """Triggers when a new plant is placed or created on the board.

        Returns:
            Plant: An accessor object for inspecting or modifying the created plant.
        """

        def __init__(self) -> None:
            self.node = nodes.on_plant_create()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnPlantClicked:
        """Triggers when a plant is clicked by the player.

        Returns:
            Plant: An accessor object for inspecting or modifying the clicked plant.
        """

        def __init__(self) -> None:
            self.node = nodes.on_plant_click()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnPlantDeath:
        """Triggers immediately before a plant dies.

        Note:
            Does not trigger for instantaneous sacrificial plants (such as Cherry Bomb or Doom-shroom).

        Returns:
            Plant: An accessor object for inspecting the dying plant.
        """

        def __init__(self) -> None:
            self.node = nodes.on_plant_die()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnZombieSpawn:
        """Triggers whenever a zombie spawns onto the board.

        Returns:
            Zombie: An accessor object for inspecting or modifying the spawned zombie.
        """

        def __init__(self) -> None:
            self.node = nodes.on_zombie_spawn()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnZombieDeath:
        """Triggers when a zombie is eliminated.

        Returns:
            Zombie: An accessor object for inspecting the defeated zombie.
        """

        def __init__(self) -> None:
            self.node = nodes.on_zombie_die()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnPlantDeathComplete:
        """Triggers after a plant's death animation has completely finished playing.

        Returns:
            Plant: An accessor object for inspecting the removed plant.
        """

        def __init__(self) -> None:
            self.node = nodes.on_plant_death_complete()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()
