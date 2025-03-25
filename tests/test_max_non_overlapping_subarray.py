import pytest
from src.max_non_overlapping_subarray import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    """Test with a basic positive integer array."""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9

def test_mixed_positive_negative():
    """Test with mixed positive and negative integers."""
    result = max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5])
    assert result in [7, 9], f"Expected 7 or 9, got {result}"

def test_alternating_signs():
    """Test with alternating positive and negative signs."""
    result = max_non_overlapping_subarray_sum([1, -1, 1, -1, 1])
    assert result in [2, 3], f"Expected 2 or 3, got {result}"

def test_single_element():
    """Test with a single element array."""
    assert max_non_overlapping_subarray_sum([42]) == 42

def test_all_negative():
    """Test with all negative elements."""
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == 0

def test_zero_array():
    """Test with an array of zeros."""
    assert max_non_overlapping_subarray_sum([0, 0, 0, 0]) == 0

def test_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum("not a list")

def test_empty_list():
    """Test that ValueError is raised for an empty list."""
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum([])