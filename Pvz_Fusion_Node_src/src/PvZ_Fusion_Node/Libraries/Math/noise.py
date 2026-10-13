"""
Coherent gradient noise generation (Perlin noise) for procedural scripting.
"""

from __future__ import annotations
import math
from typing import Any

from .arithmetic import _ensure_float_port
from ... import nodes
from ...node_base import PortReference

# 8 standard 2D gradient vectors
_GRADIENTS = [
    (1.0, 0.0),
    (-1.0, 0.0),
    (0.0, 1.0),
    (0.0, -1.0),
    (0.7071, 0.7071),
    (-0.7071, 0.7071),
    (0.7071, -0.7071),
    (-0.7071, -0.7071),
]


def perlin_noise(x: Any, y: Any = 0.0) -> Any:
    """Calculates 2D Gradient Perlin Noise normalized to [0.0, 1.0]."""
    raw_x = _ensure_float_port(x)
    raw_y = _ensure_float_port(y)

    is_x_static = isinstance(raw_x, (int, float)) and not isinstance(raw_x, PortReference) and not hasattr(raw_x, "node")
    is_y_static = isinstance(raw_y, (int, float)) and not isinstance(raw_y, PortReference) and not hasattr(raw_y, "node")

    # 1. Compile-Time Static Python Evaluation
    if is_x_static and is_y_static:
        x_val, y_val = float(raw_x), float(raw_y)

        def _hash_2d(ix: int, iy: int) -> int:
            h = (ix * 0x1F1F1F1F) ^ (iy * 0x5B5B5B5B)
            h = (h ^ (h >> 13)) * 0x45D9F3B
            h = (h ^ (h >> 16)) & 0x7FFFFFFF
            return h % 8

        def _fade(t: float) -> float:
            return t * t * t * (t * (t * 6.0 - 15.0) + 10.0)

        x0, y0 = math.floor(x_val), math.floor(y_val)
        x1, y1 = x0 + 1, y0 + 1

        dx, dy = x_val - x0, y_val - y0
        u, v = _fade(dx), _fade(dy)

        def _dot(ix: int, iy: int, rx: float, ry: float) -> float:
            gx, gy = _GRADIENTS[_hash_2d(ix, iy)]
            return gx * rx + gy * ry

        d00 = _dot(x0, y0, dx, dy)
        d10 = _dot(x1, y0, dx - 1.0, dy)
        d01 = _dot(x0, y1, dx, dy - 1.0)
        d11 = _dot(x1, y1, dx - 1.0, dy - 1.0)

        nx0 = d00 + u * (d10 - d00)
        nx1 = d01 + u * (d11 - d01)
        raw_noise = nx0 + v * (nx1 - nx0)

        return builtins_max(0.0, builtins_min(1.0, (raw_noise + 0.7071) / 1.4142))

    # 2. Runtime Node Graph Calculation
    x_int = nodes.float_to_int(float_val=raw_x).int
    y_int = nodes.float_to_int(float_val=raw_y).int
    x0_float = nodes.int_to_float(int_val=x_int).float
    y0_float = nodes.int_to_float(int_val=y_int).float

    tx = nodes.subtract_node(a=raw_x, b=x0_float).result
    ty = nodes.subtract_node(a=raw_y, b=y0_float).result

    tx_sq = nodes.multiply_node(a=tx, b=tx).result
    sx = nodes.multiply_node(
        a=tx_sq,
        b=nodes.subtract_node(
            a=3.0, b=nodes.multiply_node(a=tx, b=2.0).result
        ).result,
    ).result

    ty_sq = nodes.multiply_node(a=ty, b=ty).result
    sy = nodes.multiply_node(
        a=ty_sq,
        b=nodes.subtract_node(
            a=3.0, b=nodes.multiply_node(a=ty, b=2.0).result
        ).result,
    ).result

    v00 = nodes.divide_node(
        a=nodes.int_to_float(
            int_val=nodes.int_modulo(
                a=nodes.int_multiply(
                    a=nodes.int_add(
                        a=nodes.int_multiply(a=x_int, b=374761393).result,
                        b=nodes.int_multiply(a=y_int, b=668265263).result,
                    ).result,
                    b=1274126177,
                ).result,
                b=1000003,
            ).result
        ).float,
        b=1000003.0,
    ).result

    return v00


def noise1d(x: Any) -> Any:
    """Calculates 1D Gradient Noise by sampling 2D Perlin noise along y=0."""
    return perlin_noise(x, 0.0)


# Helper alias to avoid shadowing builtins in local scope
builtins_max = max
builtins_min = min

__all__ = [
    "perlin_noise",
    "noise1d",
]
