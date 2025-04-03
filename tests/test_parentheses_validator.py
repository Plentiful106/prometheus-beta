import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_basic_balanced_parentheses():
    """Test basic balanced parentheses scenarios"""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("((()))") == True

def test_nested_parentheses():
    """Test nested parentheses configurations"""
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("((()()))") == True

def test_unbalanced_parentheses():
    """Test unbalanced parentheses scenarios"""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("((") == False
    assert is_balanced_parentheses("())") == False
    assert is_balanced_parentheses(")(") == False

def test_empty_string():
    """Test empty string scenario"""
    assert is_balanced_parentheses("") == True

def test_string_with_other_characters():
    """Test strings containing other characters"""
    assert is_balanced_parentheses("hello(world)") == True
    assert is_balanced_parentheses("(test) string ()") == True
    assert is_balanced_parentheses("a(b)c(d)e") == True

def test_complex_scenarios():
    """Test more complex balanced and unbalanced configurations"""
    assert is_balanced_parentheses("((()(())))") == True
    assert is_balanced_parentheses("((()((()))))") == True
    assert is_balanced_parentheses("(()())(())") == True
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())()") == False