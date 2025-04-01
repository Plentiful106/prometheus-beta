"""
Test suite for custom logging function.
"""

import io
import pytest
from src.custom_logger import log_message


def test_basic_logging():
    """Test basic message logging without styling."""
    output = io.StringIO()
    log_message("Test Message", output=output)
    assert output.getvalue().strip() == "Test Message"


def test_color_logging():
    """Test logging with different colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    for color in colors:
        output = io.StringIO()
        log_message("Colored Message", color=color, output=output)
        colored_message = output.getvalue().strip()
        
        # Check that the message contains ANSI color code
        color_code = f"\033[{31 + colors.index(color)}m"
        assert color_code in colored_message
        assert "Colored Message" in colored_message


def test_text_styling():
    """Test different text styling options."""
    output = io.StringIO()
    log_message("Styled Message", bold=True, italic=True, underline=True, output=output)
    styled_message = output.getvalue().strip()
    
    # Check for bold, italic, and underline ANSI codes
    assert '\033[1m' in styled_message  # bold
    assert '\033[3m' in styled_message  # italic
    assert '\033[4m' in styled_message  # underline
    assert "Styled Message" in styled_message


def test_color_and_styling_combined():
    """Test combining color and text styling."""
    output = io.StringIO()
    log_message("Combined Styling", color='green', bold=True, output=output)
    combined_message = output.getvalue().strip()
    
    # Check for green color and bold styling
    assert '\033[32m' in combined_message  # green
    assert '\033[1m' in combined_message   # bold
    assert "Combined Styling" in combined_message


def test_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_message("Invalid Color", color="purple")


def test_empty_message():
    """Test logging an empty message."""
    output = io.StringIO()
    log_message("", output=output)
    assert output.getvalue().strip() == ""