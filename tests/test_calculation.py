"""
Unit tests for the Calculations class.
"""

import operator
import pytest
from Calculator.calculations import Calculations
from Calculator.calculation import Calculation


def setup_function():
    """Clear history before each test."""
    Calculations.clear_history()


def test_add_calculation():
    """Test adding a calculation to history."""
    calc = Calculation(operator.add, 2, 3)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 5


def test_clear_history():
    """Test clearing history."""
    Calculations.add_calculation(Calculation(operator.add, 2, 3))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0


def test_get_history():
    """Test retrieving the history of calculations."""
    calc1 = Calculation(operator.add, 1, 1)
    calc2 = Calculation(operator.mul, 2, 3)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    history = Calculations.get_history()
    assert len(history) == 2
    assert history[0].get_result() == 2
    assert history[1].get_result() == 6


def test_get_last_calculation():
    """Test retrieving the last calculation."""
    calc1 = Calculation(operator.sub, 5, 3)
    calc2 = Calculation(operator.truediv, 10, 2)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    last_calc = Calculations.get_last_calculation()
    assert last_calc.get_result() == 5.0  # 10 / 2


def test_get_last_calculation_empty():
    """Test getting last calculation when history is empty."""
    assert Calculations.get_last_calculation() is None


def test_invalid_operand_types():
    """Test invalid operand types."""
    with pytest.raises(TypeError):
        Calculation(operator.add, "a", 3)

    with pytest.raises(TypeError):
        Calculation(operator.mul, 4, None)


def test_division_by_zero():
    """Test division by zero case."""
    calc = Calculation(operator.truediv, 5, 0)
    assert calc.get_result() == float('inf')


def test_repr():
    """Test the string representation of Calculation."""
    calc = Calculation(operator.add, 2, 3)
    assert repr(calc) == "Calculation(2 add 3 = 5)"


def test_from_tuple():
    """Test creating a Calculation from a tuple."""
    calc = Calculation.from_tuple((operator.sub, 8, 3))
    assert calc.get_result() == 5

    with pytest.raises(ValueError):
        Calculation.from_tuple((operator.add, 2))  # Invalid tuple length


def test_history_storage():
    """Test that calculations persist in history."""
    calc = Calculation(operator.mul, 4, 5)
    Calculations.add_calculation(calc)

    stored_calc = Calculations.get_history()[0]
    assert stored_calc.get_result() == 20


def test_clear_and_re_add():
    """Test clearing history and adding new calculations."""
    Calculations.add_calculation(Calculation(operator.add, 1, 1))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

    calc = Calculation(operator.sub, 7, 4)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 3
