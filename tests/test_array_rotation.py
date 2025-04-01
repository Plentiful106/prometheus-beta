import pytest
from src.array_rotation import rotate_array_right

def test_basic_rotation():
    """Test basic array rotation"""
    assert rotate_array_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotation_full_length():
    """Test rotation equal to array length"""
    assert rotate_array_right([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    assert rotate_array_right([1, 2, 3], 5) == [2, 3, 1]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array_right([], 3) == []

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_array_right([1, 2, 3], 0) == [1, 2, 3]

def test_invalid_input_non_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_right("not a list", 2)

def test_invalid_rotation_type():
    """Test non-integer rotation amount raises TypeError"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_right([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount raises ValueError"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_right([1, 2, 3], -1)

def test_single_element_array():
    """Test rotation of single-element array"""
    assert rotate_array_right([42], 3) == [42]