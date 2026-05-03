"""Tests for calculator module."""
import pytest
from src.calculator import add, divide, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(3, 2) == 1.5
    assert divide(0, 1) == 0.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
