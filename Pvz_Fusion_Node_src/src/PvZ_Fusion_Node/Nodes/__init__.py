"""
PvZ Fusion Nodes Package.
Contains Original (base engine nodes) and Extentions (composite extension nodes).
"""

__all__ = [
    "Original",
    "Extentions",
]

def __getattr__(name: str):
    from . import Extentions
    if hasattr(Extentions, name):
        return getattr(Extentions, name)
    from . import Original
    if hasattr(Original, name):
        return getattr(Original, name)
    raise AttributeError(f"module 'PvZ_Fusion_Node.Nodes' has no attribute '{name}'")
