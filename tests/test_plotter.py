import pytest
from plotter import validate_function, evaluate_function

def test_validate_function():
    assert validate_function("5*x^3 + 2*x")
    assert not validate_function("5*x^3 + 2*x + @")

def test_evaluate_function():
    x = 2
    assert evaluate_function("5*x^3 + 2*x", x) == 5*2**3 + 2*2
