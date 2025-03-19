import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a simple increasing sequence"""
    assert longest_increasing_subsequence([10, 22, 33, 50, 60, 80]) == 6

def test_mixed_sequence():
    """Test a more complex mixed sequence"""
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_empty_array():
    """Test an empty array"""
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    """Test an array with a single element"""
    assert longest_increasing_subsequence([5]) == 1

def test_non_increasing_sequence():
    """Test a sequence with no increasing subsequence"""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_repeated_elements():
    """Test a sequence with repeated elements"""
    assert longest_increasing_subsequence([1, 1, 1, 1, 1]) == 1

def test_negative_numbers():
    """Test a sequence with negative numbers"""
    assert longest_increasing_subsequence([-5, -4, -3, -2, -1]) == 5

def test_mixed_positive_negative():
    """Test a mixed sequence with positive and negative numbers"""
    assert longest_increasing_subsequence([-2, 1, -1, 3, 0, 4, -3, 5]) == 5