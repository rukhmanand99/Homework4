"""
Advanced Calculator with calculation history.
"""

from Calculator.calculation import Calculation
from Calculator.calculations import Calculations

class Calculator:
    """A calculator that supports arithmetic operations and stores history."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Performs addition and stores in history."""
        calc = Calculation(lambda x, y: x + y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Performs subtraction and stores in history."""
        calc = Calculation(lambda x, y: x - y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Performs multiplication and stores in history."""
        calc = Calculation(lambda x, y: x * y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Performs division and stores in history. Raises an error if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        calc = Calculation(lambda x, y: x / y, a, b)
        Calculations.add_calculation(calc)
        return calc.get_result()