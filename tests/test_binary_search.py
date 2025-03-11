import pytest
from src.binary_search import binary_search

def test_binary_search_normal_case():
    """Test binary search with a standard sorted list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 15) == 7

def test_binary_search_not_found():
    """Test when target is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 16) == -1

def test_binary_search_empty_list():
    """Test binary search with an empty list"""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element():
    """Test binary search with a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(ValueError):
        binary_search([5, 3, 1], 3)  # Unsorted list

def test_binary_search_duplicate_elements():
    """Test binary search with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    # Note: Returns the index of any occurrence of the target
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 2) in [1, 2]