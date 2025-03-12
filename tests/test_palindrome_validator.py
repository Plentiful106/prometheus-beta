import pytest
from src.palindrome_validator import is_palindrome

def test_standard_palindromes():
    """Test classic palindrome strings"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_empty_and_single_char():
    """Test edge cases with empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_case_and_punctuation():
    """Test palindromes with mixed case and punctuation"""
    assert is_palindrome("Madam, I'm Adam.") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("hello world") == False

def test_special_characters():
    """Test strings with various special characters"""
    assert is_palindrome("a!b@c#c@b!a") == True
    assert is_palindrome("a!b@c#d$e") == False

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert is_palindrome("  racecar  ") == True
    assert is_palindrome(" no lemon, no melon ") == True