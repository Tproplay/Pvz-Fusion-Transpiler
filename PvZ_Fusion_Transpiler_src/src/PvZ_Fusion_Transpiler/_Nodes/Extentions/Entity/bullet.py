from __future__ import annotations

from typing import Any
from .... import nodes
from ....typing import to_float_port


class Bullet:
    """Smart wrapper around a runtime Bullet entity pointer.

    Provides bullet modification actions and property access.
    """

    def __init__(self, bullet_ref: Any) -> None:
        if isinstance(bullet_ref, Bullet):
            self.ref: Any = bullet_ref.ref
        else:
            self.ref = bullet_ref

    def modify(self, value: Any) -> Any:
        float_val = to_float_port(value)
        return nodes.modify_event_bullet(bullet=self.ref, value=float_val)

    def _get_primary_port(self) -> Any:
        return self.ref


__all__ = ["Bullet"]
