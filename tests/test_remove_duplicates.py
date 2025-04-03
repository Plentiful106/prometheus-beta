import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"
    assert remove_duplicate_chars("mississippi") == "misp"

def test_remove_duplicates_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicates_all_duplicates():
    """Test string with all duplicate characters."""
    assert remove_duplicate_chars("aaaa") == "a"

def test_remove_duplicates_type_error():
    """Test type error handling."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_chars(None)

def test_remove_duplicates_case_error():
    """Test case sensitivity error handling."""
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("Hello")
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("WORLD")
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("MiXeD")