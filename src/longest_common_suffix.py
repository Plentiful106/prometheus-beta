def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.

    Args:
        strings (list): A list of strings to compare.

    Returns:
        str: The longest common suffix. If no common suffix exists, 
             returns an empty string.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # If only one string, return the entire string as suffix
    if len(strings) == 1:
        return strings[0]
    
    # Find the minimum length of all strings
    min_length = min(len(s) for s in strings)
    
    # Check suffixes from longest to shortest
    for length in range(min_length, 0, -1):
        current_common_suffix = strings[0][-length:]
        
        # Check if this suffix is common to all strings
        if all(s.endswith(current_common_suffix) for s in strings):
            return current_common_suffix
    
    # If no common suffix found
    return ""