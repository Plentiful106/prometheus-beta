import pytest
from src.gcd import find_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_zero_cases():
    """Test GCD with zero inputs"""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5
    assert find_gcd(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD with negative numbers"""
    assert find_gcd(-48, 18) == 6
    assert find_gcd(48, -18) == 6
    assert find_gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD when both inputs are the same"""
    assert find_gcd(7, 7) == 7
    assert find_gcd(0, 0) == 0

def test_gcd_type_errors():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError):
        find_gcd(4.5, 3)
    with pytest.raises(TypeError):
        find_gcd(4, '3')
    with pytest.raises(TypeError):
        find_gcd('4', 3)