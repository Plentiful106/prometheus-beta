import pytest
from src.bitwise_and_range import bitwise_and_range

def test_basic_range():
    """Test bitwise AND for a simple range of numbers."""
    assert bitwise_and_range(5, 7) == 4

def test_single_number():
    """Test when start and end are the same number."""
    assert bitwise_and_range(10, 10) == 10

def test_same_numbers():
    """Test range with repeated numbers."""
    assert bitwise_and_range(3, 3) == 3

def test_zero_range():
    """Test range starting with zero."""
    assert bitwise_and_range(0, 2) == 0

def test_invalid_input_negative():
    """Test raising error for negative inputs."""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(-1, 5)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(5, -1)

def test_invalid_input_start_greater_than_end():
    """Test raising error when start is greater than end."""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)