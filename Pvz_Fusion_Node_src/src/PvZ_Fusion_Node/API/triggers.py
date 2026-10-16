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
from ..Nodes.Original.Node import Port
from ..Extras.TypeMgr import KeyCode


class Trigger:
    """Namespace containing event triggers that execute node logic in response to game events."""

    class OnGameStart:
        """Triggers immediately after the 'Ready, Set, Plant!' sequence finishes."""

        def __init__(self) -> None:
            self.node = nodes.on_game_start()

        def __enter__(self) -> "Trigger.OnGameStart":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnBoardStart:
        """Triggers on the very first frame of entering the level (before countdown / card selection)."""

        def __init__(self) -> None:
            self.node = nodes.on_board_start()

        def __enter__(self) -> "Trigger.OnBoardStart":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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

        def __enter__(self) -> Port:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnPlantMixed:
        """Triggers when a plant is mixed (fused).

        Returns:
            Plant: An accessor object for inspecting the mixed plant.
        """

        def __init__(self) -> None:
            self.node = nodes.OnPlantMixedNode()

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnWaveCleared:
        """Triggers when all zombies in a wave are cleared.

        Returns:
            Port: The wave index reference port.
        """

        def __init__(self) -> None:
            self.node = nodes.OnWaveClearedNode()

        def __enter__(self) -> Port:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return self.node.wave

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnWorldPlantEffect:
        """Triggers on full-screen / world plant effects (e.g. Doom-shroom, Ice-shroom).

        Args:
            effect (int): The target effect identifier.

        Returns:
            Plant: An accessor object for inspecting the effect-triggering plant.
        """

        def __init__(self, effect: int = 0) -> None:
            self.node = nodes.OnWorldPlantEffectNode(effect=effect)

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnZombieClick:
        """Triggers when a zombie is clicked by the player.

        Returns:
            Zombie: An accessor object for inspecting or modifying the clicked zombie.
        """

        def __init__(self) -> None:
            self.node = nodes.OnZombieClickNode()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnZombieHealthBelow:
        """Triggers when a zombie's health drops below a specified threshold.

        Returns:
            Zombie: An accessor object for inspecting the zombie.
        """

        def __init__(self) -> None:
            self.node = nodes.OnZombieHealthBelowNode()

        def __enter__(self) -> Zombie:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class WaveEvent:
        """Triggers when a specific wave spawns.

        Args:
            wave (int): The target wave number.

        Returns:
            Port: The wave index reference port.
        """

        def __init__(self, wave: int = 0) -> None:
            self.node = nodes.WaveEventNode(wave_value=wave)

        def __enter__(self) -> Port:
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return self.node.wave

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

    class OnStageEnter:
        """Triggers when entering a specific game stage.

        Args:
            stage_name (str): Name of the stage (e.g. '战斗', '准备').
        """

        def __init__(self, stage_name: str = "战斗") -> None:
            self.node = nodes.OnStageEnterNode(stage_name=stage_name)

        def __enter__(self) -> "Trigger.OnStageEnter":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, self.node.Trigger_output_trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()
