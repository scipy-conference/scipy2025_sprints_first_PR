import pytest

from pr_tutorial.simple_functions import factorial,fibonacci



@pytest.mark.parametrize("value, expected", [
    (0, 1),
    (3, 6),
    (5, 120),
])
def test_factorial_3(value: int, expected: int):
    """Simplest test for one crete case"""

    assert factorial(value) == expected


@pytest.mark.parametrize("n_terms, expected", [
    (0, [0, 1]),
    (1, [0, 1]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test__fibonacci(n_terms: int, expected: list[int]):
    """Simplest test for one crete case"""

    assert fibonacci(n_terms) == expected

