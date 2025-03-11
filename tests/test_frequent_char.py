import pytest
from src.frequent_char import find_most_frequent_char

def test_find_most_frequent_char_normal_case():
    """Test finding most frequent character in a typical string."""
    assert find_most_frequent_char("hello") == 'l'

def test_find_most_frequent_char_all_unique():
    """Test string where all characters are unique."""
    assert find_most_frequent_char("abcde") == 'a'

def test_find_most_frequent_char_empty_string():
    """Test handling of empty string."""
    assert find_most_frequent_char("") is None

def test_find_most_frequent_char_multiple_max_freq():
    """Test when multiple characters have same highest frequency."""
    assert find_most_frequent_char("aabbcc") in ['a', 'b', 'c']

def test_find_most_frequent_char_with_spaces():
    """Test string with spaces."""
    assert find_most_frequent_char("a a a b b c") == 'a'

def test_find_most_frequent_char_with_special_chars():
    """Test string with special characters."""
    assert find_most_frequent_char("!!@@##a") == '!'

def test_find_most_frequent_char_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)