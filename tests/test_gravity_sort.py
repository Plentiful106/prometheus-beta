import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_normal_case():
    """Test gravity sort with a typical list of positive integers."""
    input_list = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_already_sorted():
    """Test gravity sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_reverse_sorted():
    """Test gravity sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_with_duplicates():
    """Test gravity sort with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_empty_list():
    """Test gravity sort with an empty list."""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test gravity sort with a single-element list."""
    input_list = [42]
    expected = [42]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_invalid_input_negative():
    """Test that ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        gravity_sort([-1, 2, 3])

def test_gravity_sort_invalid_input_non_integer():
    """Test that ValueError is raised for non-integer values."""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        gravity_sort([1, 2.5, 3])