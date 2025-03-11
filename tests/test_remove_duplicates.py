import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing duplicate characters."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("abracadabra") == "abrcd"
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_case_sensitive():
    """Test that the function is case-sensitive."""
    assert remove_duplicate_chars("AaBbCc") == "AaBbCc"

def test_remove_duplicate_chars_different_types():
    """Test that the function raises a TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)
    with pytest.raises(TypeError):
        remove_duplicate_chars(["hello"])

def test_remove_duplicate_chars_preserves_order():
    """Test that the function preserves the original order of first occurrences."""
    assert remove_duplicate_chars("banana") == "ban"
    assert remove_duplicate_chars("mississippi") == "misp"

def test_remove_duplicate_chars_special_characters():
    """Test handling of special characters and whitespace."""
    assert remove_duplicate_chars("  hello  world  ") == " helowrd"
    assert remove_duplicate_chars("!@#$%^&*()!@#") == "!@#$%^&*()"