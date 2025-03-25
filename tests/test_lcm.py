import pytest
from src.lcm import lcm, gcd

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_gcd_zero():
    """Test GCD with zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative():
    """Test GCD with negative numbers"""
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 23) == 391

def test_lcm_zero():
    """Test LCM with zero"""
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0

def test_lcm_one():
    """Test LCM with one"""
    assert lcm(1, 5) == 5
    assert lcm(5, 1) == 5

def test_lcm_negative():
    """Test LCM with negative numbers"""
    assert lcm(-4, 6) == 12
    assert lcm(4, -6) == 12
    assert lcm(-4, -6) == 12

def test_lcm_invalid_input():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        lcm('a', 5)
    with pytest.raises(ValueError):
        lcm(5, 'b')
    with pytest.raises(ValueError):
        lcm([], {})

def test_lcm_both_zero():
    """Test LCM when both inputs are zero"""
    with pytest.raises(ZeroDivisionError):
        lcm(0, 0)