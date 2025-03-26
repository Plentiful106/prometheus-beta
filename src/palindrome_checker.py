def is_palindrome(input_string: str) -> bool:
    """
    Determine if the given string is a palindrome.

    A palindrome reads the same forward and backward, ignoring spaces, 
    punctuation, and letter case.

    Args:
        input_string (str): The string to check for palindrome properties.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("123321")
        True
        >>> is_palindrome("")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Check if the cleaned string reads the same forward and backward
    return cleaned_string == cleaned_string[::-1]