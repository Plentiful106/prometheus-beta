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
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 15, 17, 99]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_floating_point_perfect_squares():
    """Test floating point perfect squares."""
    floating_point_squares = [4.0, 9.0, 16.0, 25.0]
    for num in floating_point_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_floating_point_non_perfect_squares():
    """Test floating point numbers that are not perfect squares."""
    floating_point_non_squares = [2.5, 3.7, 10.1]
    for num in floating_point_non_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_perfect_square = 1000000  # 1000^2
    assert is_perfect_square(large_perfect_square) is True

def test_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
        is_perfect_square(-1)

def test_invalid_input_types():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("not a number")
        is_perfect_square([4])
        is_perfect_square(None)