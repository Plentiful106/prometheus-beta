import pytest
from src.patience_sort import patience_sort

def test_basic_sorting():
    """Test sorting of a basic integer list"""
    input_list = [5, 3, 7, 1, 9, 2]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_already_sorted_list():
    """Test sorting of an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting of a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_duplicates():
    """Test sorting of a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert patience_sort(input_list) == sorted(input_list)

def test_empty_list():
    """Test sorting of an empty list"""
    assert patience_sort([]) == []

def test_single_element_list():
    """Test sorting of a single-element list"""
    input_list = [42]
    assert patience_sort(input_list) == input_list

def test_list_with_negative_numbers():
    """Test sorting of a list with negative numbers"""
    input_list = [-5, 3, -2, 7, 1, -9, 2]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_floating_point_numbers():
    """Test sorting of a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert patience_sort(input_list) == sorted(input_list)

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        patience_sort("not a list")
    
    with pytest.raises(TypeError):
        patience_sort(123)
    
    with pytest.raises(TypeError):
        patience_sort(None)