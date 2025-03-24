import pytest
from src.remove_duplicates import remove_duplicate_characters

def test_remove_duplicate_characters_basic():
    """Test basic string with duplicate characters."""
    assert remove_duplicate_characters("hello") == "helo"
    assert remove_duplicate_characters("aabbcc") == "abc"

def test_remove_duplicate_characters_preserve_order():
    """Ensure first occurrence of characters is preserved."""
    assert remove_duplicate_characters("abcabcabc") == "abc"
    assert remove_duplicate_characters("hello world") == "helo wrd"

def test_remove_duplicate_characters_empty_string():
    """Test empty string input."""
    assert remove_duplicate_characters("") == ""

def test_remove_duplicate_characters_single_character():
    """Test string with a single character."""
    assert remove_duplicate_characters("a") == "a"

def test_remove_duplicate_characters_all_unique():
    """Test string with all unique characters."""
    assert remove_duplicate_characters("abcdef") == "abcdef"

def test_remove_duplicate_characters_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_characters(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_characters(None)