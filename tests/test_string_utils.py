import pytest
from src.string_utils import capitalize_words

def test_capitalize_words_basic():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_multiple_words():
    """Test capitalization of multiple words."""
    assert capitalize_words("python programming language") == "Python Programming Language"

def test_capitalize_words_empty_string():
    """Test handling of empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_single_char():
    """Test capitalization of a single character."""
    assert capitalize_words("a") == "A"

def test_capitalize_words_already_capitalized():
    """Test string where words are already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_capitalize_words_extra_whitespace():
    """Test string with extra whitespace."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_non_string_input():
    """Test handling of non-string input."""
    with pytest.raises(AttributeError):
        capitalize_words(123)
    with pytest.raises(AttributeError):
        capitalize_words(None)