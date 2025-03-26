import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_phrase_palindromes():
    """Test palindrome phrases with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123456") == False

def test_mixed_case_palindromes():
    """Test palindromes with mixed case."""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char():
    """Test empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!") == True

def test_non_palindromes():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_characters():
    """Test strings with special characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b@2#2b1a") == True
    assert is_palindrome("a1b2c3") == False

def test_whitespace_handling():
    """Test handling of whitespace."""
    assert is_palindrome("  racecar  ") == True
    assert is_palindrome(" a b c b a ") == True

def test_unicode_characters():
    """Test unicode characters."""
    assert is_palindrome("Madam, I'm Adam") == True