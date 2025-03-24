import pytest
from src.rotated_array_search import search_rotated_array

def test_search_rotated_array_normal_case():
    """Test searching in a typical rotated sorted array"""
    arr = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_array(arr, 0) == 4
    assert search_rotated_array(arr, 3) == -1

def test_search_rotated_array_no_rotation():
    """Test array with no rotation"""
    arr = [1, 2, 3, 4, 5]
    assert search_rotated_array(arr, 3) == 2
    assert search_rotated_array(arr, 6) == -1

def test_search_rotated_array_single_element():
    """Test array with single element"""
    arr = [1]
    assert search_rotated_array(arr, 1) == 0
    assert search_rotated_array(arr, 0) == -1

def test_search_rotated_array_empty():
    """Test empty array"""
    arr = []
    assert search_rotated_array(arr, 5) == -1

def test_search_rotated_array_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        search_rotated_array(None, 5)
    
    with pytest.raises(TypeError):
        search_rotated_array([1, 2, 3], "5")

def test_search_rotated_array_edge_cases():
    """Test various edge cases"""
    # Rotation at the beginning
    arr = [5, 1, 2, 3, 4]
    assert search_rotated_array(arr, 1) == 1
    
    # Rotation at the end
    arr = [2, 3, 4, 5, 1]
    assert search_rotated_array(arr, 1) == 4
    
    # Large rotation
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert search_rotated_array(arr, 5) == 8
    assert search_rotated_array(arr, 16) == 1