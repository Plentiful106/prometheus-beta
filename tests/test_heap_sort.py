import pytest
from src.heap_sort import heap_sort

def test_heap_sort_basic():
    """Test sorting a basic list of integers."""
    assert heap_sort([4, 1, 3, 9, 7]) == [1, 3, 4, 7, 9]

def test_heap_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_heap_sort_empty_list():
    """Test sorting an empty list."""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a list with a single element."""
    assert heap_sort([42]) == [42]

def test_heap_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert heap_sort([-4, 1, -9, 0, 5]) == [-9, -4, 0, 1, 5]

def test_heap_sort_floating_point():
    """Test sorting a list with floating-point numbers."""
    assert heap_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_heap_sort_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort("not a list")

def test_heap_sort_preserves_original_list():
    """Test that the original list is not modified."""
    original = [4, 1, 3, 9, 7]
    heap_sort(original)
    assert original == [4, 1, 3, 9, 7]