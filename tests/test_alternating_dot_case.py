import pytest
from src.alternating_dot_case import convert_to_alternating_dot_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert convert_to_alternating_dot_case("hello") == 'h.E.l.L.o.'

def test_multiple_words():
    """Test conversion of multiple words."""
    assert convert_to_alternating_dot_case("hello world") == 'h.E.l.L.o. .W.o.R.l.D.'

def test_mixed_case_input():
    """Test input with mixed case."""
    assert convert_to_alternating_dot_case("Python") == 'P.y.T.h.O.n.'

def test_single_character():
    """Test single character input."""
    assert convert_to_alternating_dot_case("a") == 'a.'

def test_string_with_numbers_and_symbols():
    """Test input with numbers and symbols."""
    assert convert_to_alternating_dot_case("Hello123!") == 'h.E.l.L.o.1.2.3.!'

def test_empty_string_raises_error():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_dot_case("")

def test_non_string_input_raises_error():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(None)