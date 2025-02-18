"""
Pytest configuration file to generate dynamic test cases using Faker.
"""

import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add command line option --num_records to pytest."""
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate",
    )

@pytest.fixture(scope="session")
def num_records(request):
    """Return the number of records specified via the command line."""
    return request.config.getoption("--num_records")

@pytest.fixture(
    scope="function",
    params=[
        (fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100))
        for _ in range(10)  # Reduced count for better test execution
    ],
)
def random_numbers(request):
    """Generate dynamic test data using Faker."""
    return request.param

# ** Temporary self-test to improve coverage **
@pytest.fixture(scope="session", autouse=True)
def _test_conftest_fixtures(request):
    """Ensure fixtures are covered in pytest."""
    num_records_value = request.config.getoption("--num_records")
    assert isinstance(num_records_value, int)
    assert num_records_value > 0  # Ensures at least 1 test record
