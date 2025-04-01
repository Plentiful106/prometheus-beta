import pytest
from src.bit_operations import count_set_bits

def test_count_set_bits_positive_numbers():
    """Test set bits counting for positive integers."""
    assert count_set_bits(5) == 2  # Binary: 101
    assert count_set_bits(7) == 3  # Binary: 111
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(0) == 0  # Binary: 0
    assert count_set_bits(1) == 1  # Binary: 1

def test_count_set_bits_negative_numbers():
    """Test set bits counting for negative integers."""
    assert count_set_bits(-5) == 2  # Two's complement representation
    assert count_set_bits(-1) == 32  # All bits set in 32-bit signed integer
    assert count_set_bits(-7) == 2  # Two's complement representation

def test_count_set_bits_large_numbers():
    """Test set bits counting for large integers."""
    assert count_set_bits(2**10 - 1) == 10  # 1023 in decimal
    assert count_set_bits(2**20 - 1) == 20  # Large number with many set bits

def test_count_set_bits_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    
    with pytest.raises(TypeError):
        count_set_bits(None)