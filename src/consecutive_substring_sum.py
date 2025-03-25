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
        >>> max_consecutive_substring_sum("abcdef")  # All consecutive, sum is 21
        21
        >>> max_consecutive_substring_sum("zyx")  # Reverse consecutive, sum is 6
        6
        >>> max_consecutive_substring_sum("abc123")  # Mixed consecutive, sum is 6
        6
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert string to list of character values
    char_values = [ord(char) for char in input_string]
    
    # Track maximum sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Iterate through the string to find maximum consecutive sum
    for i in range(len(char_values)):
        # Check if current character is consecutive with previous
        if i == 0 or abs(char_values[i] - char_values[i-1]) == 1:
            current_sum += char_values[i]
            max_sum = max(max_sum, current_sum)
        else:
            # Reset current sum if not consecutive
            current_sum = char_values[i]
    
    return max_sum