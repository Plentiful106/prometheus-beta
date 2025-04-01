"""
Unit tests for the error logging function.
"""

import pytest
import io
import sys

from src.error_logger import log_error

def test_log_error_normal_message(capsys):
    """Test logging a normal error message."""
    log_error("Test error message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "ERROR: Test error message"

def test_log_error_with_special_characters(capsys):
    """Test logging an error message with special characters."""
    log_error("Error with !@#$%^&* special chars")
    captured = capsys.readouterr()
    assert captured.out.strip() == "ERROR: Error with !@#$%^&* special chars"

def test_log_error_non_string_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)
    
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(None)

def test_log_error_empty_string():
    """Test that ValueError is raised for empty string."""
    with pytest.raises(ValueError, match="Error message cannot be empty"):
        log_error("")
    
    with pytest.raises(ValueError, match="Error message cannot be empty"):
        log_error("   ")  # Whitespace-only string