"""
Unit tests for the Calculations class.
"""
import operator
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
    Calculations.add_calculation(Calculation(operator.mul, 4, 5))
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


def test_get_history_length():
    """Test retrieving the number of calculations in history."""
    assert Calculations.get_history_length() == 0  # Empty initially

    Calculations.add_calculation(Calculation(operator.sub, 8, 4))
    assert Calculations.get_history_length() == 1

    Calculations.add_calculation(Calculation(operator.mul, 6, 2))
    assert Calculations.get_history_length() == 2


def test_is_history_empty():
    """Test checking if history is empty."""
    assert Calculations.is_history_empty() is True  # Initially empty

    Calculations.add_calculation(Calculation(operator.add, 2, 3))
    assert Calculations.is_history_empty() is False  # Now it has one item

    Calculations.clear_history()
    assert Calculations.is_history_empty() is True  # After clearing


def test_calculation_persistence():
    """Test that calculations persist correctly in history."""
    calc1 = Calculation(operator.add, 1, 2)
    calc2 = Calculation(operator.mul, 3, 4)

    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)

    assert Calculations.get_history_length() == 2
    assert Calculations.get_last_calculation().get_result() == 12  # 3 * 4


def test_clear_and_re_add():
    """Test clearing history and adding new calculations."""
    Calculations.add_calculation(Calculation(operator.sub, 9, 3))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

    calc = Calculation(operator.truediv, 8, 2)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0].get_result() == 4.0
