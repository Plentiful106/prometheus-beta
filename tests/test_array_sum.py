import pytest
from src.array_sum import calculate_array_sum

def test_sum_of_positive_integers():
    """Test sum of positive integers."""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_of_negative_integers():
    """Test sum of negative integers."""
    assert calculate_array_sum([-1, -2, -3, -4, -5]) == -15

def test_sum_of_mixed_numbers():
    """Test sum of mixed positive and negative numbers."""
    assert calculate_array_sum([-1, 0, 1, 2, 3]) == 5

def test_sum_of_floats():
    """Test sum of floating-point numbers."""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_empty_array():
    """Test sum of an empty array."""
    assert calculate_array_sum([]) == 0

def test_single_element_array():
    """Test sum of a single-element array."""
    assert calculate_array_sum([42]) == 42

def test_invalid_input_not_list():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_invalid_input_non_numeric():
    """Test that array with non-numeric elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "3", 4])
        
def test_mixed_numeric_types():
    """Test sum of mixed numeric types (int and float)."""
    assert calculate_array_sum([1, 2.5, 3, 4.5]) == 11.0