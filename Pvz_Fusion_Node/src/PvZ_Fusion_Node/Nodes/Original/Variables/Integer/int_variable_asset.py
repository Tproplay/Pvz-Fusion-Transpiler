from typing import Optional
from ...VariableAsset import VariableAsset


class IntVariableAsset(VariableAsset):
    asset_class = "IntVariableAsset"

    def __init__(
        self,
        name: str = "整数",
        initial_value: int = 0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=int(initial_value),
            variable_id=variable_id,
            rid=rid,
        )

    @property
    def value(self) -> int:
        return int(self._value)

    @value.setter
    def value(self, val: int) -> None:
        self._value = int(val)
