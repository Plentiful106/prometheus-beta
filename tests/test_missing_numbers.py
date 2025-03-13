import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending array."""
    arr = [1, 3, 5, 7, 9]
    assert find_missing_numbers(arr) == [2, 4, 6, 8]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending array."""
    arr = [9, 7, 5, 3, 1]
    assert find_missing_numbers(arr) == [2, 4, 6, 8]

def test_no_missing_numbers():
    """Test when no numbers are missing."""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_large_gaps():
    """Test with large gaps between numbers."""
    arr = [2, 5, 8, 11]
    assert find_missing_numbers(arr) == [3, 4, 6, 7, 9, 10]

def test_single_element():
    """Test with a single element array."""
    arr = [5]
    assert find_missing_numbers(arr) == [1, 2, 3, 4]

def test_error_handling_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_error_handling_non_positive():
    """Test error handling for non-positive integers."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_error_handling_non_integer():
    """Test error handling for non-integer inputs."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, 3.5, 4])