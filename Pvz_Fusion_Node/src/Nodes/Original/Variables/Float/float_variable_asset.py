from typing import Optional
from ...VariableAsset import VariableAsset


class FloatVariableAsset(VariableAsset):
    asset_class = "FloatVariableAsset"

    def __init__(
        self,
        name: str = "浮点数",
        initial_value: float = 0.0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=float(initial_value),
            variable_id=variable_id,
            rid=rid,
        )

    @property
    def value(self) -> float:
        return float(self._value)

    @value.setter
    def value(self, val: float) -> None:
        self._value = float(val)
