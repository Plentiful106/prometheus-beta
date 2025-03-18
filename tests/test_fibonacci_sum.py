import pytest
from src.fibonacci_sum import fibonacci_sequence_sum

def test_fibonacci_sequence_sum_basic():
    """Test basic functionality of fibonacci_sequence_sum"""
    assert fibonacci_sequence_sum(1) == 0  # First term is 0
    assert fibonacci_sequence_sum(2) == 1  # 0 + 1
    assert fibonacci_sequence_sum(3) == 2  # 0 + 1 + 1
    assert fibonacci_sequence_sum(5) == 7  # 0 + 1 + 1 + 2 + 3

def test_fibonacci_sequence_sum_larger_n():
    """Test sum for larger values of n"""
    assert fibonacci_sequence_sum(10) == 88  # Verified sum of first 10 Fibonacci numbers

def test_fibonacci_sequence_sum_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sequence_sum("not a number")