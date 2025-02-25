import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_regular_numbers():
    """Test sorting a list of regular numbers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 0, -3, 10, -1, 8]
    expected = [-5, -3, -1, 0, 8, 10]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_duplicate_numbers():
    """Test sorting a list with duplicate numbers."""
    input_list = [4, 2, 4, 1, 3, 2]
    expected = [1, 2, 2, 3, 4, 4]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    expected = []
    assert bubble_sort(input_list) == expected

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    expected = [42]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_float_numbers():
    """Test sorting a list of float numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert bubble_sort(input_list) == expected

def test_bubble_sort_non_list_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        bubble_sort("not a list")

def test_bubble_sort_non_comparable_elements():
    """Test that TypeError is raised for non-comparable elements."""
    with pytest.raises(TypeError):
        bubble_sort([1, 2, "a", 3])