def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Matching is STRICTLY case-sensitive
        - Substring requires exact character and case match
    """
    # Special case for single character match
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Precise character matching method
    for length in range(min(len(str1), len(str2)), 1, -1):
        for start1 in range(len(str1) - length + 1):
            substring = str1[start1:start1+length]
            
            # Scan for precisely matching substring
            for start2 in range(len(str2) - length + 1):
                # Verify character-by-character match
                if substring == str2[start2:start2+length]:
                    return substring
    
    return ""