import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_basic_zero_sum_pairs():
    """Test basic functionality of counting zero-sum pairs."""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2
    assert count_zero_sum_pairs([]) == 0
    assert count_zero_sum_pairs([0, 0, 0]) == 1

def test_multiple_pairs():
    """Test scenarios with multiple zero-sum pairs."""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3, -3, 4, -4]) == 4

def test_no_zero_sum_pairs():
    """Test when no zero-sum pairs exist."""
    assert count_zero_sum_pairs([1, 2, 3, 4, 5]) == 0

def test_input_validation():
    """Test input validation and error handling."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_zero_sum_pairs("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_zero_sum_pairs(None)

def test_invalid_elements():
    """Test handling of non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        count_zero_sum_pairs([1, 2, "3"])
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        count_zero_sum_pairs([1, 2, 3.14])