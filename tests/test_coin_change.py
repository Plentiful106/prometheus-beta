import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios."""
    assert min_coins(11, [1, 2, 5]) == 3  # 5 + 5 + 1
    assert min_coins(4, [1, 2, 3]) == 2   # 2 + 2
    assert min_coins(0, [1, 2, 5]) == 0   # No coins needed for 0

def test_impossible_change():
    """Test scenarios where exact change is impossible."""
    assert min_coins(3, [2]) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins(7, [3, 5]) == -1  # Cannot make 7 with 3 and 5 cent coins

def test_single_coin_denomination():
    """Test with single coin denomination."""
    assert min_coins(10, [2]) == 5  # 5 * 2-cent coins
    assert min_coins(7, [1]) == 7   # 7 * 1-cent coins

def test_large_amount():
    """Test with larger amounts."""
    assert min_coins(100, [1, 5, 10, 25]) == 4  # 4 * 25-cent coins
    assert min_coins(93, [1, 5, 10, 25]) == 8   # 3 * 25-cent + 1 * 10-cent + 3 * 1-cent

def test_input_validation():
    """Test input validation."""
    with pytest.raises(ValueError, match="Amount must be non-negative"):
        min_coins(-5, [1, 2, 5])
    
    with pytest.raises(ValueError, match="Coins list cannot be empty"):
        min_coins(10, [])