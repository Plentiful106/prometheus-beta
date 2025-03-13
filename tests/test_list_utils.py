import pytest
from src.list_utils import find_common

def test_find_common_basic():
    """Test finding common elements in simple lists"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert find_common(list1, list2) == [4, 5]

def test_find_common_empty_lists():
    """Test behavior with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test when no common elements exist"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_common(list1, list2) == []

def test_find_common_duplicate_elements():
    """Test with lists containing duplicate elements"""
    list1 = [1, 2, 2, 3, 4, 4]
    list2 = [2, 4, 5, 5]
    assert find_common(list1, list2) == [2, 4]

def test_find_common_different_types():
    """Test with different types of hashable elements"""
    list1 = [1, 'a', (1, 2), 3.14]
    list2 = ['b', (1, 2), 3.14, 5]
    assert find_common(list1, list2) == [(1, 2), 3.14]

def test_find_common_order_preservation():
    """Test that the order of first occurrence in list1 is preserved"""
    list1 = [5, 2, 3, 4, 2]
    list2 = [2, 4, 6]
    assert find_common(list1, list2) == [2, 4]