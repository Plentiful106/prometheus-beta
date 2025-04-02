import pytest
from src.triangle_number import triangle_number

def test_triangle_numbers():
    """Test known Triangle Numbers"""
    triangle_nums = [6, 28]
    for num in triangle_nums:
        assert triangle_number(num) is True, f"{num} should be a Triangle Number"

def test_non_triangle_numbers():
    """Test known non-Triangle Numbers"""
    non_triangle_nums = [12, 18, 20]
    for num in non_triangle_nums:
        assert triangle_number(num) is False, f"{num} should not be a Triangle Number"

def test_small_triangle_numbers():
    """Test small Triangle Numbers"""
    assert triangle_number(1) is False
    assert triangle_number(3) is False

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        triangle_number(3.14)
    with pytest.raises(TypeError):
        triangle_number("6")
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        triangle_number(0)
    with pytest.raises(ValueError):
        triangle_number(-5)

def test_large_triangle_number():
    """Test a larger Triangle Number"""
    assert triangle_number(496) is True, "496 is a known Triangle Number"