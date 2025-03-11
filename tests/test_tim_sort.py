import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element"""
    assert tim_sort([5]) == [5]

def test_tim_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert tim_sort(arr) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert tim_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_tim_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-4, 1, -9, 0, 5, -2]
    assert tim_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_tim_sort_large_list():
    """Test sorting a large list"""
    arr = list(range(1000, 0, -1))
    assert tim_sort(arr) == list(range(1, 1001))

def test_tim_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert tim_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_tim_sort_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        tim_sort("not a list")

def test_tim_sort_preserves_original_list():
    """Test that the original list is not modified"""
    original = [5, 2, 8, 1, 9]
    tim_sort(original)
    assert original == [5, 2, 8, 1, 9]