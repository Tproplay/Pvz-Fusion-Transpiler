from enum import IntEnum

class ListStorageOperation(IntEnum):
    """Operation enum for list storage manipulation matching Unity IL2CPP GameLevel.EventNodes.ListStorageOperation."""
    Set = 0
    Add = 1
    Remove = 2
