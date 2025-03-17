import pytest
from src.find_minimum import find_minimum

def test_find_minimum_basic():
    """Test finding minimum in a simple array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([3]) == 3

def test_find_minimum_mixed_numbers():
    """Test finding minimum with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1]) == -1
    assert find_minimum([-5, -4, -3, -2, -1]) == -5
    assert find_minimum([10, -10, 5, -5]) == -10

def test_find_minimum_floating_point():
    """Test finding minimum with floating point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 3.7]) == 0.1
    assert find_minimum([-1.5, -2.3, -0.1, -3.7]) == -3.7

def test_find_minimum_error_cases():
    """Test error handling for invalid inputs."""
    # Empty array
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])
    
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    
    # List with non-numeric elements
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "3", 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None, 4])