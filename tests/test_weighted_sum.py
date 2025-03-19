import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert compute_weighted_sum(numbers, weights) == 1*0.5 + 2*1 + 3*1.5

def test_single_element():
    """Test weighted sum with a single element."""
    numbers = [10]
    weights = [2]
    assert compute_weighted_sum(numbers, weights) == 20

def test_floating_point_values():
    """Test weighted sum with floating point numbers."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.1, 0.2, 0.3]
    expected = 1.5*0.1 + 2.5*0.2 + 3.5*0.3
    assert compute_weighted_sum(numbers, weights) == pytest.approx(expected)

def test_unequal_lengths_raises_error():
    """Test that unequal list lengths raise a ValueError."""
    with pytest.raises(ValueError, match="lists must have equal length"):
        compute_weighted_sum([1, 2], [1, 2, 3])

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        compute_weighted_sum([], [])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        compute_weighted_sum(1, 2)

def test_non_numeric_input_raises_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        compute_weighted_sum([1, 'a'], [1, 2])

def test_zero_weights():
    """Test weighted sum with zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 0, 0]
    assert compute_weighted_sum(numbers, weights) == 0

def test_negative_values():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [1, -0.5, 0.5]
    expected = -1*1 + 2*(-0.5) + (-3)*0.5
    assert compute_weighted_sum(numbers, weights) == expected