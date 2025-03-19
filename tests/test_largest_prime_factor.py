import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_prime_number():
    """Test that a prime number returns itself"""
    assert find_largest_prime_factor(17) == 17

def test_composite_number():
    """Test a composite number with multiple prime factors"""
    assert find_largest_prime_factor(84) == 7

def test_large_number():
    """Test a large number with a large prime factor"""
    assert find_largest_prime_factor(13195) == 29

def test_power_of_two():
    """Test a power of two"""
    assert find_largest_prime_factor(16) == 2

def test_very_large_number():
    """Test a very large number"""
    assert find_largest_prime_factor(600851475143) == 6857

def test_invalid_input_less_than_two():
    """Test that an error is raised for inputs less than 2"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-5)

def test_non_integer_input():
    """Test that an error is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        find_largest_prime_factor(3.14)
    
    with pytest.raises(TypeError):
        find_largest_prime_factor("123")
    
    with pytest.raises(TypeError):
        find_largest_prime_factor(None)