import pytest
from src.word_capitalizer import capitalize_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_already_capitalized():
    """Test string with already capitalized words."""
    assert capitalize_words("Hello World") == "Hello World"

def test_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_single_word():
    """Test single word capitalization."""
    assert capitalize_words("hello") == "Hello"

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(None)

def test_special_characters():
    """Test capitalization with special characters."""
    assert capitalize_words("hello, world!") == "Hello, World!"