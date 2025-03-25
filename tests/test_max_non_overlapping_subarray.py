import pytest
import random
from src.max_non_overlapping_subarray import max_non_overlapping_subarray_sum

# ... (previous tests remain the same)

def test_large_input():
    """Test with maximum allowed input size and varied integers."""
    # Generate array of 10,000 elements between -10,000 and 10,000
    large_arr = [random.randint(-10000, 10000) for _ in range(10000)]
    result = max_non_overlapping_subarray_sum(large_arr)
    assert isinstance(result, int), "Result must be an integer"
    assert result is not None, "Result cannot be None"

def test_boundary_input_size():
    """Test minimum and maximum input sizes."""
    # Minimum size (1 element)
    assert isinstance(max_non_overlapping_subarray_sum([42]), int)
    
    # Maximum size (10,000 elements)
    max_arr = [random.randint(-10000, 10000) for _ in range(10000)]
    assert isinstance(max_non_overlapping_subarray_sum(max_arr), int)