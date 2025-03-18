import pytest
from src.find_unique_element import find_single_unique_element

def test_single_unique_element_in_middle():
    """Test finding unique element in the middle of the array."""
    arr = [1, 1, 2, 3, 3, 4, 4]
    assert find_single_unique_element(arr) == 2

def test_single_unique_element_at_start():
    """Test finding unique element at the start of the array."""
    arr = [2, 3, 3, 4, 4, 5, 5]
    assert find_single_unique_element(arr) == 2

def test_single_unique_element_at_end():
    """Test finding unique element at the end of the array."""
    arr = [1, 1, 2, 2, 3, 4, 5]
    assert find_single_unique_element(arr) == 5

def test_single_element_array():
    """Test array with only one element."""
    arr = [42]
    assert find_single_unique_element(arr) == 42

def test_empty_array_raises_error():
    """Test that empty array raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_unique_element([])

def test_none_array_raises_error():
    """Test that None input raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_unique_element(None)

def test_invalid_input_no_unique_element():
    """Test array where all elements appear twice."""
    with pytest.raises(ValueError, match="No unique element found"):
        find_single_unique_element([1, 1, 2, 2, 3, 3])

def test_large_array():
    """Test a larger array with unique element."""
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
    assert find_single_unique_element(arr) == 7