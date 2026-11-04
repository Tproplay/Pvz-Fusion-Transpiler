from enum import Enum


class ListStorageOperation(Enum):
    """ListStorageOperation enum in PvZ Fusion."""

    Set = 0
    Add = 1
    Remove = 2


__all__ = ["ListStorageOperation"]
