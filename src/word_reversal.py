def reverse_words(input_string: str) -> str:
    """
    Reverses the order of words in a given string.
    
    Args:
        input_string (str): The input string to reverse.
    
    Returns:
        str: A new string with words in reversed order.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("Python is awesome")
        'awesome is Python'
    """
    # Handle edge cases
    if not input_string:
        return ""
    
    # Split the string into words and reverse their order
    words = input_string.split()
    return " ".join(words[::-1])