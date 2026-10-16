from __future__ import annotations

from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from .plant import Plant


class ForEachPlant:
    """Context manager that loops through a collection of Plant entities on the node canvas.

    Acts as a transparent proxy to the current `Plant` object, allowing direct calls to
    plant methods (e.g., `loop.die()`, `loop.heal()`) without explicitly accessing `.plant`.

    Example:
        ```python
        with ForEachPlant(target_plants) as plant:
            plant.heal(50)

        with plant.on_complete:
            ...
        ```
    """

    def __init__(self, plant_list_port: Any) -> None:
        if hasattr(plant_list_port, "list_port"):
            plant_list_port = plant_list_port.list_port
        elif hasattr(plant_list_port, "value"):
            plant_list_port = plant_list_port.value

        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        self._plant_cache: Optional[Plant] = None

    def __enter__(self) -> ForEachPlant:
        _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_LoopBody))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.trigger_stack.pop()

    @property
    def on_complete(self) -> ExecutionPath:
        return ExecutionPath(self.node.port_output_trigger_LoopComplete)

    @property
    def plant(self) -> Plant:
        if self._plant_cache is None:
            self._plant_cache = Plant(self.node.port_output_plant_CurrentPlant)
        return self._plant_cache

    @property
    def index(self) -> Any:
        return self.node.port_output_int_CurrentIndex

    def __getattr__(self, name: str) -> Any:
        return getattr(self.plant, name)


class ForEachPlantType:
    """Context manager that safely loops through a list of Plant Types natively on the canvas.

    Example:
        ```python
        with ForEachPlantType(allowed_plants) as loop:
            ...
        ```
    """

    def __init__(self, type_list_port: Any) -> None:
        if hasattr(type_list_port, "list_port"):
            type_list_port = type_list_port.list_port
        elif hasattr(type_list_port, "value"):
            type_list_port = type_list_port.value

        self.node = nodes.for_each_plant_type(type_list=type_list_port)

    def __enter__(self) -> ForEachPlantType:
        _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_LoopBody))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.trigger_stack.pop()

    @property
    def on_complete(self) -> ExecutionPath:
        return ExecutionPath(self.node.port_output_trigger_LoopComplete)

    @property
    def plant_type(self) -> Any:
        return getattr(self.node, "port_output_planttype_CurrentType", getattr(self.node, "port_output_planttype_CurrentPlantType", None))

    type = plant_type
    value = plant_type

    @property
    def index(self) -> Any:
        return self.node.port_output_int_CurrentIndex

    def _get_primary_port(self) -> Any:
        return self.plant_type

    def __eq__(self, other: Any) -> Any:
        return self.plant_type == other

    def __ne__(self, other: Any) -> Any:
        return self.plant_type != other


__all__ = ["ForEachPlant", "ForEachPlantType"]
