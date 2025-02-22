import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test basic functionality of finding missing numbers"""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_find_missing_numbers_no_missing():
    """Test when no numbers are missing"""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_find_missing_numbers_large_gaps():
    """Test finding missing numbers with larger gaps"""
    assert find_missing_numbers([10, 20, 30]) == list(range(11, 30))

def test_find_missing_numbers_consecutive_array():
    """Test with a consecutive array of two elements"""
    assert find_missing_numbers([1, 2]) == []

def test_find_missing_numbers_single_element():
    """Test with a single element array"""
    assert find_missing_numbers([5]) == []

def test_find_missing_numbers_invalid_input():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError):
        find_missing_numbers([])