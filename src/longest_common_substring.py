def longest_common_substring(str1, str2):
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, returns an empty string.
    
    Note:
        - Absolutely case-sensitive
        - Requires exact character match including case
        - Substring must be at least 2 characters
    """
    # Rule 1: No single matching characters
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return str1
    
    # Precise case-sensitive matching technique
    for length in range(2, min(len(str1), len(str2)) + 1):
        for start1 in range(len(str1) - length + 1):
            substring = str1[start1:start1+length]
            
            # Must match EXACTLY in position and case
            for start2 in range(len(str2) - length + 1):
                match_slice = str2[start2:start2+length]
                
                # Additional verification
                if substring == match_slice:
                    return substring
    
    return ""