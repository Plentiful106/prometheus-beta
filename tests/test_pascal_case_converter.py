import pytest
from src.pascal_case_converter import convert_to_pascal_case

def test_basic_conversion():
    """Test basic string to Pascal case conversion"""
    assert convert_to_pascal_case("hello world") == "HelloWorld"
    assert convert_to_pascal_case("python programming") == "PythonProgramming"

def test_snake_case_conversion():
    """Test converting snake_case to Pascal case"""
    assert convert_to_pascal_case("snake_case_example") == "SnakeCaseExample"

def test_kebab_case_conversion():
    """Test converting kebab-case to Pascal case"""
    assert convert_to_pascal_case("kebab-case-string") == "KebabCaseString"

def test_mixed_separators():
    """Test conversion with mixed separators"""
    assert convert_to_pascal_case("mixed_separators-test case") == "MixedSeparatorsTestCase"

def test_empty_string():
    """Test empty string conversion"""
    assert convert_to_pascal_case("") == ""
    assert convert_to_pascal_case("   ") == ""

def test_single_word():
    """Test single word conversion"""
    assert convert_to_pascal_case("hello") == "Hello"

def test_already_pascal_case():
    """Test string that is already in Pascal case"""
    assert convert_to_pascal_case("AlreadyPascalCase") == "AlreadyPascalCase"

def test_special_characters():
    """Test conversion with special characters"""
    assert convert_to_pascal_case("hello@world!test") == "HelloWorldTest"

def test_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        convert_to_pascal_case(None)
    
    with pytest.raises(TypeError):
        convert_to_pascal_case(123)
    
    with pytest.raises(TypeError):
        convert_to_pascal_case(["list", "of", "words"])