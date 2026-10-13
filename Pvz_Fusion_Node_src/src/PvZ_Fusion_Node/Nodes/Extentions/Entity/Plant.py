"""
High-Level Plant Entity Wrapper for PvZ Fusion Visual Scripts.
"""

from __future__ import annotations
from typing import Any, Optional, Union

from ..extension_node import ExtensionNode
from ...Original.Node import Port, to_port
from ...Original.PlantFunction.die_plant_node import DiePlantNode
from ...Original.PlantFunction.damage_plant_node import DamagePlantNode
from ...Original.PlantFunction.heal_plant_node import HealPlantNode
from ...Original.PlantFunction.give_plant_shield_node import GivePlantShieldNode
from ...Original.PlantFunction.move_plant_node import MovePlantNode
from ...Original.PlantFunction.modify_plant_attack_node import ModifyPlantAttackNode
from ...Original.PlantFunction.modify_plant_health_node import ModifyPlantHealthNode
from ...Original.PlantFunction.plant_split_node import PlantSplitNode


class Plant(ExtensionNode):
    """Smart wrapper around a runtime Plant entity pointer.
    
    Provides high-level actions, stat modifications, grid movement, and lazy-loaded
    properties via destructuring nodes.
    """

    def __init__(self, plant_ref: Any, creator_node: Optional[Any] = None) -> None:
        super().__init__()
        if isinstance(plant_ref, Plant):
            self._ref = plant_ref._ref
            self._creator = plant_ref._creator
        else:
            self._ref = to_port(plant_ref)
            self._creator = creator_node

        self._split_cache: Optional[PlantSplitNode] = None

    @property
    def ref(self) -> Port:
        return self._ref

    def get_primary_port(self) -> Optional[Port]:
        return self._ref

    # =========================================================================
    # ACTIONS & METHODS
    # =========================================================================

    def die(self) -> DiePlantNode:
        """Instantly kills and removes the plant from the lawn."""
        node = DiePlantNode()
        self.ref.connect(node.get_input("植物"))
        self.attach_node(node)
        return node

    def damage(self, amount: Union[float, int, Port, Any]) -> DamagePlantNode:
        """Inflicts damage on the plant."""
        node = DamagePlantNode()
        self.ref.connect(node.get_input("植物"))
        to_port(amount).connect(node.get_input("伤害值"))
        self.attach_node(node)
        return node

    def heal(self, amount: Union[float, int, Port, Any]) -> HealPlantNode:
        """Restores health to the plant."""
        node = HealPlantNode()
        self.ref.connect(node.get_input("植物"))
        to_port(amount).connect(node.get_input("回血量"))
        self.attach_node(node)
        return node

    def add_shield(self, amount: Union[float, int, Port, Any]) -> GivePlantShieldNode:
        """Grants protective shield to the plant."""
        node = GivePlantShieldNode()
        self.ref.connect(node.get_input("植物"))
        to_port(amount).connect(node.get_input("护盾值"))
        self.attach_node(node)
        return node

    def move(self, col: Any, row: Any, force: bool = False) -> MovePlantNode:
        """Teleports the plant to absolute lawn grid coordinates."""
        node = MovePlantNode()
        self.ref.connect(node.get_input("植物"))
        to_port(col).connect(node.get_input("列"))
        to_port(row).connect(node.get_input("行"))
        to_port(force).connect(node.get_input("强制"))
        self.attach_node(node)
        return node

    def move_relative(self, col_diff: Any, row_diff: Any, force: bool = False) -> MovePlantNode:
        """Moves the plant relative to its current board tile position."""
        return self.move(col=self.col + col_diff, row=self.row + row_diff, force=force)

    def modify_attack(self, multiplier: Union[float, int, Port, Any]) -> ModifyPlantAttackNode:
        """Scales the plant's attack power."""
        node = ModifyPlantAttackNode()
        self.ref.connect(node.get_input("植物"))
        to_port(multiplier).connect(node.get_input("攻击力加成x100%"))
        self.attach_node(node)
        return node

    def modify_health(self, multiplier: Union[float, int, Port, Any]) -> ModifyPlantHealthNode:
        """Scales the plant's health."""
        node = ModifyPlantHealthNode()
        self.ref.connect(node.get_input("植物"))
        to_port(multiplier).connect(node.get_input("血量加成x100%"))
        self.attach_node(node)
        return node

    # =========================================================================
    # LAZY DESTRUCTURED PROPERTIES
    # =========================================================================

    @property
    def _split(self) -> PlantSplitNode:
        if self._split_cache is None:
            self._split_cache = PlantSplitNode()
            self.ref.connect(self._split_cache.get_input("植物"))
            self.attach_node(self._split_cache)
        return self._split_cache

    @property
    def plantType(self) -> Port:
        return self._split.get_output("植物类型")

    @property
    def row(self) -> Port:
        return self._split.get_output("行")

    @property
    def col(self) -> Port:
        return self._split.get_output("列")

    @property
    def health(self) -> Port:
        return self._split.get_output("植物血量")

    @property
    def attributeCD(self) -> Port:
        return self._split.get_output("属性倒计时")

    # =========================================================================
    # SPAWN OUTCOME PATHS
    # =========================================================================

    @property
    def on_created(self) -> Any:
        if self._creator is not None:
            return self._creator.Output.OnCreated
        from ...Core.context import ExecutionPath
        return ExecutionPath(self.ref.node.node_id, "创建成功")

    @property
    def on_failed(self) -> Any:
        if self._creator is not None:
            return self._creator.Output.OnCreateFailed
        from ...Core.context import ExecutionPath
        return ExecutionPath(self.ref.node.node_id, "创建失败")