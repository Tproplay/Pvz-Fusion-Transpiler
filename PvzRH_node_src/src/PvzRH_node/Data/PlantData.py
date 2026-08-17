from __future__ import annotations

from typing import Any

from .plant_data_methods import PlantDataMethodsMixin
from .plant_defaults import PLANT_DEFAULTS, PlantDefaultStats
from .TypeMgr import PlantType


def _to_json_val(val: Any) -> Any:
    return val.value if hasattr(val, "value") else val


class PlantData(PlantDataMethodsMixin):
    """Factory helper for generating plant runtime data overrides."""

    @staticmethod
    def get_defaults(plant_type: int | PlantType) -> PlantDefaultStats | None:
        """Returns baseline stats for a given plant."""
        p_id = int(_to_json_val(plant_type))
        return PLANT_DEFAULTS.get(p_id)

    @classmethod
    def create(
        cls,
        plant_type: int | PlantType,
        cost: int | None = None,
        cd: float | None = None,
        max_health: int | None = None,
        attack_damage: int | None = None,
        attack_interval: float | None = None,
        produce_interval: float | None = None,
    ) -> dict[str, Any]:
        """
        Creates a PlantData configuration dictionary.
        Any omitted parameter (None) defaults to the plant's official base stat.
        """
        p_id = int(_to_json_val(plant_type))
        defaults = PLANT_DEFAULTS.get(p_id)

        d_cost = defaults.cost if defaults else 100
        d_cd = defaults.cd if defaults else 10.0
        d_hp = defaults.max_health if defaults else 300
        d_dmg = defaults.attack_damage if defaults else 0
        d_atk_int = defaults.attack_interval if defaults else 0.0
        d_prod_int = defaults.produce_interval if defaults else 25.0

        return {
            "thePlantType": p_id,
            "cost": int(cost if cost is not None else d_cost),
            "cd": float(cd if cd is not None else d_cd),
            "maxHealth": int(max_health if max_health is not None else d_hp),
            "attackDamage": int(attack_damage if attack_damage is not None else d_dmg),
            "attackInterval": float(attack_interval if attack_interval is not None else d_atk_int),
            "produceInterval": float(produce_interval if produce_interval is not None else d_prod_int),
        }