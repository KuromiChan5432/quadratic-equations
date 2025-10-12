import pytest
from solving_simple_quadratic_equations import solve
from unittest.mock import patch


def test_quadratic_standart():
    with patch("builtins.input", return_value="x^2+17x-18=0"):
        result1, result2 = solve()
        assert result1 == -18
        assert result2 == 1
def test_quadratic_big_numbers():
    with patch("builtins.input", return_value="x^2-52x+285=0"):
        result1, result2 = solve()
        assert result1 == 6.23
        assert result2 == 45.77
def test_quadratic_random():
    with patch("builtins.input", return_value="7x+13-x^2=0"):
        result1, result2 = solve()
        assert result1 == 8.52
        assert result2 == -1.52
def test_quadratic_no_c():
    with patch("builtins.input", return_value="x^2+11x=0"):
        result1, result2 = solve()
        assert result1 == -11
        assert result2 == 0