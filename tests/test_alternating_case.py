import pytest
from src.alternating_case import convert_to_alternating_lower_case

def test_convert_to_alternating_lower_case_normal_string():
    """Test conversion of a normal string."""
    assert convert_to_alternating_lower_case("Hello World") == 'hElLo wOrLd'

def test_convert_to_alternating_lower_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_lower_case("") == ''

def test_convert_to_alternating_lower_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_lower_case("A") == 'a'

def test_convert_to_alternating_lower_case_all_uppercase():
    """Test conversion of an all uppercase string."""
    assert convert_to_alternating_lower_case("HELLO") == 'hElLo'

def test_convert_to_alternating_lower_case_all_lowercase():
    """Test conversion of an all lowercase string."""
    assert convert_to_alternating_lower_case("hello") == 'hElLo'

def test_convert_to_alternating_lower_case_mixed_case():
    """Test conversion of a mixed case string."""
    assert convert_to_alternating_lower_case("HeLLo WoRLd") == 'hElLo wOrLd'

def test_convert_to_alternating_lower_case_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert convert_to_alternating_lower_case("Hello123 World!") == 'hElLo123 wOrLd!'

def test_convert_to_alternating_lower_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_lower_case(123)

def test_convert_to_alternating_lower_case_none_input():
    """Test that TypeError is raised for None input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_lower_case(None)