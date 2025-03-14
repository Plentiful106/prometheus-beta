import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic_range():
    """Test a basic range of numbers"""
    assert sum_of_multiples(1, 10) == 33  # 2+3+4+6+8+9+10 = 33

def test_sum_of_multiples_single_number():
    """Test when min and max are the same number"""
    assert sum_of_multiples(2, 2) == 2
    assert sum_of_multiples(3, 3) == 3
    assert sum_of_multiples(5, 5) == 0

def test_sum_of_multiples_invalid_range():
    """Test that an error is raised when min > max"""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        sum_of_multiples(10, 5)

def test_sum_of_multiples_zero_range():
    """Test range starting at zero"""
    assert sum_of_multiples(0, 10) == 33

def test_sum_of_multiples_large_range():
    """Test a larger range of numbers"""
    assert sum_of_multiples(1, 1000) == 234168