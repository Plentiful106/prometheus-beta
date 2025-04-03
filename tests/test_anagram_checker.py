import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("rail safety", "fairy tales") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert anagram_checker("Tea", "Eat") == True
    assert anagram_checker("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test handling of whitespace in inputs"""
    assert anagram_checker("debit card", "bad credit") == True
    assert anagram_checker(" listen ", "silent") == True

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        anagram_checker(123, "hello")
    
    with pytest.raises(TypeError):
        anagram_checker("hello", ["not", "a", "string"])
    
    with pytest.raises(ValueError):
        anagram_checker("", "hello")
    
    with pytest.raises(ValueError):
        anagram_checker("hello", "")

def test_single_character():
    """Test single character anagrams"""
    assert anagram_checker("a", "a") == True

def test_unicode_characters():
    """Test handling of unicode characters"""
    assert anagram_checker("résumé", "émuser") == True
    assert anagram_checker("café", "face") == False