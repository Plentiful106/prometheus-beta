import pytest
from src.array_rotation import rotate_array

def test_rotate_array_basic():
    """Test basic array rotation"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_array_full_rotation():
    """Test rotation equal to array length (no change)"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 5) == arr

def test_rotate_array_empty():
    """Test rotation of empty array"""
    assert rotate_array([], 3) == []

def test_rotate_array_single_element():
    """Test rotation of single-element array"""
    assert rotate_array([1], 10) == [1]

def test_rotate_array_large_rotation():
    """Test rotation larger than array length"""
    assert rotate_array([1, 2, 3], 7) == [2, 3, 1]

def test_rotate_array_zero_rotation():
    """Test zero rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array(arr, 0) == arr

def test_invalid_input_non_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)

def test_invalid_input_non_integer_rotation():
    """Test non-integer rotation amount raises TypeError"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_invalid_input_negative_rotation():
    """Test negative rotation amount raises ValueError"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)