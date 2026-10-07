from typing import Optional
from ...VariableAsset import VariableAsset


class BoolVariableAsset(VariableAsset):
    asset_class = "BoolVariableAsset"

    def __init__(
        self,
        name: str = "布尔值",
        initial_value: bool = False,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=bool(initial_value),
            variable_id=variable_id,
            rid=rid,
        )

    @property
    def value(self) -> bool:
        return bool(self._value)

    @value.setter
    def value(self, val: bool) -> None:
        self._value = bool(val)
