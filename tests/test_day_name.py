import pytest
from datetime import datetime
from src.day_name import get_day_name

def test_get_day_name_datetime():
    """Test getting day name from a datetime object"""
    date = datetime(2023, 6, 15)  # This is a Thursday
    assert get_day_name(date) == 'Thursday'

def test_get_day_name_iso_string():
    """Test getting day name from an ISO formatted date string"""
    assert get_day_name('2023-06-15') == 'Thursday'

def test_get_day_name_us_format():
    """Test getting day name from US formatted date string"""
    assert get_day_name('06/15/2023') == 'Thursday'

def test_get_day_name_uk_format():
    """Test getting day name from UK formatted date string"""
    assert get_day_name('15/06/2023') == 'Thursday'

def test_invalid_date_string():
    """Test handling of invalid date string"""
    with pytest.raises(ValueError):
        get_day_name('invalid-date')

def test_none_input():
    """Test handling of None input"""
    with pytest.raises(ValueError):
        get_day_name(None)

def test_invalid_input_type():
    """Test handling of invalid input type"""
    with pytest.raises(ValueError):
        get_day_name(123)  # Integer input

def test_different_days():
    """Test different days of the week"""
    test_cases = [
        (datetime(2023, 6, 12), 'Monday'),    # Monday
        (datetime(2023, 6, 13), 'Tuesday'),   # Tuesday
        (datetime(2023, 6, 14), 'Wednesday'), # Wednesday
        (datetime(2023, 6, 15), 'Thursday'),  # Thursday
        (datetime(2023, 6, 16), 'Friday'),    # Friday
        (datetime(2023, 6, 17), 'Saturday'),  # Saturday
        (datetime(2023, 6, 18), 'Sunday')     # Sunday
    ]
    
    for date, expected_day in test_cases:
        assert get_day_name(date) == expected_day