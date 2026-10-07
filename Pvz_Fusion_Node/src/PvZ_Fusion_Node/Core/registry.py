"""
Deterministic RID allocator and Symbol Registry for references.RefIds.
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional


class SymbolRegistry:
    def __init__(self, start_rid: int = 1000):
        self.current_rid: int = start_rid
        self._registered_items: List[Any] = []
        self._asset_cache: Dict[str, Any] = {}

    def allocate_rid(self) -> int:
        rid = self.current_rid
        self.current_rid += 1
        return rid

    def register(self, item: Any) -> Any:
        # Deduplicate variable assets by variableId
        if hasattr(item, "variable_id"):
            vid = item.variable_id
            if vid in self._asset_cache:
                return self._asset_cache[vid]
            self._asset_cache[vid] = item

        if getattr(item, "rid", None) is None:
            item.rid = self.allocate_rid()

        if item not in self._registered_items:
            self._registered_items.append(item)
        return item

    def dump_ref_ids(self) -> List[Dict[str, Any]]:
        return [item.dump_ref() for item in self._registered_items]
