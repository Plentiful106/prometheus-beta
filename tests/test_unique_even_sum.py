import pytest
from src.unique_even_sum import sum_unique_even_numbers

def test_basic_unique_even_sum():
    """Test basic functionality with unique even numbers."""
    assert sum_unique_even_numbers([1, 2, 3, 4, 2, 6]) == 6

def test_no_even_numbers():
    """Test when there are no even numbers."""
    assert sum_unique_even_numbers([1, 3, 5]) == 0

def test_empty_list():
    """Test with an empty list."""
    assert sum_unique_even_numbers([]) == 0

def test_all_duplicate_evens():
    """Test when all even numbers are duplicates."""
    assert sum_unique_even_numbers([2, 2, 4, 4, 6, 6]) == 0

def test_mixed_unique_and_duplicate_evens():
    """Test with a mix of unique and duplicate even numbers."""
    assert sum_unique_even_numbers([2, 2, 4, 6, 8, 10, 10]) == 6

def test_negative_numbers():
    """Test with negative even numbers."""
    assert sum_unique_even_numbers([-2, 2, -4, 4, -6]) == 0

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_unique_even_numbers("not a list")

def test_invalid_element_type():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_even_numbers([1, 2, "3", 4])