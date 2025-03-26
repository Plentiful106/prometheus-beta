import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_sensitive():
    """Ensure function is case-sensitive."""
    assert is_palindrome("RaceCar") == False
    assert is_palindrome("Racecar") == False

def test_empty_and_single_char():
    """Test edge cases of empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("z") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_and_special_chars():
    """Test palindromes with numbers and special characters."""
    assert is_palindrome("1221") == True
    assert is_palindrome("a1b2c2b1a") == True
    assert is_palindrome("!11!") == True
    assert is_palindrome("a1b2c") == False

def test_whitespace():
    """Ensure whitespace is considered in palindrome check."""
    assert is_palindrome("race car") == False
    assert is_palindrome("a ") == False