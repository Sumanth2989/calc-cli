import math
import pytest
from calculator.operations import add, sub, mul, div

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 5),
        (-2, 3, 1),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (5, 2, 3),
        (-2, -3, 1),
        (2.5, 0.5, 2.0),
    ],
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 6),
        (-2, 3, -6),
        (2.5, 0.5, 1.25),
    ],
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (-6, 3, -2),
        (2.5, 0.5, 5.0),
    ],
)
def test_div(a, b, expected):
    assert div(a, b) == expected

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
