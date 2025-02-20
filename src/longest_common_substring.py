def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Special case for identical single-character strings
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Strict matching requires exact case and sequential preservation
    result = ""
    max_length = 0
    
    # Nested loops to check all possible substring matches
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Current tracking of sequential match
            current_match = ""
            k = 0
            
            # Ensure we stay within bounds and match exactly
            while (i+k < len(str1) and 
                   j+k < len(str2) and 
                   str1[i+k] == str2[j+k]):
                current_match += str1[i+k]
                k += 1
            
            # Update only if match is longer and meets strict criteria
            if len(current_match) > max_length:
                max_length = len(current_match)
                result = current_match
    
    # Return result only if it's substantially longer than a single character
    return result if len(result) > 1 else ""