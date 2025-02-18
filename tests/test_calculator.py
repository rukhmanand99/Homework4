"""
Unit tests for the Calculator class using Faker for test data.
"""
# pylint: disable=invalid-name

import pytest
from faker import Faker
from Calculator.calculator import Calculator
from Calculator.calculations import Calculations

fake = Faker()


@pytest.fixture(autouse=True)
def clear_history():
    """Clear calculation history before each test."""
    Calculations.clear_history()


@pytest.mark.parametrize(
    "a, b",
    [(fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100)) for _ in range(5)],
)
def test_add(a, b):
    """Test addition with Faker-generated inputs."""
    assert Calculator.add(a, b) == a + b


@pytest.mark.parametrize(
    "a, b",
    [(fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100)) for _ in range(5)],
)
def test_subtract(a, b):
    """Test subtraction with Faker-generated inputs."""
    assert Calculator.subtract(a, b) == a - b


@pytest.mark.parametrize(
    "a, b",
    [(fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100)) for _ in range(5)],
)
def test_multiply(a, b):
    """Test multiplication with Faker-generated inputs."""
    assert Calculator.multiply(a, b) == a * b


@pytest.mark.parametrize(
    "a, b",
    [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(5)],
)
def test_divide(a, b):
    """Test division with Faker-generated inputs."""
    assert Calculator.divide(a, b) == a / b


def test_divide_by_zero():
    """Test division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(fake.random_int(min=1, max=100), 0)
