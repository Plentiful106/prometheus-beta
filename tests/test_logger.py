import pytest
import sys
from io import StringIO
import src.logger as logger

def test_log_bold_normal_message(capsys):
    """Test logging a normal message in bold."""
    result = logger.log_bold("Hello, World!")
    captured = capsys.readouterr()
    
    # Check the printed output contains ANSI bold codes
    assert "\033[1mHello, World!\033[0m" in captured.out
    assert result == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_message():
    """Test that an empty message raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        logger.log_bold("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        logger.log_bold("   ")

def test_log_bold_non_string_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        logger.log_bold(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        logger.log_bold(None)

def test_log_bold_special_characters(capsys):
    """Test logging a message with special characters."""
    result = logger.log_bold("Hello, @#$%^&*()!")
    captured = capsys.readouterr()
    
    assert "\033[1mHello, @#$%^&*()!\033[0m" in captured.out
    assert result == "\033[1mHello, @#$%^&*()!\033[0m"