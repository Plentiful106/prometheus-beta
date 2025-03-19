import pytest
from src.left_product_array import left_product_array

def test_normal_case():
    """Test a standard case of left product array."""
    assert left_product_array([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_empty_list():
    """Test an empty input list."""
    assert left_product_array([]) == []

def test_single_element():
    """Test a list with a single element."""
    assert left_product_array([5]) == [1]

def test_two_elements():
    """Test a list with two elements."""
    assert left_product_array([2, 3]) == [1, 2]

def test_float_inputs():
    """Test inputs with float values."""
    assert left_product_array([1.5, 2.0, 3.0]) == [1, 1.5, 3.0]

def test_invalid_input_type():
    """Test that a non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        left_product_array("not a list")

def test_non_numeric_input():
    """Test that a list with non-numeric elements raises ValueError."""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        left_product_array([1, 2, "3", 4])

def test_zero_in_list():
    """Test a list containing zero."""
    assert left_product_array([1, 0, 2, 3]) == [1, 1, 0, 0]

def test_negative_numbers():
    """Test a list with negative numbers."""
    assert left_product_array([-1, 2, 3, -4]) == [1, -1, -2, -6]