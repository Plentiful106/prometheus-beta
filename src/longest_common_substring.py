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
    
    # Strict matching requires exact case preservation
    result = ""
    max_length = 0
    
    for i in range(len(str1)):
        for j in range(len(str2)):
            # Must be EXACT match
            current_match = ""
            k = 0
            while (i+k < len(str1) and 
                   j+k < len(str2) and 
                   str1[i+k] == str2[j+k]):
                current_match += str1[i+k]
                k += 1
            
            # Only update if this exact match is longer and meets criteria
            if len(current_match) > max_length:
                max_length = len(current_match)
                result = current_match
    
    # Strict requirements for substring
    return result if len(result) > 1 else ""