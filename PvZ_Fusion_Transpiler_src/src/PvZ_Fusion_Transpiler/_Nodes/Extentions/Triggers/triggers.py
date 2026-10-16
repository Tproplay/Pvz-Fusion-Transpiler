from __future__ import annotations

from enum import Enum
from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from ...._Data.TypeMgr import KeyCode
from ..Input.mouse_ext import Mouse
from ..Entity.plant import Plant
from ..Entity.zombie import Zombie
from .... import nodes


class Trigger:
    """Namespace containing event triggers that initiate visual script execution streams."""

    class OnGameStart:
        """Triggers just after 'Ready, Set, Plant!'."""

        def __init__(self) -> None:
            self.node = nodes.on_game_start()

        def __enter__(self) -> Trigger.OnGameStart:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnBoardStart:
        """Triggers at the very first frame of entering the level."""

        def __init__(self) -> None:
            self.node = nodes.on_board_start()

        def __enter__(self) -> Trigger.OnBoardStart:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnWave:
        """Triggers on every wave. Provides the wave number output port."""

        def __init__(self) -> None:
            self.node = nodes.on_wave()

        def __enter__(self) -> Any:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self.node.wave

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnMouseClick:
        """Triggers when the mouse is clicked. Yields a Mouse helper object."""

        def __init__(self) -> None:
            self.node = nodes.on_mouse_click()

        def __enter__(self) -> Mouse:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Mouse(self.node)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnKeyDown:
        """Triggers when a specific keyboard key is pressed."""

        def __init__(self, key_code: KeyCode | int | Any) -> None:
            if isinstance(key_code, Enum):
                key_code = key_code.value
            self.node = nodes.on_key_press(target_key=key_code)

        def __enter__(self) -> Trigger.OnKeyDown:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnPlantCreate:
        """Triggers when a plant is created. Yields a Plant instance."""

        def __init__(self) -> None:
            self.node = nodes.on_plant_create()

        def __enter__(self) -> Plant:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnPlantClick:
        """Triggers when a plant is clicked. Yields a Plant instance."""

        def __init__(self) -> None:
            self.node = nodes.on_plant_click()

        def __enter__(self) -> Plant:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    OnPlantClicked = OnPlantClick

    class OnPlantDie:
        """Triggers before a plant dies. Yields a Plant instance."""

        def __init__(self) -> None:
            self.node = nodes.on_plant_die()

        def __enter__(self) -> Plant:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    OnPlantDeath = OnPlantDie

    class OnPlantDeathComplete:
        """Triggers after a plant's death animation completes. Yields a Plant instance."""

        def __init__(self) -> None:
            self.node = nodes.on_plant_death_complete()

        def __enter__(self) -> Plant:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Plant(self.node.plant)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnZombieSpawn:
        """Triggers when a zombie spawns. Yields a Zombie instance."""

        def __init__(self) -> None:
            self.node = nodes.on_zombie_spawn()

        def __enter__(self) -> Zombie:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    class OnZombieDie:
        """Triggers when a zombie dies. Yields a Zombie instance."""

        def __init__(self) -> None:
            self.node = nodes.on_zombie_die()

        def __enter__(self) -> Zombie:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return Zombie(self.node.zombie)

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()

    OnZombieDeath = OnZombieDie

    class OnWaveCleared:
        """Triggers when a wave has been completely cleared."""

        def __init__(self) -> None:
            self.node = nodes.on_wave_cleared()

        def __enter__(self) -> Any:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self.node.wave

        def __exit__(self, *args: Any) -> None:
            _ctx.trigger_stack.pop()


__all__ = ["Trigger"]