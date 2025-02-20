import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    """Test basic case with a common substring"""
    assert longest_common_substring("hello", "world") == ""
    assert longest_common_substring("ABCDGH", "ACDGHR") == "CDGH"
    assert longest_common_substring("programming", "program") == "program"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_substring("python", "python") == "python"

def test_no_common_substring():
    """Test when no common substring exists"""
    assert longest_common_substring("abc", "def") == ""
    assert longest_common_substring("", "test") == ""
    assert longest_common_substring("test", "") == ""

def test_case_sensitivity():
    """Test case sensitivity of substring matching"""
    assert longest_common_substring("Hello", "hello") == ""
    assert longest_common_substring("HeLLo", "hello") == ""
    assert longest_common_substring("HELLO", "hello") == ""

def test_multiple_longest_substrings():
    """Test cases where multiple substrings of same length exist"""
    result = longest_common_substring("xabcde", "abcdxy")
    assert result == "abcd"
    
def test_edge_cases():
    """Test various edge cases"""
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("a", "a") == "a"