def is_palindrome_number(number: int) -> bool:
    """
    Check if a given number is a palindrome.
    
    A palindrome number reads the same backward as forward.
    
    Args:
        number (int): The number to check for palindrome property.
    
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(-121)
        False
        >>> is_palindrome_number(10)
        False
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Convert number to string for easy comparison
    # Use abs() to handle negative numbers
    str_number = str(abs(number))
    
    # Compare the string with its reverse
    return str_number == str_number[::-1]