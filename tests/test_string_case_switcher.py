import pytest
from src.string_case_switcher import switch_cases

def test_switch_cases_basic():
    """Test basic case swapping"""
    assert switch_cases("Hello", "WORLD") == "hELLO"
    assert switch_cases("AbCdE", "12345") == "aBcDe"

def test_switch_cases_all_uppercase():
    """Test swapping when first string is all uppercase"""
    assert switch_cases("HELLO", "world") == "hello"

def test_switch_cases_all_lowercase():
    """Test swapping when first string is all lowercase"""
    assert switch_cases("hello", "WORLD") == "HELLO"

def test_switch_cases_mixed_case():
    """Test swapping with mixed case inputs"""
    assert switch_cases("HeLlO", "WoRlD") == "hElLo"

def test_switch_cases_empty_strings():
    """Test with empty strings"""
    assert switch_cases("", "") == ""

def test_switch_cases_non_alphabetic():
    """Test with non-alphabetic characters"""
    assert switch_cases("A1b2C3", "D4e5F6") == "a1B2c3"

def test_switch_cases_different_length_error():
    """Test that different length strings raise ValueError"""
    with pytest.raises(ValueError, match="Input strings must have equal length"):
        switch_cases("Hello", "World!")

def test_switch_cases_non_string_error():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError, match="Both inputs must be strings"):
        switch_cases(123, "abc")
    with pytest.raises(TypeError, match="Both inputs must be strings"):
        switch_cases("abc", [1, 2, 3])