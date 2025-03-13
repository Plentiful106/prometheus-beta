import pytest
from src.prime_filter import is_prime, filter_primes

def test_is_prime():
    """Test the is_prime function for various scenarios."""
    # Known prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    
    # Known non-prime numbers
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

def test_is_prime_type_error():
    """Test that is_prime raises TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        is_prime("2")
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime(None)

def test_filter_primes():
    """Test the filter_primes function with various input scenarios."""
    # Basic filtering
    assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
    
    # Empty list
    assert filter_primes([]) == []
    
    # List with no primes
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []
    
    # List with only primes
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_filter_primes_type_errors():
    """Test that filter_primes raises appropriate type errors."""
    # Non-list input
    with pytest.raises(TypeError):
        filter_primes("not a list")
    
    # List with non-integer elements
    with pytest.raises(TypeError):
        filter_primes([1, 2, "3", 4])
    with pytest.raises(TypeError):
        filter_primes([1, 2, 3.14, 4])
    with pytest.raises(TypeError):
        filter_primes([1, 2, None, 4])