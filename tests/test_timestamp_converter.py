import pytest
from datetime import datetime
from src.timestamp_converter import convert_timestamp_to_readable_date

def test_valid_timestamp():
    """Test conversion of a standard timestamp."""
    timestamp = 1609459200  # January 1, 2021 00:00:00 UTC
    assert convert_timestamp_to_readable_date(timestamp) == "January 01, 2021"

def test_float_timestamp():
    """Test conversion of a float timestamp."""
    timestamp = 1609459200.123
    assert convert_timestamp_to_readable_date(timestamp) == "January 01, 2021"

def test_recent_timestamp():
    """Test conversion of a recent timestamp."""
    current_timestamp = int(datetime.now().timestamp())
    result = convert_timestamp_to_readable_date(current_timestamp)
    assert isinstance(result, str)
    assert len(result) > 0

def test_invalid_type_raises_error():
    """Test that non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        convert_timestamp_to_readable_date("not a number")

def test_negative_timestamp_raises_error():
    """Test that negative timestamp raises ValueError."""
    with pytest.raises(ValueError):
        convert_timestamp_to_readable_date(-1000)

def test_extreme_future_timestamp():
    """Test very large timestamp to ensure no overflow."""
    extreme_timestamp = 2**50  # A very large timestamp
    with pytest.raises(ValueError):
        convert_timestamp_to_readable_date(extreme_timestamp)