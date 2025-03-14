import pytest
from src.longest_subarray import longest_subarray_max_diff

def test_basic_scenarios():
    # Basic scenarios with different array lengths and k values
    assert longest_subarray_max_diff([1, 5, 3, 8], 2) == 3
    assert longest_subarray_max_diff([1, 2, 3, 4], 1) == 4
    assert longest_subarray_max_diff([10, 1, 5, 8, 7], 3) == 3

def test_single_element_array():
    # Single element always returns 1
    assert longest_subarray_max_diff([42], 0) == 1

def test_all_equal_elements():
    # When no adjacent elements meet the difference requirement
    assert longest_subarray_max_diff([5, 5, 5, 5], 1) == 1

def test_k_zero():
    # Test case when k is zero
    assert longest_subarray_max_diff([1, 2, 3, 4, 5], 0) == 5

def test_large_differences():
    # Test with large differences
    assert longest_subarray_max_diff([100, 1, 200, 3, 400], 50) == 3

def test_error_handling():
    # Test error scenarios
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        longest_subarray_max_diff([], 2)
    
    with pytest.raises(ValueError, match="k must be a non-negative integer"):
        longest_subarray_max_diff([1, 2, 3], -1)

def test_negative_numbers():
    # Test with negative numbers
    assert longest_subarray_max_diff([-1, -5, -3, -8], 2) == 3