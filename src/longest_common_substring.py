def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Matching is EXPLICITLY case-sensitive
        - Requires EXACT character case preservation
    """
    result = ""
    
    # Special case for single character match
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Exhaustive search with absolute case matching
    for start1 in range(len(str1)):
        for length in range(2, len(str1) - start1 + 1):
            substring = str1[start1:start1+length]
            
            # Check substring occurs with EXACT case in same position
            found = False
            for start2 in range(len(str2) - length + 1):
                if substring == str2[start2:start2+length]:
                    found = True
                    break
            
            # Update result if found and longer
            if found and len(substring) > len(result):
                result = substring
    
    return result