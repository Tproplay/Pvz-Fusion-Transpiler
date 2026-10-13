from typing import Optional
from ...VariableAsset import VariableAsset


class StringVariableAsset(VariableAsset):
    asset_class = "StringVariableAsset"

    def __init__(
        self,
        name: str = "字符串",
        initial_value: str = "",
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=str(initial_value),
            variable_id=variable_id,
            rid=rid,
        )

    @property
    def value(self) -> str:
        return str(self._value)

    @value.setter
    def value(self, val: str) -> None:
        self._value = str(val)
