import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character_basic():
    """Test basic functionality of finding first non-repeating character"""
    assert first_non_repeating_character('aabcccdeeff') == 'b'
    assert first_non_repeating_character('leetcode') == 'l'
    assert first_non_repeating_character('loveleetcode') == 'v'

def test_first_non_repeating_character_no_non_repeating():
    """Test when no non-repeating character exists"""
    assert first_non_repeating_character('aabbcc') is None
    assert first_non_repeating_character('aaaa') is None

def test_first_non_repeating_character_single_char():
    """Test with a single character string"""
    assert first_non_repeating_character('a') == 'a'

def test_first_non_repeating_character_error_cases():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        first_non_repeating_character('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        first_non_repeating_character('AbC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        first_non_repeating_character('123')