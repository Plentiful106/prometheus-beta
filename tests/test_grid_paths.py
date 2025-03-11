import pytest
from src.grid_paths import count_unique_paths

def test_standard_grid_sizes():
    """Test unique paths for various standard grid sizes"""
    assert count_unique_paths(2, 2) == 2
    assert count_unique_paths(3, 3) == 6
    assert count_unique_paths(3, 7) == 28

def test_single_row_column():
    """Test grids with single row or column"""
    assert count_unique_paths(1, 5) == 1
    assert count_unique_paths(5, 1) == 1

def test_large_grid():
    """Test larger grid dimensions"""
    assert count_unique_paths(10, 10) == 48620

def test_invalid_grid_dimensions():
    """Test error handling for invalid grid dimensions"""
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(0, 5)
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(5, 0)
    with pytest.raises(ValueError, match="Grid dimensions must be positive integers"):
        count_unique_paths(-1, 5)