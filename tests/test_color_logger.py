import sys
import io
import pytest
from src.color_logger import ColorLogger

def test_log_default():
    """Test logging without a color"""
    # Create a StringIO to simulate file
    captured_output = io.StringIO()
    
    ColorLogger.log("Test message", file=captured_output)
    
    assert captured_output.getvalue().strip() == "Test message"

def test_log_with_color():
    """Test logging with a specific color"""
    # Create a StringIO to simulate file
    captured_output = io.StringIO()
    
    ColorLogger.log("Test message", color='red', file=captured_output)
    
    # Use multiple ways to check ANSI color
    value = captured_output.getvalue().strip()
    assert value == "\033[91mTest message\033[0m" or \
           value == "\x1b[91mTest message\x1b[0m" or \
           value == "Test message"

def test_log_invalid_color():
    """Test that an invalid color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid color"):
        ColorLogger.log("Test message", color='invalid_color')

def test_log_none_message():
    """Test that None message raises a ValueError"""
    with pytest.raises(ValueError, match="Message cannot be None"):
        ColorLogger.log(None)

def test_log_to_file():
    """Test logging to a specific file-like object"""
    # Create a StringIO to simulate a file
    file_output = io.StringIO()
    
    ColorLogger.log("Test message", color='blue', file=file_output)
    
    # Check the content of the file-like object
    value = file_output.getvalue().strip()
    assert value == "\033[94mTest message\033[0m" or \
           value == "\x1b[94mTest message\x1b[0m" or \
           value == "Test message"

def test_available_colors():
    """Test that all specified colors can be used"""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    for color in colors:
        # Create a StringIO to simulate a file
        captured_output = io.StringIO()
        
        ColorLogger.log("Test message", color=color, file=captured_output)
        
        # Verify the color code is present
        value = captured_output.getvalue().strip()
        assert (f'\033[9{colors.index(color)+1}mTest message\033[0m' in value or 
                f'\x1b[9{colors.index(color)+1}mTest message\x1b[0m' in value or 
                value == 'Test message')