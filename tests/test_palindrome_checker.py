import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test well-known palindrome phrases."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_single_word_palindromes():
    """Test single word palindromes."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaCeCaR") == True

def test_edge_cases():
    """Test edge cases including empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!!") == True

def test_numeric_palindromes():
    """Test palindromes with numbers and mixed characters."""
    assert is_palindrome("12321") == True
    assert is_palindrome("1 22 1") == True
    assert is_palindrome("123") == False

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert is_palindrome("A!b@c#c B,a") == True
    assert is_palindrome("Hello, World!") == False