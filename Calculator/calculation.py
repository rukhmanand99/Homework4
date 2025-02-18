"""
Module for storing individual calculations.
"""

from typing import Callable


class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, operation: Callable[[float, float], float], a: float, b: float):
        """
        Initializes a Calculation instance.

        :param operation: A function representing the arithmetic operation.
        :param a: First operand (must be float or int).
        :param b: Second operand (must be float or int).
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be int or float")

        self.operation = operation
        self.a = a
        self.b = b

        try:
            self.result = self.operation(self.a, self.b)
        except ZeroDivisionError:
            self.result = float('inf')  # Return infinity for division by zero

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result

    def __repr__(self):
        """Returns a string representation of the calculation."""
        op_name = self.operation.__name__ if hasattr(self.operation, '__name__') else "unknown_op"
        return f"Calculation({self.a} {op_name} {self.b} = {self.result})"

    @staticmethod
    def from_tuple(data: tuple):
        """
        Creates a Calculation instance from a tuple.

        :param data: Tuple in the format (operation, a, b)
        :return: Calculation instance
        """
        if not isinstance(data, tuple) or len(data) != 3:
            raise ValueError("Tuple must contain exactly three elements: (operation, a, b)")
        return Calculation(*data)
