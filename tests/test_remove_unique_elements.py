import pytest
from src.remove_unique_elements import remove_unique_elements

def test_remove_duplicate_elements():
    """Test removing duplicate elements from a list"""
    input_list = [1, 2, 2, 3, 3, 4, 5]
    expected = [2, 3]
    assert sorted(remove_unique_elements(input_list)) == sorted(expected)

def test_no_duplicates():
    """Test a list with no duplicates returns an empty list"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_unique_elements(input_list) == []

def test_all_duplicates():
    """Test a list with all duplicates returns the list"""
    input_list = [1, 1, 1, 1]
    assert remove_unique_elements(input_list) == [1, 1, 1, 1]

def test_empty_list():
    """Test an empty list returns an empty list"""
    input_list = []
    assert remove_unique_elements(input_list) == []

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_unique_elements("not a list")

def test_invalid_element_type():
    """Test that a list with non-integer elements raises a TypeError"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        remove_unique_elements([1, 2, "3", 4])