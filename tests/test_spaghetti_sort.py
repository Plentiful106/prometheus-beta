import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test basic sorting functionality"""
    assert spaghetti_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_spaghetti_sort_empty_list():
    """Test sorting an empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test sorting a single-element list"""
    assert spaghetti_sort([42]) == [42]

def test_spaghetti_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert spaghetti_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_spaghetti_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert spaghetti_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_spaghetti_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    assert spaghetti_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_spaghetti_sort_zero_elements():
    """Test sorting a list with zero"""
    assert spaghetti_sort([0, 0, 0]) == [0, 0, 0]

def test_spaghetti_sort_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        spaghetti_sort("not a list")

def test_spaghetti_sort_negative_numbers():
    """Test that negative numbers raise ValueError"""
    with pytest.raises(ValueError):
        spaghetti_sort([1, 2, -3, 4])

def test_spaghetti_sort_non_integer():
    """Test that non-integer elements raise ValueError"""
    with pytest.raises(ValueError):
        spaghetti_sort([1, 2, 3.14, 4])