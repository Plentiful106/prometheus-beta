import pytest
from src.vowel_reversal import reverse_vowels_in_substring

def test_basic_vowel_reversal():
    assert reverse_vowels_in_substring("hello world", 0, 5) == "holle world"
    assert reverse_vowels_in_substring("python programming", 7, 17) == "python prigrammong"

def test_no_vowels_in_substring():
    assert reverse_vowels_in_substring("hello world", 6, 11) == "hello world"

def test_all_vowels_in_substring():
    assert reverse_vowels_in_substring("aeiou", 0, 5) == "uoiea"

def test_mixed_case_vowels():
    assert reverse_vowels_in_substring("AeIoU", 0, 5) == "UoIeA"

def test_partial_substring_vowel_reversal():
    assert reverse_vowels_in_substring("hello world python", 0, 11) == "hollo werld python"

def test_invalid_indices():
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 5, 2)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 5)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 0, 6)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        reverse_vowels_in_substring(12345, 0, 5)

def test_edge_cases():
    # Empty string
    assert reverse_vowels_in_substring("", 0, 0) == ""
    
    # Single character strings
    assert reverse_vowels_in_substring("a", 0, 1) == "a"
    assert reverse_vowels_in_substring("b", 0, 1) == "b"

    # Substring at start
    assert reverse_vowels_in_substring("hello world", 0, 1) == "hello world"

    # Substring at end
    assert reverse_vowels_in_substring("hello world", 10, 11) == "hello world"