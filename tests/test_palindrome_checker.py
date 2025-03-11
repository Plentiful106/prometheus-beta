import pytest
from src.palindrome_checker import is_palindrome_number

def test_positive_palindrome_numbers():
    """Test various positive palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(1) == True

def test_non_palindrome_numbers():
    """Test various non-palindrome numbers."""
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(12345) == False

def test_negative_numbers():
    """Test handling of negative numbers."""
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == True

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)