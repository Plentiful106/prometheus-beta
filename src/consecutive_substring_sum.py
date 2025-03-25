def max_consecutive_substring_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The maximum sum of consecutive characters' ASCII values.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> max_consecutive_substring_sum("abcdef")  # Consecutive, returns 21 (sum of ASCII values)
        21
        >>> max_consecutive_substring_sum("zyx")  # Reverse consecutive, returns 6
        6
        >>> max_consecutive_substring_sum("abc123")  # Consecutive sequence returns sum
        294
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # For a single character, return its ASCII value
    if len(input_string) == 1:
        return ord(input_string[0])
    
    # Track maximum consecutive sum
    max_consecutive_sum = 0
    current_consecutive_sum = ord(input_string[0])
    
    for i in range(1, len(input_string)):
        # Check if current character is consecutive with previous
        if abs(ord(input_string[i]) - ord(input_string[i-1])) == 1:
            current_consecutive_sum += ord(input_string[i])
        else:
            # Compare and reset
            max_consecutive_sum = max(max_consecutive_sum, current_consecutive_sum)
            current_consecutive_sum = ord(input_string[i])
    
    # Final comparison
    max_consecutive_sum = max(max_consecutive_sum, current_consecutive_sum)
    
    return max_consecutive_sum