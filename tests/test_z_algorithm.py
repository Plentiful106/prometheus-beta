import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert z_algorithm(text, pattern) == [10]

def test_multiple_matches():
    """Test when pattern appears multiple times"""
    text = "AAAAAAAA"
    pattern = "AAA"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_no_matches():
    """Test when pattern is not in text"""
    text = "ABCDEF"
    pattern = "XYZ"
    assert z_algorithm(text, pattern) == []

def test_pattern_equals_text():
    """Test when pattern is the entire text"""
    text = "HELLO"
    pattern = "HELLO"
    assert z_algorithm(text, pattern) == [0]

def test_empty_pattern_raises_error():
    """Test that empty pattern raises ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("TEXT", "")

def test_empty_text_raises_error():
    """Test that empty text raises ValueError"""
    with pytest.raises(ValueError):
        z_algorithm("", "PATTERN")

def test_non_string_inputs():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError):
        z_algorithm(123, "PATTERN")
    
    with pytest.raises(TypeError):
        z_algorithm("TEXT", 456)

def test_case_sensitivity():
    """Test that matching is case-sensitive"""
    text = "abcABCabcABC"
    pattern = "abc"
    assert z_algorithm(text, pattern) == [0, 6]

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "VERYLONGPATTERN"
    assert z_algorithm(text, pattern) == []