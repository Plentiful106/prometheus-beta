import pytest
from src.simple_calculator import simple_calculator

def test_addition():
    """Test addition operation."""
    assert simple_calculator(5, 3, '+') == 8
    assert simple_calculator(-2, 2, '+') == 0
    assert simple_calculator(1.5, 2.5, '+') == 4.0

def test_subtraction():
    """Test subtraction operation."""
    assert simple_calculator(10, 4, '-') == 6
    assert simple_calculator(2, 5, '-') == -3
    assert simple_calculator(3.5, 1.2, '-') == 2.3

def test_multiplication():
    """Test multiplication operation."""
    assert simple_calculator(5, 3, '*') == 15
    assert simple_calculator(-2, 4, '*') == -8
    assert simple_calculator(1.5, 2, '*') == 3.0

def test_division():
    """Test division operation."""
    assert simple_calculator(10, 2, '/') == 5
    assert simple_calculator(7, 3, '/') == 7/3
    assert simple_calculator(-6, 3, '/') == -2

def test_invalid_operator():
    """Test handling of invalid operators."""
    with pytest.raises(ValueError, match="Invalid operator"):
        simple_calculator(5, 3, '%')
    with pytest.raises(ValueError, match="Invalid operator"):
        simple_calculator(5, 3, '^')

def test_division_by_zero():
    """Test handling of division by zero."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        simple_calculator(10, 0, '/')

def test_string_inputs():
    """Test handling of string inputs that can be converted to numbers."""
    assert simple_calculator('5', '3', '+') == 8
    assert simple_calculator('5.5', '2.5', '*') == 13.75