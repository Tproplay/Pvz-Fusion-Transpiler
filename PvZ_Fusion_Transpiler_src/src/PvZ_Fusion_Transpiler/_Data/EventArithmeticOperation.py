from enum import Enum


class EventArithmeticOperation(Enum):
    """EventArithmeticOperation enum in PvZ Fusion."""

    Add = 0
    Subtract = 1
    Multiply = 2
    Divide = 3
    Modulo = 4


__all__ = ["EventArithmeticOperation"]
