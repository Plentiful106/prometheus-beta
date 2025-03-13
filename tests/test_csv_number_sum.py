import pytest
from src.csv_number_sum import sum_csv_numbers

def test_basic_csv_sum():
    """Test summing a simple CSV of numbers."""
    assert sum_csv_numbers('1,2,3') == 6

def test_empty_string():
    """Test that an empty string returns 0."""
    assert sum_csv_numbers('') == 0

def test_single_number():
    """Test a CSV with a single number."""
    assert sum_csv_numbers('42') == 42

def test_numbers_with_spaces():
    """Test CSV with numbers that have surrounding spaces."""
    assert sum_csv_numbers(' 1 , 2 , 3 ') == 6

def test_negative_numbers():
    """Test CSV with negative numbers."""
    assert sum_csv_numbers('-1,2,-3') == -2

def test_invalid_input():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError):
        sum_csv_numbers('1,2,abc')

def test_mixed_invalid_input():
    """Test that a mix of valid and invalid input raises a ValueError."""
    with pytest.raises(ValueError):
        sum_csv_numbers('1,2,3a')