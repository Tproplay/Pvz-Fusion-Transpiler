from __future__ import annotations
from typing import Any, Iterable, Optional, Union
from enum import Enum
from .... import nodes
from ....Core.context import ctx, ExecutionPath
from ....Extras.TypeMgr import PlantType, ZombieType
from ..extension_node import ExtensionNode
from ...Original.Node import Port, to_port
from ....typing import _staticproperty, to_int_port, to_float_port, to_bool_port

class ForEachPlant(ExtensionNode):
    """Context manager that loops through a collection of Plant entities on the node canvas.

    Acts as a transparent proxy to the current `Plant` object, allowing direct calls to
    plant methods (e.g., `loop.die()`, `loop.heal()`) without explicitly accessing `.plant`.

    Example:
        ```python
        with pvn.ForEachPlant(target_plants) as plant:
            ...
            
        with plant.on_complete:
            ...
        ```
    """

    def __init__(self, plant_list_port):

        if hasattr(plant_list_port, "list_port"):
            plant_list_port = plant_list_port.list_port
        elif hasattr(plant_list_port, "value"):
            plant_list_port = plant_list_port.value

        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        super().__init__(root_node=self.node)
        self._plant_cache = None

    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Execution path context manager triggered after the loop finishes all iterations."""
        return ExecutionPath(self.node.id, "循环完成")

    @property
    def plant(self):
        """The current iterated plant wrapped in a smart Plant helper object."""
        if self._plant_cache is None:
            self._plant_cache = Plant(self.node.currentPlant)
        return self._plant_cache

    @property
    def index(self):
        """Output port representing the 0-based index of the current iteration."""
        return self.node.currentIndex

    # ==========================================================
    # TRANSPARENT PROXY TO PLANT WRAPPER
    # ==========================================================
    def __getattr__(self, name):
        """Forwards all plant methods and properties (heal, damage, die, row, col, etc.) directly."""
        return getattr(self.plant, name)


class ForEachPlantType(ExtensionNode):
    """Context manager that safely loops through a list of Plant Types natively on the canvas.

    Example:
        ```python
        with pvn.ForEachPlantType(allowed_plants) as loop:
            ...
        ```
    """

    def __init__(self, type_list_port):

        if hasattr(type_list_port, "list_port"):
            type_list_port = type_list_port.list_port
        elif hasattr(type_list_port, "value"):
            type_list_port = type_list_port.value

        self.node = nodes.for_each_plant_type(type_list=type_list_port)
        super().__init__(root_node=self.node)

    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

    @property
    def on_complete(self):
        """Execution path context manager triggered after the loop finishes all iterations."""
        return ExecutionPath(self.node.id, "循环完成")

    @property
    def plant_type(self):
        """Output port representing the plant type enum ID of the current iteration."""
        return self.node.currentPlantType

    # Aliases
    type = plant_type
    value = plant_type

    @property
    def index(self):
        """Output port representing the 0-based index of the current iteration."""
        return self.node.currentIndex

    # ==========================================================
    # DIRECT PORT & OPERATOR FORWARDING
    # ==========================================================
    def get_primary_port(self):
        return self.plant_type

    def _get_primary_port(self):
        return self.plant_type

    def __eq__(self, other):
        return self.plant_type == other

    def __ne__(self, other):
        return self.plant_type != other


class PlantTypeList(ExtensionNode):
    """A smart wrapper representing a dynamic or static list of Plant Types on the node canvas.

    Supports native collection operations (addition, subtraction, merging) and conditional 
    checks directly translated into graph nodes.

    Example:
    ```python
    # Create a list
    pool = pvn.PlantTypeList([PlantType.Peashooter, PlantType.WallNut])
    
    # Add and remove types dynamically
    pool += PlantType.CherryBomb
    pool -= PlantType.Peashooter
    ```
    """

    def __init__(self, initial: Any | None = None, initialize_empty: bool = True):
        super().__init__()
        self._current_port = None
        self._count_port = None

        if initial is None:
            storage = nodes.plant_type_list_storage(op=0, init_empty=initialize_empty)
            self._current_port = storage.currentList
            self._count_port = storage.count

        elif isinstance(initial, (Enum, int)):
            val = initial.value if isinstance(initial, Enum) else int(initial)
            multi_node = nodes.multi_plant_type_list(plant_types=[val])
            self._current_port = multi_node.plantTypeList
            self._count_port = nodes.int_value(val=1).value

        elif isinstance(initial, (list, tuple, set)) and not isinstance(
            initial, PortReference
        ):
            items = list(initial)
            if len(items) == 0:
                storage = nodes.plant_type_list_storage(
                    op=0, init_empty=initialize_empty
                )
                self._current_port = storage.currentList
                self._count_port = storage.count
            else:
                raw_types = [
                    item.value if isinstance(item, Enum) else int(item)
                    for item in items
                ]
                multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
                self._current_port = multi_node.plantTypeList
                self._count_port = nodes.int_value(val=len(raw_types)).value

        elif isinstance(initial, PlantTypeList):
            self._current_port = initial.list_port
            self._count_port = initial.count
        elif isinstance(initial, PortReference) or hasattr(initial, "node"):
            self._current_port = initial
        else:
            self._current_port = initial

    @property
    def list_port(self):
        """The underlying visual script output port for this list array."""
        return self._current_port

    @property
    def count(self):
        """Output port representing the number of items currently in the list."""
        if self._count_port is not None:
            return self._count_port
        return self._current_port

    def set(self, other: PlantTypeList | Iterable | Enum | int | Any):
        """Overwrites this list's contents with another list or collection."""
        new_list = PlantTypeList(other)
        self._current_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type):
        """
        Uses ForEachPlantTypeNode to search MultiPlantTypeListNode.
        Strictly prevents duplicate trigger wiring by isolating BaseNode.__init__.
        """

        raw_target = target_type.value if hasattr(target_type, "value") else target_type
        if isinstance(raw_target, int) and not isinstance(raw_target, PortReference):
            target_port = nodes.plant_type_value(val=raw_target).value
        elif hasattr(raw_target, "_get_primary_port"):
            target_port = raw_target._get_primary_port()  # type: ignore
        elif hasattr(raw_target, "value"):
            target_port = raw_target.value  # type: ignore
        else:
            target_port = raw_target

        parent_trigger = ctx.trigger_stack[-1] if ctx.trigger_stack else None

        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        match_toggle = nodes.toggle_node(initial_state=False)
        reset_branch = nodes.branch_node(condition=match_toggle.state)
        loop = nodes.for_each_plant_type(type_list=self._current_port)

        curr_type = PortReference(loop, "当前类型")
        is_equal = nodes.compare_plant_type(a=curr_type, b=target_port).equal
        match_branch = nodes.branch_node(condition=is_equal)
        state_guard = nodes.branch_node(condition=match_toggle.state)

        if parent_trigger:
            ctx.add_connection(
                parent_trigger.id, parent_trigger.out_trigger, reset_branch.id, "触发"
            )

        ctx.add_connection(reset_branch.id, "真（触发）", match_toggle.id, "触发")
        ctx.add_connection(reset_branch.id, "真（触发）", loop.id, "触发")
        ctx.add_connection(reset_branch.id, "假（停止）", loop.id, "触发")

        ctx.add_connection(loop.id, "循环体", match_branch.id, "触发")
        ctx.add_connection(match_branch.id, "真（触发）", state_guard.id, "触发")
        ctx.add_connection(state_guard.id, "假（停止）", match_toggle.id, "触发")

        ctx.trigger_stack.extend(saved_stack)
        ctx.trigger_stack[-1] = ExecutionPath(loop.id, "循环完成")

        return match_toggle.state

    def contains(self, plant_type: Enum | int | Iterable | Any):
        """Checks if the given plant type(s) exist within the list.

        Returns a boolean output port representing the evaluation result.
        """
        if isinstance(plant_type, (list, set)) and not isinstance(
            plant_type, PortReference
        ):
            items = list(plant_type)
            if not items:
                return nodes.bool_value(val=True).value

            result_wire = None
            for p in items:
                check_wire = self._contains_single(p)
                result_wire = (
                    check_wire if result_wire is None else (result_wire & check_wire)
                )
            return result_wire

        return self._contains_single(plant_type)

    def __iadd__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        if isinstance(other, (Enum, int)):
            val = other.value if isinstance(other, Enum) else int(other)
            single_node = nodes.single_plant_type_list(plant_type=val)
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=single_node.plantTypeList
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            raw_types = [
                item.value if isinstance(item, Enum) else int(item) for item in other
            ]
            multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=multi_node.plantTypeList
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif isinstance(other, PlantTypeList):
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=other.list_port
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count
        elif hasattr(other, "list_port") or hasattr(other, "node"):
            port = other.list_port if hasattr(other, "list_port") else other  # type: ignore
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=port
            )
            self._current_port = merge_node.mergedList
            self._count_port = merge_node.count

        return self

    def __add__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list += other
        return copy_list

    def __isub__(self, other: PlantTypeList | Enum | int | Iterable | Any):

        if isinstance(other, (Enum, int)):
            raw_val = other.value if isinstance(other, Enum) else int(other)
            rem_node = nodes.remove_plant_type(
                list_in=self._current_port, plant_type=raw_val
            )
            self._current_port = rem_node.resultList
        elif isinstance(other, (list, set)) and not isinstance(other, PortReference):
            for item in other:
                self.__isub__(item)
        elif isinstance(other, PlantTypeList):
            with ForEachPlantType(other.list_port) as loop:
                rem_node = nodes.remove_plant_type(
                    list_in=self._current_port, plant_type=loop.plant_type
                )
                self._current_port = rem_node.resultList
        elif hasattr(other, "node"):
            rem_node = nodes.remove_plant_type(
                list_in=self._current_port, plant_type=other
            )
            self._current_port = rem_node.resultList

        return self

    def __sub__(self, other: PlantTypeList | Enum | int | Iterable | Any):
        copy_list = PlantTypeList(self._current_port)
        copy_list._count_port = self._count_port
        copy_list -= other
        return copy_list

    def __eq__(self, other: 'PlantTypeList' | Any):  # type: ignore
        if isinstance(other, PlantTypeList):
            return nodes.compare_int(a=self.count, b=other.count).equal
        return False

    def add(self, plant_type: Enum | int | Any):
        """Adds a plant type to the list (chainable)."""
        self += plant_type
        return self

    def remove(self, plant_type: Enum | int | Any):
        """Removes a plant type from the list (chainable)."""
        self -= plant_type
        return self

    def get_random(self):
        """Retrieves a random PlantType port from the current contents of the list."""
        return nodes.get_random_plant_type(list_in=self._current_port).result

    def merge(self, other: 'PlantTypeList' | Any):
        """Merges another PlantTypeList into this list (chainable)."""
        self += other
        return self

    def for_each(self):
        """Returns a `ForEachPlantType` context manager to loop over this list."""
        return ForEachPlantType(self._current_port)


class Plant(ExtensionNode):
    """Smart wrapper around a runtime Plant entity pointer.

    Provides high-level actions, stat modifications, grid movement, and lazy-loaded
    properties via destructuring nodes.
    """

    def __init__(self, plant_ref):
        """Initializes a Plant wrapper referencing an existing plant port or pointer.

        Args:
            plant_ref: A raw node output reference port or an existing Plant instance.
        """
        super().__init__()
        if isinstance(plant_ref, Plant):
            self.ref = plant_ref.ref
        else:
            self.ref = plant_ref

        self._split_cache = None

    def get_primary_port(self):
        return to_port(self.ref) if self.ref is not None else None

    def _get_primary_port(self):
        return self.get_primary_port()

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def die(self):
        """Instantly kills and removes the plant from the lawn."""
        return nodes.die_plant(plant=self.ref)

    def damage(self, amount):
        """Inflicts a specified amount of damage to the plant.

        Args:
            amount (float | int | Any): Damage value or numeric node output port.
        """
        float_amount = to_float_port(amount)
        return nodes.damage_plant(plant=self.ref, damage=float_amount)

    def heal(self, amount):
        """Restores health to the plant by a specified amount.

        Args:
            amount (float | int | Any): Healing amount or numeric node output port.
        """
        float_amount = to_float_port(amount)
        return nodes.heal_plant(plant=self.ref, heal_amount=float_amount)

    def add_shield(self, amount):
        """Grants a protective shield value to the plant.

        Args:
            amount (float | int | Any): Shield amount or numeric node output port.
        """
        float_amount = to_float_port(amount)
        return nodes.give_plant_shield(plant=self.ref, shield=float_amount)

    def move(self, col, row, force=False):
        """Teleports the plant to absolute lawn grid coordinates.

        Args:
            col (int | Any): Target column index (0-based).
            row (int | Any): Target row index (0-based).
            force (bool | Any): When True, bypasses tile occupancy checks.
        """
        int_col = to_int_port(col)
        int_row = to_int_port(row)
        bool_force = to_bool_port(force)
        return nodes.move_plant(
            plant=self.ref, row=int_row, column=int_col, force=bool_force
        )

    def move_relative(self, col_diff, row_diff, force=False):
        """Moves the plant relative to its current board tile position.

        Args:
            col_diff (int | Any): Column offset from current position.
            row_diff (int | Any): Row offset from current position.
            force (bool | Any): When True, bypasses tile occupancy checks.
        """
        return self.move(
            col=self.col + col_diff, row=self.row + row_diff, force=force
        )

    def modify_attack(self, multiplier):
        """Scales the plant's attack power.

        Args:
            multiplier (float | int | Any): Attack scaling multiplier (e.g. 1.5 = +50%).
        """
        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_attack(
            plant=self.ref, multiplier=float_multiplier
        )

    def modify_health(self, multiplier):
        """Scales the plant's maximum and current health.

        Args:
            multiplier (float | int | Any): Health scaling multiplier (e.g. 2.0 = double HP).
        """
        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_health(
            plant=self.ref, multiplier=float_multiplier
        )

    def curse(self):
        """Curses the plant entity."""
        from ...Original.PlantFunction.curse_plant_node import CursePlantNode
        node = CursePlantNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, CursePlantNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(CursePlantNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, CursePlantNode.Complete_output_trigger)
        return self

    def silence(self):
        """Silences the plant entity, disabling ability triggers."""
        from ...Original.PlantFunction.silence_plant_node import SilencePlantNode
        node = SilencePlantNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SilencePlantNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SilencePlantNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SilencePlantNode.Complete_output_trigger)
        return self

    def feed_golden_bean(self):
        """Feeds a golden bean to the plant entity."""
        from ...Original.PlantFunction.feed_golden_bean_node import FeedGoldenBeanNode
        node = FeedGoldenBeanNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, FeedGoldenBeanNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(FeedGoldenBeanNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, FeedGoldenBeanNode.Complete_output_trigger)
        return self

    def super_skill(self):
        """Attempts to trigger the plant's ultimate/super skill."""
        from ...Original.PlantFunction.try_plant_super_skill_node import TryPlantSuperSkillNode
        node = TryPlantSuperSkillNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, TryPlantSuperSkillNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(TryPlantSuperSkillNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, TryPlantSuperSkillNode.Complete_output_trigger)
        return self

    def upgrade(self):
        """Upgrades the event plant entity."""
        from ...Original.PlantFunction.upgrade_event_plant_node import UpgradeEventPlantNode
        node = UpgradeEventPlantNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, UpgradeEventPlantNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(UpgradeEventPlantNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, UpgradeEventPlantNode.Complete_output_trigger)
        return self

    def set_attack_speed(self, speed):
        """Sets the attack speed of the plant."""
        from ...Original.PlantFunction.set_plant_attack_speed_node import SetPlantAttackSpeedNode
        node = SetPlantAttackSpeedNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetPlantAttackSpeedNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SetPlantAttackSpeedNode.Plant_input_plant))
        to_port(to_float_port(speed)).connect(node.get_input(SetPlantAttackSpeedNode.AttackSpeed_input_float))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetPlantAttackSpeedNode.Complete_output_trigger)
        return self

    def get_attack_speed(self):
        """Gets the attack speed port of the plant."""
        from ...Original.PlantFunction.get_plant_attack_speed_node import GetPlantAttackSpeedNode
        node = GetPlantAttackSpeedNode()
        to_port(self.ref).connect(node.get_input(GetPlantAttackSpeedNode.Plant_input_plant))
        return node.get_output(GetPlantAttackSpeedNode.AttackSpeed_output_float)

    def set_attack_interval(self, interval):
        """Sets the attack interval duration for the plant."""
        from ...Original.PlantFunction.set_plant_attack_interval_node import SetPlantAttackIntervalNode
        node = SetPlantAttackIntervalNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetPlantAttackIntervalNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SetPlantAttackIntervalNode.Plant_input_plant))
        to_port(to_float_port(interval)).connect(node.get_input(SetPlantAttackIntervalNode.AttackInterval_input_float))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetPlantAttackIntervalNode.Complete_output_trigger)
        return self

    def set_attribute_countdown(self, cd):
        """Sets the plant's attribute countdown."""
        from ...Original.PlantFunction.set_plant_attribute_countdown_node import SetPlantAttributeCountdownNode
        node = SetPlantAttributeCountdownNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetPlantAttributeCountdownNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SetPlantAttributeCountdownNode.Plant_input_plant))
        to_port(to_float_port(cd)).connect(node.get_input(SetPlantAttributeCountdownNode.Countdown_input_float))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetPlantAttributeCountdownNode.Complete_output_trigger)
        return self

    def get_attribute_countdown(self):
        """Gets the plant's attribute countdown port."""
        from ...Original.PlantFunction.get_plant_attribute_countdown_node import GetPlantAttributeCountdownNode
        node = GetPlantAttributeCountdownNode()
        to_port(self.ref).connect(node.get_input(GetPlantAttributeCountdownNode.Plant_input_plant))
        return node.get_output(GetPlantAttributeCountdownNode.PropertyCountdown_output_float)

    def get_components(self):
        """Returns the primary components GameObject reference of this plant."""
        from ...Original.PlantFunction.get_plant_basic_components_node import GetPlantBasicComponentsNode
        node = GetPlantBasicComponentsNode()
        to_port(self.ref).connect(node.get_input(GetPlantBasicComponentsNode.Plant_input_plant))
        return node.get_output(GetPlantBasicComponentsNode.Component_output_gameobject)

    def bind(self, name: str = "守护目标"):
        """Binds this plant under a given key in ObjectBinding."""
        from ...Original.ObjectBinding.bind_plant_node import BindPlantNode
        node = BindPlantNode(binding_name=name)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, BindPlantNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(BindPlantNode.Plant_input_plant))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, BindPlantNode.Complete_output_trigger)
        return self

    @classmethod
    def get_bound(cls, name: str = "守护目标") -> Plant:
        """Retrieves a previously bound plant instance by name."""
        from ...Original.ObjectBinding.get_bound_plant_node import GetBoundPlantNode
        node = GetBoundPlantNode(binding_name=name)
        return cls(node.get_output(GetBoundPlantNode.Plant_output_plant))

    def to_object(self):
        """Converts this Plant into an engine GameObject."""
        from ...Original.TypeConvert.plant_to_object_node import PlantToObjectNode
        from ..GameObject.game_object import GameObject
        node = PlantToObjectNode()
        to_port(self.ref).connect(node.get_input(PlantToObjectNode.Plant_input_plant))
        return GameObject(node.get_output(PlantToObjectNode.GameObject_output_gameobject))


    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via plant_split)
    # ==========================================================
    @property
    def _split(self):
        """Lazy-loaded destructuring node decomposing the plant reference."""
        if self._split_cache is None:
            self._split_cache = nodes.plant_split(plant=self.ref)
        return self._split_cache

    @property
    def plantType(self):
        """Output port representing the plant's type enum ID."""
        return self._split.plantType

    @property
    def row(self):
        """Output port representing the plant's current row coordinate."""
        return self._split.row

    @property
    def col(self):
        """Output port representing the plant's current column coordinate."""
        return self._split.column

    @property
    def attributeCD(self):
        """Output port representing the plant's internal ability cooldown counter."""
        return self._split.attributeCountdown


class Zombie(ExtensionNode):
    """Smart wrapper around a runtime Zombie entity pointer.

    Provides combat actions, mind control overrides, position shifts, animation triggers,
    and destructuring properties.
    """

    def __init__(self, zombie_ref):
        """Initializes a Zombie wrapper referencing an existing zombie port or pointer.

        Args:
            zombie_ref: A raw node output reference port or an existing Zombie instance.
        """
        super().__init__()
        if isinstance(zombie_ref, Zombie):
            self.ref = zombie_ref.ref
        else:
            self.ref = zombie_ref

        self._split_cache = None

    def get_primary_port(self):
        return to_port(self.ref) if self.ref is not None else None

    def _get_primary_port(self):
        return self.get_primary_port()

    # ==========================================================
    # ACTIONS & METHODS
    # ==========================================================
    def damage(self, amount):
        """Deals damage to the zombie.

        Args:
            amount (float | int | Any): Damage value or numeric node output port.
        """
        return nodes.damage_zombie(zombie=self.ref, damage=amount)

    def set_health_multiplier(self, ratio):
        """Modifies the zombie's health ratio.

        Args:
            ratio (float | int | Any): Health scaling ratio (e.g. 0.5 = half health).
        """
        float_ratio = to_float_port(ratio)
        return nodes.modify_zombie_health(zombie=self.ref, ratio=float_ratio)

    def hypnotize(self):
        """Mind-controls/hypnotizes the zombie to turn back and fight against other zombies."""
        return nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row, col):
        """Teleports the zombie to specific grid coordinates.

        Args:
            row (int | Any): Target row index.
            col (int | Any): Target column index.
        """
        int_row = to_int_port(row)
        int_col = to_int_port(col)
        return nodes.move_zombie(zombie=self.ref, row=int_row, column=int_col)

    def move_relative(self, row_diff=0, col_diff=0):
        """Shifts the zombie relative to its current grid position.

        Args:
            row_diff (int | Any): Row offset from current position. Defaults to 0.
            col_diff (int | Any): Column offset from current position. Defaults to 0.
        """
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    def play_animation(self, anim_name: str | Enum | Any = "idle"):
        """Plays a specific animation clip on the zombie model.

        Args:
            anim_name (str | Enum | Any): Name or Enum representing the target animation clip.
        """
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        return nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)

    # ==========================================================
    # LAZY DESTRUCTURED PROPERTIES (via zombie_split)
    # ==========================================================
    @property
    def split(self):
        """Lazy-loaded destructuring node decomposing the zombie reference."""
        if self._split_cache is None:
            self._split_cache = nodes.zombie_split(zombie=self.ref)
        return self._split_cache

    @property
    def zombieType(self):
        """Output port representing the zombie's type enum ID."""
        return self.split.zombieType

    @property
    def row(self):
        """Output port representing the zombie's current row coordinate."""
        return self.split.row

    @property
    def col(self):
        """Output port representing the zombie's current column coordinate."""
        return self.split.column

    def get_stats(self, stat: int = 0):
        """Queries a stat value from the zombie."""
        from ...Original.ZombieFunction.get_zombie_stats_node import GetZombieStatsNode
        node = GetZombieStatsNode(stat=stat)
        to_port(self.ref).connect(node.get_input(GetZombieStatsNode.Zombie_input_zombie))
        return node.get_output(GetZombieStatsNode.Value_output_float)

    def set_stats(self, value: Any, stat: int = 0):
        """Sets a stat value on the zombie."""
        from ...Original.ZombieFunction.set_zombie_stats_node import SetZombieStatsNode
        node = SetZombieStatsNode(stat=stat)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetZombieStatsNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SetZombieStatsNode.Zombie_input_zombie))
        to_port(to_float_port(value)).connect(node.get_input(SetZombieStatsNode.Value_input_float))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetZombieStatsNode.Complete_output_trigger)
        return self

    def get_status(self, status: int = 0):
        """Queries whether this zombie has a specific status flag active."""
        from ...Original.ZombieFunction.get_zombie_status_node import GetZombieStatusNode
        node = GetZombieStatusNode(status=status)
        to_port(self.ref).connect(node.get_input(GetZombieStatusNode.Zombie_input_zombie))
        return node.get_output(GetZombieStatusNode.HasState_output_bool)

    def set_status(self, state: Any, status: int = 0):
        """Toggles or sets a status flag on this zombie."""
        from ...Original.ZombieFunction.set_zombie_status_node import SetZombieStatusNode
        node = SetZombieStatusNode(status=status)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, SetZombieStatusNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(SetZombieStatusNode.Zombie_input_zombie))
        to_port(to_bool_port(state)).connect(node.get_input(SetZombieStatusNode.State_input_bool))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, SetZombieStatusNode.Complete_output_trigger)
        return self

    def bind(self, name: str = "守护目标"):
        """Binds this zombie under a named key in ObjectBinding."""
        from ...Original.ObjectBinding.bind_zombie_node import BindZombieNode
        node = BindZombieNode(binding_name=name)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, BindZombieNode.Trigger_input_trigger)
        to_port(self.ref).connect(node.get_input(BindZombieNode.Zombie_input_zombie))
        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, BindZombieNode.Complete_output_trigger)
        return self

    @classmethod
    def get_bound(cls, name: str = "守护目标") -> Zombie:
        """Retrieves a previously bound zombie instance by name."""
        from ...Original.ObjectBinding.get_bound_zombie_node import GetBoundZombieNode
        node = GetBoundZombieNode(binding_name=name)
        return cls(node.get_output(GetBoundZombieNode.Zombie_output_zombie))

    def to_object(self):
        """Converts this Zombie into an engine GameObject."""
        from ...Original.TypeConvert.zombie_to_object_node import ZombieToObjectNode
        from ..GameObject.game_object import GameObject
        node = ZombieToObjectNode()
        to_port(self.ref).connect(node.get_input(ZombieToObjectNode.Zombie_input_zombie))
        return GameObject(node.get_output(ZombieToObjectNode.GameObject_output_gameobject))


class ForEachZombie(ExtensionNode):
    """Context manager looping over a collection of Zombie entities."""

    def __init__(self, zombie_list_port: Any) -> None:
        from ...Original.ZombieFunction.for_each_zombie_node import ForEachZombieNode
        self.node = ForEachZombieNode()
        super().__init__(root_node=self.node)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self.node.node_id, ForEachZombieNode.Trigger_input_trigger)
        to_port(zombie_list_port).connect(self.node.get_input(ForEachZombieNode.ZombieList_input_zombielist))
        self._zombie_cache = None

    def __enter__(self) -> Zombie:
        from ...Original.ZombieFunction.for_each_zombie_node import ForEachZombieNode
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, ForEachZombieNode.LoopBody_output_trigger))
        if self._zombie_cache is None:
            self._zombie_cache = Zombie(self.node.get_output(ForEachZombieNode.CurrentZombie_output_zombie))
        return self._zombie_cache

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        from ...Original.ZombieFunction.for_each_zombie_node import ForEachZombieNode
        if ctx.trigger_stack:
            ctx.trigger_stack.pop()
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, ForEachZombieNode.LoopComplete_output_trigger))

    @property
    def on_complete(self) -> ExecutionPath:
        from ...Original.ZombieFunction.for_each_zombie_node import ForEachZombieNode
        return ExecutionPath(self.node.node_id, ForEachZombieNode.LoopComplete_output_trigger)


class ForEachAllZombies(ExtensionNode):
    """Context manager looping over all Zombie entities currently on the lawn."""

    def __init__(self) -> None:
        from ...Original.ZombieFunction.for_each_all_zombies_node import ForEachAllZombiesNode
        self.node = ForEachAllZombiesNode()
        super().__init__(root_node=self.node)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self.node.node_id, ForEachAllZombiesNode.Trigger_input_trigger)
        self._zombie_cache = None

    def __enter__(self) -> Zombie:
        from ...Original.ZombieFunction.for_each_all_zombies_node import ForEachAllZombiesNode
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, ForEachAllZombiesNode.LoopBody_output_trigger))
        if self._zombie_cache is None:
            self._zombie_cache = Zombie(self.node.get_output(ForEachAllZombiesNode.CurrentZombie_output_zombie))
        return self._zombie_cache

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        from ...Original.ZombieFunction.for_each_all_zombies_node import ForEachAllZombiesNode
        if ctx.trigger_stack:
            ctx.trigger_stack.pop()
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, ForEachAllZombiesNode.LoopComplete_output_trigger))

    @property
    def on_complete(self) -> ExecutionPath:
        from ...Original.ZombieFunction.for_each_all_zombies_node import ForEachAllZombiesNode
        return ExecutionPath(self.node.node_id, ForEachAllZombiesNode.LoopComplete_output_trigger)


__all__ = [
    "ForEachPlant",
    "ForEachPlantType",
    "PlantTypeList",
    "Plant",
    "Zombie",
    "ForEachZombie",
    "ForEachAllZombies",
]

