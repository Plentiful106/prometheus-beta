import pytest
from src.factor_counter import count_factors

def test_count_factors_basic():
    """Test basic scenario of counting factors"""
    assert count_factors(12) == 6  # Factors are 1, 2, 3, 4, 6, 12
    assert count_factors(1) == 1   # 1 has only one factor
    assert count_factors(16) == 5  # Factors are 1, 2, 4, 8, 16

def test_count_factors_prime():
    """Test factor counting for prime numbers"""
    assert count_factors(7) == 2   # Prime numbers have 2 factors: 1 and itself
    assert count_factors(11) == 2  # Another prime number example

def test_count_factors_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(-5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_factors(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_factors("12")