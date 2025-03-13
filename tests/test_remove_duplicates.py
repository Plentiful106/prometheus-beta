import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal in a sorted list"""
    assert remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    """Test list with a single element"""
    assert remove_duplicates([42]) == [42]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_negative_numbers():
    """Test list with negative numbers"""
    assert remove_duplicates([-3, -3, -2, -1, -1, 0, 0, 1, 1]) == [-3, -2, -1, 0, 1]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, "3", 4])

def test_preserves_sorted_order():
    """Ensure the function preserves the original sorted order"""
    sorted_list = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
    assert remove_duplicates(sorted_list) == [1, 2, 3, 4, 5, 6]