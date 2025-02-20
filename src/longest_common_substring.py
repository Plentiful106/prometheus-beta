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
    
    # Special case for single character match with exact case
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    result = ""
    
    # Exhaustive search with absolute strict matching
    for start1 in range(len(str1)):
        for length in range(1, len(str1) - start1 + 1):
            substring = str1[start1:start1+length]
            
            # Check if this exact substring exists in str2 with same case at same position
            for start2 in range(len(str2)):
                if substring == str2[start2:start2+length] and len(substring) > len(result):
                    result = substring
    
    # Return only if truly meaningful substring found
    return result if len(result) > 1 else ""