import pytest
from src.lowercase_converter import convert_to_lowercase

def test_convert_to_lowercase_basic():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase("HELLO") == "hello"
    assert convert_to_lowercase("World") == "world"
    assert convert_to_lowercase("python") == "python"

def test_convert_to_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_mixed_case():
    """Test conversion of mixed case string."""
    assert convert_to_lowercase("HeLLo WoRLd") == "hello world"

def test_convert_to_lowercase_with_numbers_and_symbols():
    """Test conversion of string with numbers and symbols."""
    assert convert_to_lowercase("Hello123!@#") == "hello123!@#"

def test_convert_to_lowercase_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(["list"])