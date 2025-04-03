import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from array_average import calculate_min_max_average

def test_basic_functionality():
    """Test with a standard list of numbers"""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_min_max_average(numbers) == 3.5

def test_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, -3, -4, -5, -6]
    assert calculate_min_max_average(numbers) == -3.5

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    numbers = [-10, 2, 0, 5, 8, 12]
    assert calculate_min_max_average(numbers) == 1.5

def test_floating_point_numbers():
    """Test with floating point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_min_max_average(numbers) == 4.0

def test_invalid_list_length():
    """Test error handling for incorrect list length"""
    with pytest.raises(ValueError, match="Input must contain exactly 6 numbers"):
        calculate_min_max_average([1, 2, 3, 4, 5])

def test_non_numeric_input():
    """Test error handling for non-numeric input"""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        calculate_min_max_average([1, 2, 3, 4, 5, 'six'])

def test_non_list_input():
    """Test error handling for non-list input"""
    with pytest.raises(ValueError, match="Input must be a list"):
        calculate_min_max_average("123456")