"""
Test module for string reversal functions.
"""

import pytest
from src.string_reversal import (
    reverse_string_manual, 
    reverse_string_builtin, 
    reverse_string_slice, 
    reverse_string_split_join, 
    reverse_string_recursive
)

# Test cases to cover various scenarios
TEST_CASES = [
    "",         # Empty string
    "a",        # Single character
    "hello",    # Regular string
    "12345",    # Numeric string
    "  trim  ", # String with whitespace
    "Madam, I'm Adam" # Palindrome with punctuation
]

# List of all reversal functions to test
REVERSAL_FUNCTIONS = [
    reverse_string_manual,
    reverse_string_builtin,
    reverse_string_slice,
    reverse_string_split_join,
    reverse_string_recursive
]

@pytest.mark.parametrize("func", REVERSAL_FUNCTIONS)
@pytest.mark.parametrize("input_str", TEST_CASES)
def test_string_reversal_valid_inputs(func, input_str):
    """
    Test that all reversal methods work correctly for valid inputs.
    """
    expected = input_str[::-1]
    assert func(input_str) == expected

@pytest.mark.parametrize("func", REVERSAL_FUNCTIONS)
def test_string_reversal_type_error(func):
    """
    Test that all reversal methods raise TypeError for non-string inputs.
    """
    with pytest.raises(TypeError, match="Input must be a string"):
        func(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        func(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        func(["list", "not", "string"])

def test_different_methods_consistency():
    """
    Verify that all reversal methods produce the same result.
    """
    test_string = "Python is awesome!"
    
    # Collect results from all methods
    results = [
        reverse_string_manual(test_string),
        reverse_string_builtin(test_string),
        reverse_string_slice(test_string),
        reverse_string_split_join(test_string),
        reverse_string_recursive(test_string)
    ]
    
    # Verify all results are identical
    assert len(set(results)) == 1, "All reversal methods should produce the same result"