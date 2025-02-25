import pytest
from src.mode_finder import find_mode

def test_single_mode():
    """Test finding a single mode in a list of numbers."""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes when frequencies are equal."""
    assert sorted(find_mode([1, 2, 2, 3, 3, 4])) == [2, 3]

def test_all_unique_numbers():
    """Test list where all numbers appear once."""
    assert find_mode([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]

def test_mode_with_floats():
    """Test finding mode with floating point numbers."""
    assert find_mode([1.5, 2.5, 2.5, 3.5]) == 2.5

def test_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])

def test_single_element_list():
    """Test list with a single element."""
    assert find_mode([42]) == 42

def test_mode_at_beginning_end():
    """Test mode at the start and end of the list."""
    assert find_mode([5, 1, 2, 3, 5]) == 5