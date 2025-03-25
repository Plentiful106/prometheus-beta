import pytest
from src.subsequence_validator import can_divide_subsequences

def test_valid_vowel_subsequences():
    assert can_divide_subsequences("aeio") == True
    assert can_divide_subsequences("aeiou") == True

def test_valid_consonant_subsequences():
    assert can_divide_subsequences("bcd") == True
    assert can_divide_subsequences("xyzw") == True

def test_mixed_valid_subsequences():
    assert can_divide_subsequences("aebocido") == False  # Cannot mix vowels and consonants
    assert can_divide_subsequences("aeibocido") == False  # Cannot mix vowels and consonants

def test_invalid_subsequences():
    assert can_divide_subsequences("ab") == False
    assert can_divide_subsequences("abc") == False
    assert can_divide_subsequences("aei") == False  # Needs to divide into 2+ letter groups
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

def test_complex_sequences():
    assert can_divide_subsequences("bcaeiodfghi") == False  # Cannot mix subsequences