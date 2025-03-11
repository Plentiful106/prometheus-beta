import pytest
from src.quickselect import quickselect

def test_quickselect_basic():
    """Test basic functionality of quickselect"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert quickselect(arr, 1) == 1  # 1st smallest
    assert quickselect(arr, 3) == 2  # 3rd smallest
    assert quickselect(arr, 6) == 4  # 6th smallest

def test_quickselect_with_duplicates():
    """Test quickselect with an array containing duplicate elements"""
    arr = [3, 3, 3, 2, 1, 1, 4]
    assert quickselect(arr, 1) == 1  # 1st smallest
    assert quickselect(arr, 3) == 1  # 3rd smallest
    assert quickselect(arr, 6) == 3  # 6th smallest

def test_quickselect_sorted_array():
    """Test quickselect with an already sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quickselect(arr, 1) == 1  # 1st smallest
    assert quickselect(arr, 5) == 5  # 5th smallest
    assert quickselect(arr, 9) == 9  # 9th smallest

def test_quickselect_reverse_sorted_array():
    """Test quickselect with a reverse sorted array"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert quickselect(arr, 1) == 1  # 1st smallest
    assert quickselect(arr, 5) == 5  # 5th smallest
    assert quickselect(arr, 9) == 9  # 9th smallest

def test_quickselect_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        quickselect([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 4)

def test_quickselect_single_element():
    """Test quickselect with a single-element array"""
    arr = [42]
    assert quickselect(arr, 1) == 42