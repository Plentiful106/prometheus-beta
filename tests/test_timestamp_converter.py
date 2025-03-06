import pytest
from datetime import datetime, timezone
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a standard timestamp"""
    # Timestamp for 2023-01-15 11:10:45 UTC
    timestamp = 1673781045
    assert timestamp_to_human_readable(timestamp) == '2023-01-15 11:10:45 UTC'

def test_float_timestamp():
    """Test conversion of a float timestamp"""
    # Timestamp with decimal part
    timestamp = 1673781045.123
    assert timestamp_to_human_readable(timestamp) == '2023-01-15 11:10:45 UTC'

def test_zero_timestamp():
    """Test conversion of 0 timestamp (Unix epoch start)"""
    assert timestamp_to_human_readable(0) == '1970-01-01 00:00:00 UTC'

def test_future_timestamp():
    """Test conversion of a future timestamp"""
    # Timestamp for 2030-01-01 00:00:00 UTC
    timestamp = 1893456000
    assert timestamp_to_human_readable(timestamp) == '2030-01-01 00:00:00 UTC'

def test_invalid_type_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Timestamp must be a numeric value"):
        timestamp_to_human_readable("not a number")
    
    with pytest.raises(TypeError, match="Timestamp must be a numeric value"):
        timestamp_to_human_readable(None)

def test_out_of_range_timestamp():
    """Test handling of timestamps far outside reasonable range"""
    # Very far past timestamp
    with pytest.raises(ValueError, match="Invalid timestamp"):
        timestamp_to_human_readable(-1000000000000)
    
    # Very far future timestamp
    with pytest.raises(ValueError, match="Invalid timestamp"):
        timestamp_to_human_readable(100000000000000)