import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15, 17]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test floating point perfect squares."""
    floating_squares = [4.0, 9.0, 16.0, 25.0]
    for num in floating_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_floating_point_non_squares():
    """Test floating point non-perfect squares."""
    floating_non_squares = [2.1, 3.5, 5.7, 7.2]
    for num in floating_non_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_square = 1000000  # 1000^2
    assert is_perfect_square(large_square) is True

def test_zero_and_one():
    """Test edge cases of 0 and 1."""
    assert is_perfect_square(0) is True
    assert is_perfect_square(1) is True

def test_negative_number_raises_value_error():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)

def test_non_numeric_input_raises_type_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)