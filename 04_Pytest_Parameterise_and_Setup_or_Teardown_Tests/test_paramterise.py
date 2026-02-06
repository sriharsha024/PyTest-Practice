import pytest
import math


@pytest.mark.parametrize("test_input", [82, 78, 45, 66])
def test_param01(test_input):
    """
    Verify that all input values are greater than 50.
    """
    assert test_input > 50


@pytest.mark.parametrize(
    "inp, expected",
    [(2, 4), (3, 27), (4, 256)]
)
def test_param02(inp, expected):
    """
    Validate power calculations where the input
    is raised to the power of itself.
    """
    assert inp ** inp == expected


test_data = [
    ([2, 3, 4], "sum", 9),
    ([2, 3, 4], "prod", 24),
]


@pytest.mark.parametrize("numbers, operation, expected", test_data)
def test_param03(numbers, operation, expected):
    """
    Validate sum and product operations on a list
    using parametrized test data.
    """
    if operation == "sum":
        assert sum(numbers) == expected
    elif operation == "prod":
        assert math.prod(numbers) == expected
