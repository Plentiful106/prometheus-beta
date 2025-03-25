import pytest
from src.consecutive_substring_sum import max_consecutive_substring_sum

def test_basic_consecutive_string():
    """Test a basic consecutive string."""
    assert max_consecutive_substring_sum("abcdef") == 21

def test_reverse_consecutive_string():
    """Test a reverse consecutive string."""
    assert max_consecutive_substring_sum("zyx") == 6

def test_mixed_consecutive_string():
    """Test a mixed consecutive string."""
    assert max_consecutive_substring_sum("abc123") == 6

def test_single_character():
    """Test a single character string."""
    assert max_consecutive_substring_sum("a") == ord('a')

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert max_consecutive_substring_sum("aaa") == 3 * ord('a')

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        max_consecutive_substring_sum(123)

def test_empty_string():
    """Test that a ValueError is raised for an empty string."""
    with pytest.raises(ValueError):
        max_consecutive_substring_sum("")

def test_numeric_consecutive():
    """Test consecutive numeric characters."""
    assert max_consecutive_substring_sum("1234") == 10

def test_ascii_consecutive():
    """Test consecutive ASCII characters with large gaps."""
    assert max_consecutive_substring_sum("AZ") == ord('A') + ord('Z')

def test_mixed_types_consecutive():
    """Test consecutive characters of different types."""
    assert max_consecutive_substring_sum("a1b") == 2