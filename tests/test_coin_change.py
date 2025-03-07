import pytest
from src.coin_change import min_coins

def test_standard_case():
    """Test a standard case with multiple coin denominations"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2, 3, 5], 8) == 2   # 3 + 5
    assert min_coins([1, 3, 4, 5], 7) == 2  # 3 + 4

def test_no_solution():
    """Test cases where no exact change is possible"""
    assert min_coins([2], 3) == -1
    assert min_coins([2], 1) == -1

def test_zero_amount():
    """Test zero amount case"""
    assert min_coins([1, 2, 5], 0) == 0

def test_single_coin():
    """Test cases with single coin denomination"""
    assert min_coins([1], 10) == 10
    assert min_coins([2], 6) == 3

def test_large_amount():
    """Test larger amounts"""
    assert min_coins([1, 5, 10, 25], 100) == 4  # 25 + 25 + 25 + 25
    assert min_coins([1, 5, 10, 25], 67) == 6   # 25 + 25 + 10 + 5 + 1 + 1

def test_error_handling():
    """Test error cases for invalid inputs"""
    with pytest.raises(ValueError, match="Coins must be a non-empty list"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="Coins must be a non-empty list"):
        min_coins(None, 10)
    
    with pytest.raises(ValueError, match="Amount must be a non-negative integer"):
        min_coins([1, 2, 5], -1)
    
    with pytest.raises(ValueError, match="Amount must be a non-negative integer"):
        min_coins([1, 2, 5], 'abc')
    
    with pytest.raises(ValueError, match="No valid coin denominations provided"):
        min_coins([0, -1, 'a'], 10)

def test_edge_cases():
    """Test more complex edge cases"""
    assert min_coins([2, 3, 5], 1) == -1
    assert min_coins([1, 3, 4, 5], 6) == 2  # 3 + 3
    assert min_coins([2, 3, 5], 0) == 0