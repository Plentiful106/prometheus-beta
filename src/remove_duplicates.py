def remove_duplicate_chars(input_string: str) -> str:
    """
    Remove duplicate characters from the input string while preserving the original order.

    Args:
        input_string (str): A lowercase string from which duplicates should be removed.

    Returns:
        str: A string with duplicate characters removed, maintaining the first occurrence order.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input contains non-lowercase characters.

    Examples:
        >>> remove_duplicate_chars("hello")
        'helo'
        >>> remove_duplicate_chars("aabbcc")
        'abc'
        >>> remove_duplicate_chars("")
        ''
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Validate lowercase characters
    if not input_string.islower():
        raise ValueError("Input must contain only lowercase characters")
    
    # Use a set to track seen characters while preserving order
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)