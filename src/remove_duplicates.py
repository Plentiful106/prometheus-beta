def remove_duplicates_over_two(input_string):
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    
    Examples:
        >>> remove_duplicates_over_two("aabbbcccc")
        'aabbc'
        >>> remove_duplicates_over_two("hello")
        'hello'
        >>> remove_duplicates_over_two("aaaaabbbbbccccc")
        'ab'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Count character occurrences
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Build result string, keeping first two occurrences of chars that appear more than twice
    result = []
    seen_counts = {}
    for char in input_string:
        # Initialize count for the character if not seen before
        if char not in seen_counts:
            seen_counts[char] = 0
        
        # Add character if its count is less than 3
        if seen_counts[char] < 2:
            result.append(char)
        
        # Increment the count for this character
        seen_counts[char] += 1
    
    return ''.join(result)