import pytest
from src.unique_sorted_list import get_unique_sorted_integers

def test_basic_functionality():
    """Test basic list of integers."""
    assert get_unique_sorted_integers([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 2, 3, 4, 5, 6, 9]

def test_already_sorted():
    """Test list that is already sorted."""
    assert get_unique_sorted_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test empty list."""
    assert get_unique_sorted_integers([]) == []

def test_single_element():
    """Test list with a single element."""
    assert get_unique_sorted_integers([42]) == [42]

def test_negative_numbers():
    """Test list with negative numbers."""
    assert get_unique_sorted_integers([-3, -1, -4, 0, 1, 3]) == [-4, -3, -1, 0, 1, 3]

def test_invalid_input_non_list():
    """Test non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_invalid_input_non_integers():
    """Test list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])

def test_repeated_elements():
    """Test list with repeated elements."""
    assert get_unique_sorted_integers([5, 5, 5, 5]) == [5]