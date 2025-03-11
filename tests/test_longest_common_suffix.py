import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_common_suffix_exists():
    """Test finding a common suffix that exists."""
    strings = ["flower", "tower", "power"]
    assert find_longest_common_suffix(strings) == "wer"

def test_full_word_common_suffix():
    """Test when entire word is the common suffix."""
    strings = ["hello", "bello", "cello"]
    assert find_longest_common_suffix(strings) == "ello"

def test_single_string():
    """Test with a single string."""
    strings = ["hello"]
    assert find_longest_common_suffix(strings) == "hello"

def test_no_common_suffix():
    """Test when no common suffix exists."""
    strings = ["abc", "def", "ghi"]
    assert find_longest_common_suffix(strings) == ""

def test_empty_string_list():
    """Test raising ValueError for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_common_suffix([])

def test_non_list_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_non_string_list():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["hello", 123, "world"])

def test_different_length_strings():
    """Test finding common suffix in strings of different lengths."""
    strings = ["longer", "short"]
    assert find_longest_common_suffix(strings) == ""

def test_unicode_strings():
    """Test finding common suffix with unicode strings."""
    strings = ["résumé", "causé", "passé"]
    assert find_longest_common_suffix(strings) == "ssé"

def test_whitespace_suffix():
    """Test common suffix that includes whitespace."""
    strings = ["hello world", "good world", "great world"]
    assert find_longest_common_suffix(strings) == " world"