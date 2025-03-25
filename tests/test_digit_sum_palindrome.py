import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_true_cases():
    """Test cases where the digit sum is a palindrome."""
    test_cases = [
        56,    # 5 + 6 = 11 (palindrome)
        89,    # 8 + 9 = 17 (not palindrome)
        100,   # 1 + 0 + 0 = 1 (palindrome)
        0,     # 0 (palindrome)
        11,    # 1 + 1 = 2 (palindrome)
    ]
    
    expected_results = [
        True,
        False,
        True,
        True,
        True
    ]
    
    for num, expected in zip(test_cases, expected_results):
        assert is_digit_sum_palindrome(num) == expected, f"Failed for {num}"

def test_digit_sum_palindrome_error_cases():
    """Test error handling for invalid inputs."""
    error_cases = [
        -1,        # Negative number
        3.14,      # Float
        "123",     # String
        None       # None
    ]
    
    for invalid_input in error_cases:
        with pytest.raises(ValueError, match="Input must be a non-negative integer"):
            is_digit_sum_palindrome(invalid_input)

def test_large_numbers():
    """Test function with larger numbers."""
    test_cases = [
        12345,     # 1 + 2 + 3 + 4 + 5 = 15 (not palindrome)
        10001,     # 1 + 0 + 0 + 0 + 1 = 2 (palindrome)
    ]
    
    expected_results = [
        False,
        True
    ]
    
    for num, expected in zip(test_cases, expected_results):
        assert is_digit_sum_palindrome(num) == expected, f"Failed for {num}"