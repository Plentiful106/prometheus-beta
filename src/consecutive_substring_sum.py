def max_consecutive_substring_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The maximum sum of consecutive characters.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> max_consecutive_substring_sum("abcdef")  # Consecutive, returns 6
        6
        >>> max_consecutive_substring_sum("zyx")  # Consecutive decreasing, returns 3
        3
        >>> max_consecutive_substring_sum("abc123")  # Longest streak, returns 2
        2
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Track maximum consecutive characters
    max_consecutive = 1
    current_consecutive = 1
    
    for i in range(1, len(input_string)):
        # Check if characters are consecutive
        if abs(ord(input_string[i]) - ord(input_string[i-1])) == 1:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            # Reset current consecutive count
            current_consecutive = 1
    
    return max_consecutive