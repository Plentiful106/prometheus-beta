import pytest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_lis_length

def test_normal_sequence():
    """Test a typical increasing subsequence"""
    assert find_lis_length([10, 22, 9, 33, 21, 50, 41, 60]) == 5

def test_empty_list():
    """Test empty list returns 0"""
    assert find_lis_length([]) == 0

def test_single_element():
    """Test list with single element"""
    assert find_lis_length([42]) == 1

def test_decreasing_sequence():
    """Test a strictly decreasing sequence"""
    assert find_lis_length([5, 4, 3, 2, 1]) == 1

def test_all_same_elements():
    """Test list with all identical elements"""
    assert find_lis_length([3, 3, 3, 3]) == 1

def test_mixed_sequence():
    """Test a mixed sequence"""
    assert find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_floating_point_numbers():
    """Test with floating point numbers"""
    assert find_lis_length([1.5, 2.3, 0.5, 4.1, 2.7]) == 3

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_lis_length([-3, -1, -2, 5, 0, 6, 10]) == 4

def test_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        find_lis_length("not a list")

def test_invalid_list_elements():
    """Test list with non-numeric elements raises ValueError"""
    with pytest.raises(ValueError):
        find_lis_length([1, 2, 'a', 3])