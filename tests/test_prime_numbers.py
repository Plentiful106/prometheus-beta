import pytest
from src.prime_numbers import get_primes_up_to_n

def test_primes_up_to_100():
    """Test prime numbers up to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert get_primes_up_to_n(100) == expected_primes

def test_primes_lower_bound():
    """Test edge cases with lower bound numbers."""
    assert get_primes_up_to_n(1) == []
    assert get_primes_up_to_n(2) == [2]

def test_primes_small_numbers():
    """Test prime numbers in smaller ranges."""
    assert get_primes_up_to_n(10) == [2, 3, 5, 7]
    assert get_primes_up_to_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        get_primes_up_to_n(-5)

def test_zero_input():
    """Test that zero returns an empty list."""
    assert get_primes_up_to_n(0) == []