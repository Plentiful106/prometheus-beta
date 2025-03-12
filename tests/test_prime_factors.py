import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization scenarios."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test prime numbers."""
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(3) == [3]
    assert get_prime_factors(17) == [17]

def test_prime_factors_edge_cases():
    """Test edge cases."""
    assert get_prime_factors(1) == []

def test_prime_factors_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors("not a number")