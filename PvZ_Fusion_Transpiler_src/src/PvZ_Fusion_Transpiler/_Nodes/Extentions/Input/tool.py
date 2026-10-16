from __future__ import annotations

from typing import Any, NamedTuple
from enum import Enum
from .... import nodes
from ...._Data.ToolType import ToolType


class ToolCooldown(NamedTuple):
    total_seconds: Any
    remaining_seconds: Any
    exists: Any


class Tool:
    """Namespace for querying and controlling player mouse tools and cooldowns."""

    @staticmethod
    def get_held() -> tuple[Any, Any]:
        """Returns (GameObject, ToolType) for the tool currently held by the player."""
        n = nodes.get_held_tool()
        return (n.port_output_gameobject_GameObject, n.port_output_tooltype_ToolType)

    @staticmethod
    def is_held(tool_type: ToolType | Any) -> Any:
        """Returns a bool port indicating whether the given tool type is currently held."""
        held = nodes.get_held_tool()
        cmp_node = nodes.compare_tool_type(a=held.port_output_tooltype_ToolType, b=tool_type)
        return cmp_node.port_output_bool_Equal

    @staticmethod
    def get_cooldown(tool_type: ToolType | Any) -> ToolCooldown:
        """Returns cooldown information (total, remaining, exists) for the tool type."""
        cd_node = nodes.get_tool_cooldown(tool_type=tool_type)
        return ToolCooldown(
            total_seconds=cd_node.port_output_float_TotalSeconds,
            remaining_seconds=cd_node.port_output_float_RemainingSeconds,
            exists=cd_node.port_output_bool_Exists,
        )

    @staticmethod
    def set_cooldown(tool_type: ToolType | Any, ratio: Any) -> Any:
        """Sets the cooldown ratio for the specified tool type."""
        return nodes.set_tool_cooldown(tool_type=tool_type, ratio=ratio)


__all__ = ["Tool", "ToolCooldown"]
