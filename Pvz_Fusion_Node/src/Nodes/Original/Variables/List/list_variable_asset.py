from __future__ import annotations

from enum import IntEnum
from typing import Any, List, Optional, Union
from ...VariableAsset import VariableAsset


class ListElementType(IntEnum):
    """Element type enum for ListVariableAsset, matching the in-game editor dropdown."""
    Integer = 0
    Float = 1      # 小数
    Bool = 2       # 布尔
    String = 3
    PlantType = 4  # 植物类型
    ZombieType = 5 # 僵尸类型
    Object = 6     # 对象 (stores target binding name in text)


class ListElementItem:
    """Represents Unity's serialized union struct for a list item."""

    __slots__ = ("integer", "number", "boolean", "text")

    def __init__(
        self,
        integer: int = 0,
        number: float = 0.0,
        boolean: bool = False,
        text: str = "",
    ):
        self.integer: int = integer
        self.number: float = number
        self.boolean: bool = boolean
        self.text: str = text

    @classmethod
    def from_value(cls, val: Any, element_type: ListElementType) -> "ListElementItem":
        """Constructs an element struct based on the targeted element type."""
        # Normalize enums
        if hasattr(val, "value"):
            val = val.value

        if element_type in (ListElementType.Integer, ListElementType.PlantType, ListElementType.ZombieType):
            return cls(integer=int(val))
        elif element_type == ListElementType.Float:
            return cls(number=float(val))
        elif element_type == ListElementType.Bool:
            return cls(boolean=bool(val))
        elif element_type in (ListElementType.String, ListElementType.Object):
            return cls(text=str(val))
        return cls()

    def to_dict(self) -> dict:
        return {
            "integer": self.integer,
            "number": self.number,
            "boolean": self.boolean,
            "text": self.text,
        }


class ListVariableAsset(VariableAsset):
    """Represents a ListVariableAsset in references.RefIds with multi-type union items."""

    asset_class = "ListVariableAsset"

    def __init__(
        self,
        name: str = "列表",
        element_type: Union[ListElementType, int] = ListElementType.Integer,
        initial_values: Optional[List[Any]] = None,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        self.element_type: ListElementType = ListElementType(element_type)
        
        # Parse initial values into ListElementItem structs
        items = []
        if initial_values:
            for v in initial_values:
                if isinstance(v, ListElementItem):
                    items.append(v)
                else:
                    items.append(ListElementItem.from_value(v, self.element_type))

        super().__init__(
            name=name,
            initial_value=items,
            variable_id=variable_id,
            rid=rid,
        )

    def add_item(self, val: Any) -> None:
        """Appends a new value formatted into the Unity union struct."""
        if isinstance(val, ListElementItem):
            self._value.append(val)
        else:
            self._value.append(ListElementItem.from_value(val, self.element_type))

    def dump_data(self) -> dict:
        return {
            "name": self.name,
            "variableId": self.variable_id,
            "referencedNodeIds": list(self.referenced_node_ids),
            "valueType": int(self.element_type),
            "values": [item.to_dict() if hasattr(item, "to_dict") else item for item in self._value],
        }
