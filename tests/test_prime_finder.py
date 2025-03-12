import pytest
from src.prime_finder import find_primes_below_n

def test_find_primes_below_n_basic():
    """Test basic prime number finding."""
    assert find_primes_below_n(10) == [2, 3, 5, 7]

def test_find_primes_below_n_edge_cases():
    """Test edge cases."""
    assert find_primes_below_n(2) == []  # No primes below 2
    assert find_primes_below_n(1) == []  # No primes below 1

def test_find_primes_below_n_larger_range():
    """Test prime finding in a larger range."""
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_below_n_type_error():
    """Test that non-integer inputs raise TypeError."""
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)
    with pytest.raises(TypeError):
        find_primes_below_n("10")
    with pytest.raises(TypeError):
        find_primes_below_n(None)

def test_find_primes_below_n_large_input():
    """Test finding primes in a large range."""
    primes = find_primes_below_n(100)
    # Validate a few known primes
    assert 2 in primes
    assert 3 in primes
    assert 97 in primes
    assert 99 not in primes

def test_find_primes_below_n_zero_and_negative():
    """Test handling of zero and negative inputs."""
    assert find_primes_below_n(0) == []
    assert find_primes_below_n(-5) == []