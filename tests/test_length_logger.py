import pytest
import logging
from src.length_logger import log_length

def test_log_length_string(caplog):
    """Test logging length of a string."""
    caplog.set_level(logging.INFO)
    result = log_length("hello")
    assert result == 5
    assert "Length of input: 5" in caplog.text

def test_log_length_list(caplog):
    """Test logging length of a list."""
    caplog.set_level(logging.INFO)
    result = log_length([1, 2, 3, 4])
    assert result == 4
    assert "Length of input: 4" in caplog.text

def test_log_length_tuple(caplog):
    """Test logging length of a tuple."""
    caplog.set_level(logging.INFO)
    result = log_length((1, 2, 3))
    assert result == 3
    assert "Length of input: 3" in caplog.text

def test_log_length_empty_string(caplog):
    """Test logging length of an empty string."""
    caplog.set_level(logging.INFO)
    result = log_length("")
    assert result == 0
    assert "Length of input: 0" in caplog.text

def test_log_length_empty_list(caplog):
    """Test logging length of an empty list."""
    caplog.set_level(logging.INFO)
    result = log_length([])
    assert result == 0
    assert "Length of input: 0" in caplog.text

def test_log_length_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string or a sequence"):
        log_length(123)  # Integer is not a valid input
    
    with pytest.raises(TypeError, match="Input must be a string or a sequence"):
        log_length(None)  # None is not a valid input