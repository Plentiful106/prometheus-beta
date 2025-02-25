def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a lowercase string.
    
    Args:
        s (str): Input string containing only lowercase letters
    
    Returns:
        str | None: The first character that appears only once, or None if no such character exists
    
    Raises:
        ValueError: If the input string contains non-lowercase letters
    
    Examples:
        >>> first_non_repeating_character('aabcccdeeff')
        'b'
        >>> first_non_repeating_character('aabbcc')
        None
    """
    # Validate input 
    if not s or not s.islower():
        raise ValueError("Input must be a non-empty string of lowercase letters")
    
    # Count character frequencies
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find first character with count of 1
    for char in s:
        if char_counts[char] == 1:
            return char
    
    # No non-repeating character found
    return None