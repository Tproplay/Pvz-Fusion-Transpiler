"""
High-Level Zombie Entity Wrapper for PvZ Fusion Visual Scripts.
"""

from __future__ import annotations
from enum import Enum
from typing import Any, Optional, Union

from ..extension_node import ExtensionNode
from ...Original.Node import Port, to_port
from ...Original.ZombieFunction.damage_zombie_node import DamageZombieNode
from ...Original.ZombieFunction.modify_zombie_health_node import ModifyZombieHealthNode
from ...Original.ZombieFunction.set_zombie_mind_controlled_node import SetZombieMindControlledNode
from ...Original.ZombieFunction.move_zombie_node import MoveZombieNode
from ...Original.ZombieFunction.play_zombie_anim_node import PlayZombieAnimNode
from ...Original.ZombieFunction.zombie_split_node import ZombieSplitNode


class Zombie(ExtensionNode):
    """Smart wrapper around a runtime Zombie entity pointer.
    
    Provides combat actions, mind control overrides, position shifts, animation triggers,
    and destructuring properties.
    """

    def __init__(self, zombie_ref: Any, creator_node: Optional[Any] = None) -> None:
        super().__init__()
        if isinstance(zombie_ref, Zombie):
            self._ref = zombie_ref._ref
            self._creator = zombie_ref._creator
        else:
            self._ref = to_port(zombie_ref)
            self._creator = creator_node

        self._split_cache: Optional[ZombieSplitNode] = None

    @property
    def ref(self) -> Port:
        return self._ref

    def get_primary_port(self) -> Optional[Port]:
        return self._ref

    # =========================================================================
    # ACTIONS & METHODS
    # =========================================================================

    def damage(self, amount: Union[float, int, Port, Any]) -> DamageZombieNode:
        """Deals damage to the zombie."""
        node = DamageZombieNode()
        self.ref.connect(node.get_input("僵尸"))
        to_port(amount).connect(node.get_input("伤害值"))
        self.attach_node(node)
        return node

    def set_health_multiplier(self, ratio: Union[float, int, Port, Any]) -> ModifyZombieHealthNode:
        """Modifies the zombie's health ratio."""
        node = ModifyZombieHealthNode()
        self.ref.connect(node.get_input("僵尸"))
        to_port(ratio).connect(node.get_input("血量倍率"))
        self.attach_node(node)
        return node

    def hypnotize(self) -> SetZombieMindControlledNode:
        """Mind-controls/hypnotizes the zombie."""
        node = SetZombieMindControlledNode()
        self.ref.connect(node.get_input("僵尸"))
        self.attach_node(node)
        return node

    def move(self, row: Any, col: Any) -> MoveZombieNode:
        """Teleports the zombie to specific grid coordinates."""
        node = MoveZombieNode()
        self.ref.connect(node.get_input("僵尸"))
        to_port(col).connect(node.get_input("目标列"))
        to_port(row).connect(node.get_input("目标行"))
        self.attach_node(node)
        return node

    def move_relative(self, row_diff: Any = 0, col_diff: Any = 0) -> MoveZombieNode:
        """Shifts the zombie relative to its current grid position."""
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    def play_animation(self, anim_name: Union[str, Enum, Any] = "idle") -> PlayZombieAnimNode:
        """Plays an animation on the zombie model."""
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        node = PlayZombieAnimNode(animation_name=str(anim_name))
        self.ref.connect(node.get_input("僵尸"))
        self.attach_node(node)
        return node

    # =========================================================================
    # LAZY DESTRUCTURED PROPERTIES
    # =========================================================================

    @property
    def split(self) -> ZombieSplitNode:
        if self._split_cache is None:
            self._split_cache = ZombieSplitNode()
            self.ref.connect(self._split_cache.get_input("僵尸"))
            self.attach_node(self._split_cache)
        return self._split_cache

    @property
    def zombieType(self) -> Port:
        return self.split.get_output("僵尸类型")

    @property
    def row(self) -> Port:
        return self.split.get_output("行")

    @property
    def col(self) -> Port:
        return self.split.get_output("列")

    @property
    def isMindControlled(self) -> Port:
        return self.split.get_output("是否被魅惑")

    # =========================================================================
    # SPAWN OUTCOME PATHS
    # =========================================================================

    @property
    def on_created(self) -> Any:
        if self._creator is not None:
            return self._creator.Output.OnCreated
        from ...Core.context import ExecutionPath
        return ExecutionPath(self.ref.node.node_id, "创建成功")
