import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days_from_date

def test_subtract_days_basic():
    """Test basic day subtraction"""
    original_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(original_date, 5)
    assert result == datetime(2023, 6, 10)

def test_subtract_days_across_month():
    """Test subtraction across month boundary"""
    original_date = datetime(2023, 3, 10)
    result = subtract_days_from_date(original_date, 15)
    assert result == datetime(2023, 2, 23)

def test_subtract_days_zero():
    """Test subtracting zero days"""
    original_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(original_date, 0)
    assert result == original_date

def test_invalid_input_negative_days():
    """Test that negative days raise a ValueError"""
    original_date = datetime(2023, 6, 15)
    with pytest.raises(ValueError, match="Number of days to subtract must be non-negative"):
        subtract_days_from_date(original_date, -5)

def test_invalid_input_non_datetime():
    """Test that non-datetime first argument raises TypeError"""
    with pytest.raises(TypeError, match="First argument must be a datetime object"):
        subtract_days_from_date("2023-06-15", 5)

def test_invalid_input_non_integer_days():
    """Test that non-integer days argument raises TypeError"""
    original_date = datetime(2023, 6, 15)
    with pytest.raises(TypeError, match="Days must be an integer"):
        subtract_days_from_date(original_date, "5")

def test_leap_year_subtraction():
    """Test subtraction during a leap year"""
    original_date = datetime(2024, 3, 1)
    result = subtract_days_from_date(original_date, 1)
    assert result == datetime(2024, 2, 29)  # Check leap day handling