import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic functionality of finding duplicates."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_find_duplicates_no_duplicates():
    """Test scenario with no duplicates."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_empty_list():
    """Test with an empty list."""
    assert find_duplicates([]) == []

def test_find_duplicates_all_duplicates():
    """Test with a list where all elements are duplicates."""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_find_duplicates_multiple_duplicates():
    """Test with multiple instances of duplicates."""
    assert find_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]

def test_find_duplicates_negative_numbers():
    """Test with negative numbers."""
    assert find_duplicates([-1, -1, 0, 1, 1]) == [-1, 1]

def test_find_duplicates_large_list():
    """Test with a larger list with duplicates."""
    large_list = list(range(1000)) * 2
    result = find_duplicates(large_list)
    assert len(result) == 1000
    assert all(num in large_list for num in result)
    assert sorted(result) == list(range(1000))

def test_find_duplicates_returned_list_order():
    """Ensure returned list is sorted."""
    assert find_duplicates([3, 1, 2, 2, 1]) == [1, 2]