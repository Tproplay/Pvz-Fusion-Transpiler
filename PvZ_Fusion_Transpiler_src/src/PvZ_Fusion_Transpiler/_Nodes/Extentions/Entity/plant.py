from __future__ import annotations

from typing import Any
from .... import nodes
from ....typing import to_float_port, to_int_port, to_bool_port


class Plant:
    """Smart wrapper around a runtime Plant entity pointer.

    Provides high-level actions, stat modifications, grid movement, and lazy-loaded
    properties via destructuring nodes.
    """

    def __init__(self, plant_ref: Any) -> None:
        if isinstance(plant_ref, Plant):
            self.ref: Any = plant_ref.ref
        else:
            self.ref = plant_ref
        self._split_cache: Any = None

    def die(self) -> Any:
        return nodes.die_plant(plant=self.ref)

    def damage(self, amount: Any) -> Any:
        float_amount = to_float_port(amount)
        return nodes.damage_plant(plant=self.ref, damage=float_amount)

    def heal(self, amount: Any) -> Any:
        float_amount = to_float_port(amount)
        return nodes.heal_plant(plant=self.ref, heal_amount=float_amount)

    def add_shield(self, amount: Any) -> Any:
        float_amount = to_float_port(amount)
        return nodes.give_plant_shield(plant=self.ref, shield=float_amount)

    def move(self, col: Any, row: Any, force: Any = False) -> Any:
        int_col = to_int_port(col)
        int_row = to_int_port(row)
        bool_force = to_bool_port(force)
        return nodes.move_plant(
            plant=self.ref, row=int_row, column=int_col, force=bool_force
        )

    def move_relative(self, col_diff: Any, row_diff: Any, force: Any = False) -> Any:
        return self.move(
            col=self.col + col_diff, row=self.row + row_diff, force=force
        )

    def modify_attack(self, multiplier: Any) -> Any:
        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_attack(
            plant=self.ref, multiplier=float_multiplier
        )

    def modify_health(self, multiplier: Any) -> Any:
        float_multiplier = to_float_port(multiplier)
        return nodes.modify_plant_health(
            plant=self.ref, multiplier=float_multiplier
        )

    @property
    def _split(self) -> Any:
        if self._split_cache is None:
            self._split_cache = nodes.plant_split(plant=self.ref)
        return self._split_cache

    @property
    def plantType(self) -> Any:
        return self._split.port_output_planttype_PlantType

    @property
    def row(self) -> Any:
        return self._split.port_output_int_Row

    @property
    def col(self) -> Any:
        return self._split.port_output_int_Col

    @property
    def attributeCD(self) -> Any:
        return self._split.port_output_int_AttributeCountdown

    def curse(self, curse_value: Any) -> Any:
        return nodes.curse_plant(plant=self.ref, curse_value=curse_value)

    def silence(self, silence_value: Any) -> Any:
        return nodes.silence_plant(plant=self.ref, silence_value=silence_value)

    def feed_golden_bean(self) -> Any:
        return nodes.feed_golden_bean(plant=self.ref)

    def try_super_skill(self) -> Any:
        return nodes.try_plant_super_skill(plant=self.ref)

    def upgrade(self, target_level: Any, star: Any = False) -> Any:
        return nodes.upgrade_event_plant(plant=self.ref, target_level=target_level, star=star)

    def get_attack_speed(self) -> Any:
        return nodes.get_plant_attack_speed(plant=self.ref)

    def set_attack_speed(self, multiplier: Any) -> Any:
        return nodes.set_plant_attack_speed(plant=self.ref, speed=multiplier)

    def set_attack_interval(self, seconds: Any) -> Any:
        return nodes.set_plant_attack_interval(plant=self.ref, interval=seconds)

    def get_attribute_countdown(self) -> Any:
        return nodes.get_plant_attribute_countdown(plant=self.ref)

    def set_attribute_countdown(self, remaining: Any = None, max_seconds: Any = None) -> Any:
        return nodes.set_plant_attribute_countdown(plant=self.ref, remaining=remaining, max_seconds=max_seconds)

    def get_basic_components(self) -> Any:
        return nodes.get_plant_basic_components(plant_type=self.plantType).port_output_planttypelist_PlantTypeList

    def to_object(self) -> Any:
        return nodes.plant_to_object(plant=self.ref).port_output_gameobject_GameObject

    def ToString(self) -> Any:
        conv = nodes.plant_type_to_string(plant_type=self.plantType)
        return conv.port_output_string_String

    to_string = ToString


__all__ = ["Plant"]
