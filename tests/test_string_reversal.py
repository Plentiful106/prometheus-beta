import pytest
from src.string_reversal import recursive_reverse_string

def test_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse_string("") == ""

def test_single_character():
    """Test reversing a single character string."""
    assert recursive_reverse_string("a") == "a"

def test_normal_string():
    """Test reversing a normal string."""
    assert recursive_reverse_string("hello") == "olleh"

def test_palindrome():
    """Test reversing a palindrome."""
    assert recursive_reverse_string("racecar") == "racecar"

def test_string_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_mixed_characters():
    """Test reversing a string with mixed characters."""
    assert recursive_reverse_string("a1b2c3") == "3c2b1a"

def test_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(None)