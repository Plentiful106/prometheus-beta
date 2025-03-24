import pytest
from src.merge_sorted_arrays import merge_sorted_arrays, is_sorted

def test_merge_sorted_arrays_basic():
    """Test merging two sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_different_lengths():
    """Test merging arrays of different lengths"""
    arr1 = [1, 4, 7, 8, 10]
    arr2 = [2, 3, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 8, 10]

def test_merge_sorted_arrays_empty_array():
    """Test merging with an empty array"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    assert merge_sorted_arrays([], arr1) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    """Test merging two empty arrays"""
    assert merge_sorted_arrays([], []) == []

def test_merge_sorted_arrays_with_duplicates():
    """Test merging arrays with duplicate values"""
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4, 5]

def test_is_sorted_function():
    """Test the is_sorted helper function"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 1, 2, 3]) == True
    assert is_sorted([]) == True
    assert is_sorted([5, 4, 3]) == False

def test_merge_sorted_arrays_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_merge_sorted_arrays_unsorted_input():
    """Test error handling for unsorted inputs"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [4, 5, 6])
    
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [6, 5, 4])