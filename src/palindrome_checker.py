def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome with complete case and character sensitivity.
    
    A palindrome reads the same backward as forward, taking into account 
    exact character and case matching.
    
    Args:
        s (str): The input string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("a")
        True
    """
    # Empty string or single character is always a palindrome
    if len(s) <= 1:
        return True
    
    # Compare characters from start and end, moving inwards
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True