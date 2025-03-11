import pytest
from src.prime_numbers import get_primes_to_hundred

def test_get_primes_to_hundred():
    """
    Test the get_primes_to_hundred function.
    
    Checks:
    1. Correct number of primes
    2. Correct prime numbers
    3. Primes are in ascending order
    4. No primes outside the range
    """
    primes = get_primes_to_hundred()
    
    # Expected prime numbers from 1 to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    # Check total number of primes
    assert len(primes) == len(expected_primes), "Incorrect number of prime numbers"
    
    # Check each prime number
    assert primes == expected_primes, "Incorrect prime numbers"
    
    # Check range
    assert all(2 <= p <= 100 for p in primes), "Primes outside the valid range"
    
    # Check sorting
    assert primes == sorted(primes), "Primes not in ascending order"

def test_edge_cases():
    """
    Test edge cases for prime number generation.
    """
    primes = get_primes_to_hundred()
    
    # Check first and last prime
    assert primes[0] == 2, "First prime should be 2"
    assert primes[-1] == 97, "Last prime should be 97"
    
    # Verify no even primes except 2
    assert len([p for p in primes if p % 2 == 0]) == 1, "More than one even prime"