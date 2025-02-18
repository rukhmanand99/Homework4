"""
Unit tests for main.py, ensuring 100% test coverage.
"""

import sys
import subprocess
import pytest
from main import calculate

@pytest.mark.parametrize("num1, num2, operation, expected_output", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate(num1, num2, operation, expected_output):
    """Tests the calculate function directly."""
    assert calculate(num1, num2, operation) == expected_output

@pytest.mark.parametrize("num1, num2, operation, expected_output", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero"),
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")
])
def test_main_script(num1, num2, operation, expected_output):
    """Tests command-line execution of main.py."""
    result = subprocess.run(
        [sys.executable, "main.py", num1, num2, operation],
        capture_output=True,
        text=True,
        check=True  # Explicitly setting check=True to satisfy Pylint
    )
    assert expected_output in result.stdout

def test_main_script_usage():
    """Tests the script without enough arguments to trigger the usage message."""
    result = subprocess.run(
        [sys.executable, "main.py", "5", "3"],
        capture_output=True,
        text=True,
        check=False  # No need to enforce an error on expected failure case
    )
    assert "Usage: python main.py <num1> <num2> <operation>" in result.stdout
