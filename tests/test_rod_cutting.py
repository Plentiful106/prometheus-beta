import pytest
from src.rod_cutting import rod_cutting

def test_basic_rod_cutting():
    """Test a basic scenario of rod cutting"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10

def test_maximum_revenue():
    """Test finding maximum revenue for entire rod"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 20

def test_single_length():
    """Test rod cutting for a single length"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_zero_length():
    """Test rod of zero length returns zero revenue"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_error_empty_prices():
    """Test that an empty prices list raises ValueError"""
    with pytest.raises(ValueError, match="Prices list cannot be empty"):
        rod_cutting([], 5)

def test_error_negative_length():
    """Test that a negative rod length raises ValueError"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    with pytest.raises(ValueError, match="Rod length cannot be negative"):
        rod_cutting(prices, -1)

def test_short_price_list():
    """Test when prices list is shorter than rod length"""
    prices = [1, 5, 8]
    assert rod_cutting(prices, 4) == 10  # Use available prices optimally

def test_large_rod_length():
    """Test rod cutting with length larger than price list"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 10) == 30  # Use available prices optimally