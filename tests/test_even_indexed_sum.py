import pytest
from src.even_indexed_sum import sum_even_indexed_elements

def test_sum_even_indexed_elements_basic():
    """Test sum of even-indexed elements in a basic list."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9

def test_sum_even_indexed_elements_negative():
    """Test sum of even-indexed elements with negative numbers."""
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -9

def test_sum_even_indexed_elements_empty():
    """Test sum of even-indexed elements in an empty list."""
    assert sum_even_indexed_elements([]) == 0

def test_sum_even_indexed_elements_single_element():
    """Test sum of even-indexed elements with a single element."""
    assert sum_even_indexed_elements([42]) == 42

def test_sum_even_indexed_elements_two_elements():
    """Test sum of even-indexed elements with two elements."""
    assert sum_even_indexed_elements([10, 20]) == 10

def test_sum_even_indexed_elements_zero_values():
    """Test sum of even-indexed elements with zero values."""
    assert sum_even_indexed_elements([0, 1, 0, 2, 0]) == 0