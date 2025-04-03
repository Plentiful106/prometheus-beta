import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_standard_sequence():
    """Test a standard case with multiple increasing subsequences."""
    assert find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_empty_list():
    """Test an empty list returns 0."""
    assert find_longest_increasing_subsequence([]) == 0

def test_single_element():
    """Test a list with a single element."""
    assert find_longest_increasing_subsequence([5]) == 1

def test_already_sorted_sequence():
    """Test a sequence that is already sorted in ascending order."""
    assert find_longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_descending_sequence():
    """Test a sequence in descending order."""
    assert find_longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_repeated_elements():
    """Test a sequence with repeated elements."""
    assert find_longest_increasing_subsequence([2, 2, 2, 2]) == 1

def test_mixed_elements():
    """Test a sequence with mixed increasing subsequences."""
    assert find_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_invalid_list_contents():
    """Test that a list with non-integer elements raises a ValueError."""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "3", 4])