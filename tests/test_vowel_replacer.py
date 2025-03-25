import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_lowercase():
    """Test vowel replacement for lowercase string."""
    assert replace_vowels("hello") == "hulli"
    assert replace_vowels("python") == "pythun"

def test_replace_vowels_uppercase():
    """Test vowel replacement for uppercase string."""
    assert replace_vowels("HELLO") == "HULLI"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_mixed_case():
    """Test vowel replacement for mixed case string."""
    assert replace_vowels("HeLLo") == "HuLLi"

def test_replace_vowels_no_vowels():
    """Test string with no vowels."""
    assert replace_vowels("rhythm") == "rhythm"

def test_replace_vowels_empty_string():
    """Test empty string input."""
    assert replace_vowels("") == ""

def test_replace_vowels_special_characters():
    """Test string with special characters and numbers."""
    assert replace_vowels("h3ll0!") == "h3ll0!"
    assert replace_vowels("a1e2i3o4u5") == "e1i2o3u4a5"