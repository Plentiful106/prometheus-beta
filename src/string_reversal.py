"""
String Reversal Module

This module provides multiple methods for reversing a string.
"""

def reverse_string_manual(s: str) -> str:
    """
    Reverse a string using manual iteration.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_builtin(s: str) -> str:
    """
    Reverse a string using built-in reversed() function.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return ''.join(reversed(s))

def reverse_string_slice(s: str) -> str:
    """
    Reverse a string using string slicing.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return s[::-1]

def reverse_string_split_join(s: str) -> str:
    """
    Reverse a string using split(), reverse(), and join() methods.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return ''.join(list(s)[::-1])

def reverse_string_recursive(s: str) -> str:
    """
    Reverse a string recursively.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first char + reverse of the rest
    return reverse_string_recursive(s[1:]) + s[0]