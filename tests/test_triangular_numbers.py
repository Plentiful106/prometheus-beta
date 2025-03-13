import pytest
from src.triangular_numbers import count_triangular_numbers

def test_triangular_numbers_zero():
    """Test count of triangular numbers for 0."""
    assert count_triangular_numbers(0) == 0

def test_triangular_numbers_small_numbers():
    """Test count of triangular numbers for small values."""
    test_cases = [
        (1, 1),    # First triangular number
        (3, 2),    # First two triangular numbers (1, 3)
        (6, 3),    # First three triangular numbers (1, 3, 6)
        (10, 4),   # First four triangular numbers (1, 3, 6, 10)
    ]
    
    for n, expected in test_cases:
        assert count_triangular_numbers(n) == expected

def test_triangular_numbers_larger_values():
    """Test count of triangular numbers for larger values."""
    test_cases = [
        (15, 5),   # First five triangular numbers (1, 3, 6, 10, 15)
        (21, 6),   # First six triangular numbers (1, 3, 6, 10, 15, 21)
        (100, 13)  # Count up to 100
    ]
    
    for n, expected in test_cases:
        assert count_triangular_numbers(n) == expected

def test_invalid_inputs():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        count_triangular_numbers(3.14)
    
    with pytest.raises(TypeError):
        count_triangular_numbers("10")
    
    with pytest.raises(ValueError):
        count_triangular_numbers(-1)
    
    with pytest.raises(TypeError):
        count_triangular_numbers(None)