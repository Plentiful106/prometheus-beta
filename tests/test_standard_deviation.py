import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_basic():
    """Test standard deviation for a simple list of numbers."""
    numbers = [2, 4, 4, 4, 5, 5, 7, 9]
    assert math.isclose(calculate_standard_deviation(numbers), 2.0, rel_tol=1e-9)

def test_standard_deviation_single_value():
    """Test standard deviation for a single value (should be zero)."""
    numbers = [5]
    assert calculate_standard_deviation(numbers) == 0.0

def test_standard_deviation_zero_values():
    """Test standard deviation for a list of all zeros."""
    numbers = [0, 0, 0, 0]
    assert calculate_standard_deviation(numbers) == 0.0

def test_standard_deviation_float_values():
    """Test standard deviation with float values."""
    numbers = [1.5, 2.5, 3.5, 4.5]
    assert math.isclose(calculate_standard_deviation(numbers), 1.2909944487358056, rel_tol=1e-9)

def test_standard_deviation_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_standard_deviation_non_numeric():
    """Test that non-numeric values raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation([1, 2, '3', 4])

def test_standard_deviation_mixed_numeric_types():
    """Test standard deviation with mixed numeric types."""
    numbers = [1, 2, 3, 4.0, 5]
    assert math.isclose(calculate_standard_deviation(numbers), 1.5811388300841898, rel_tol=1e-9)