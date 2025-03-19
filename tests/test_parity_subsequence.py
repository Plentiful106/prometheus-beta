import pytest
from src.parity_subsequence import longest_parity_subsequence

def test_empty_array():
    """Test that an empty array returns an empty list."""
    assert longest_parity_subsequence([]) == []

def test_all_even_array():
    """Test an array with only even numbers."""
    assert longest_parity_subsequence([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_all_odd_array():
    """Test an array with only odd numbers."""
    assert longest_parity_subsequence([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_mixed_array_with_longer_even_subsequence():
    """Test a mixed array where the even subsequence is longer."""
    assert longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6]

def test_mixed_array_with_longer_odd_subsequence():
    """Test a mixed array where the odd subsequence is longer."""
    assert longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]

def test_mixed_array_with_equal_subsequences():
    """Test a mixed array with equal even and odd subsequences."""
    result = longest_parity_subsequence([1, 2, 3, 4, 5, 6])
    assert result == [1, 3, 5] or result == [2, 4, 6]

def test_single_element_even():
    """Test a single even element."""
    assert longest_parity_subsequence([2]) == [2]

def test_single_element_odd():
    """Test a single odd element."""
    assert longest_parity_subsequence([1]) == [1]