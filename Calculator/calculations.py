"""
Module for managing calculation history.
"""

from typing import List, Optional
from Calculator.calculation import Calculation

class Calculations:
    """Manages a history of calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a calculation to history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history.clear()

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Returns the last calculation in history, or None if empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history_length(cls) -> int:
        """Returns the number of calculations stored in history."""
        return len(cls.history)

    @classmethod
    def is_history_empty(cls) -> bool:
        """Returns True if the history is empty, False otherwise."""
        return len(cls.history) == 0
