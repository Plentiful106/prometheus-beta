import pytest
from src.remove_duplicates import remove_duplicates_over_two

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates over two."""
    assert remove_duplicates_over_two("aabbbcccc") == "aabbcc"

def test_remove_duplicates_no_change():
    """Test string with no characters appearing more than twice."""
    assert remove_duplicates_over_two("hello") == "hello"

def test_remove_all_duplicates():
    """Test string with all characters appearing more than twice."""
    assert remove_duplicates_over_two("aaaaabbbbbccccc") == "aabbcc"

def test_empty_string():
    """Test empty string input."""
    assert remove_duplicates_over_two("") == ""

def test_single_character():
    """Test single character input."""
    assert remove_duplicates_over_two("a") == "a"

def test_mixed_duplicates():
    """Test string with mixed duplicate counts."""
    assert remove_duplicates_over_two("aabbccdddeee") == "aabbccddee"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicates_over_two(123)
        remove_duplicates_over_two(None)
        remove_duplicates_over_two(["a", "b", "c"])