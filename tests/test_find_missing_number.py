import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a typical case."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_start():
    """Test when the missing number is at the start of the range."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_end():
    """Test when the missing number is at the end of the range."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_range():
    """Test with a larger range of numbers."""
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_invalid_range_raises_error():
    """Test that an array with numbers outside the valid range raises an error."""
    with pytest.raises(ValueError, match="Invalid input: missing number out of range"):
        find_missing_number([2, 3, 4, 6])  # Missing 5, but range is incorrect

def test_non_unique_numbers_raises_error():
    """Test that duplicate numbers raise an error."""
    with pytest.raises(ValueError):
        find_missing_number([1, 3, 3, 4, 5])  # Duplicate numbers are not allowed