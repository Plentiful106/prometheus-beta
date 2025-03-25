import pytest
from src.subsequence_validator import can_divide_subsequences

def test_valid_vowel_subsequences():
    assert can_divide_subsequences("aeio") == True
    assert can_divide_subsequences("aeiou") == True

def test_valid_consonant_subsequences():
    assert can_divide_subsequences("bcd") == True
    assert can_divide_subsequences("xyzw") == True

def test_mixed_valid_subsequences():
    assert can_divide_subsequences("aebocido") == False  # This should be False
    assert can_divide_subsequences("aeibocido") == False  # This should be False

def test_invalid_subsequences():
    assert can_divide_subsequences("ab") == False
    assert can_divide_subsequences("abc") == False
    assert can_divide_subsequences("aei") == False
    assert can_divide_subsequences("ae") == False
    assert can_divide_subsequences("iu") == False

def test_edge_cases():
    # Empty string
    assert can_divide_subsequences("") == False
    
    # Single character
    assert can_divide_subsequences("a") == False
    assert can_divide_subsequences("b") == False
    
    # Invalid inputs
    assert can_divide_subsequences("ABC") == False  # Uppercase
    assert can_divide_subsequences("a1b") == False  # Non-letter characters
    assert can_divide_subsequences("123") == False  # Numbers

def test_longer_valid_sequences():
    assert can_divide_subsequences("aaaaooooeeee") == True
    assert can_divide_subsequences("bcdfghjklmnp") == True

def test_complex_valid_sequences():
    assert can_divide_subsequences("bcaeiodfghi") == False  # This should be False