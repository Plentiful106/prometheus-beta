import re
from datetime import date
import pytest
from src.date_utils import get_current_date

def test_get_current_date_format():
    """
    Test that the returned date string matches the YYYY-MM-DD format.
    """
    current_date_str = get_current_date()
    
    # Check that the string matches the expected format
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', current_date_str), \
        "Date should be in YYYY-MM-DD format"

def test_get_current_date_matches_today():
    """
    Verify that the returned date matches the current date.
    """
    current_date_str = get_current_date()
    today = date.today().strftime("%Y-%m-%d")
    
    assert current_date_str == today, \
        "Returned date should match today's date"