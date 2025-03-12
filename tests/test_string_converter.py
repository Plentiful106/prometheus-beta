import pytest
from src.string_converter import convert_to_upper_with_spaces

def test_convert_to_upper_with_spaces_basic():
    """Test basic string conversion to uppercase with spaces."""
    assert convert_to_upper_with_spaces("hello world") == "HELLO WORLD"

def test_convert_to_upper_with_spaces_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert convert_to_upper_with_spaces("hello   world") == "HELLO WORLD"

def test_convert_to_upper_with_spaces_leading_trailing_spaces():
    """Test handling of leading and trailing spaces."""
    assert convert_to_upper_with_spaces("  hello world  ") == "HELLO WORLD"

def test_convert_to_upper_with_spaces_single_word():
    """Test conversion of a single word."""
    assert convert_to_upper_with_spaces("hello") == "HELLO"

def test_convert_to_upper_with_spaces_empty_string():
    """Test handling of empty string."""
    assert convert_to_upper_with_spaces("") == ""

def test_convert_to_upper_with_spaces_non_string_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_with_spaces(None)